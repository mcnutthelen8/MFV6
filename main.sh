#!/usr/bin/env bash
set -o nounset
set -o pipefail

trap "echo '[!] Interrupted by user, exiting.'; exit 0" SIGINT

SCRIPT_CMD="python3 main4.py --farm 1 --fresh 3"
GRACE_PERIOD=90
FORCE_CPU=95
FORCE_RAM=5000
CRITICAL_RAM=6200
OVERLOAD_DURATION=40
MONITOR_INTERVAL=5
FORCE_RESTART_AFTER=1800
IDLE_LIMIT=250
LOG_FILE="watchdog.txt"

kill_all() {
    local pid="${1:-}"
    echo "[⚠] Killing PID $pid and all Chrome and python3 processes at $(date)" | tee -a "$LOG_FILE"
    [[ -n "$pid" ]] && kill "$pid" 2>/dev/null || true
    sleep 2
    [[ -n "$pid" ]] && kill -9 "$pid" 2>/dev/null || true
    pkill -f "chrome" 2>/dev/null || true
    pkill -f "python3" 2>/dev/null || true
}

while true; do
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] === 🔄 Cleaning up old processes ===" | tee -a "$LOG_FILE"
    kill_all

    echo "[$(date '+%Y-%m-%d %H:%M:%S')] === 🚀 Starting new session ===" | tee -a "$LOG_FILE"
    eval "$SCRIPT_CMD" &
    PID=$!
    overload_start=0
    idle_proc_count=0
    session_start=$(date +%s)

    echo "[⏳] Waiting $GRACE_PERIOD seconds for setup..." | tee -a "$LOG_FILE"
    sleep "$GRACE_PERIOD"

    while kill -0 "$PID" 2>/dev/null; do
        now=$(date +%s)
        elapsed_session=$(( now - session_start ))

        # CPU usage
        if command -v mpstat &>/dev/null; then
            cpu_idle=$(mpstat 1 1 | awk '/Average/ {print $12}')
            cpu_usage=$(echo "100 - $cpu_idle" | bc)
        else
            cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk -F',' '{print $4}' | awk '{print $1}')
            cpu_usage=$(echo "100 - $cpu_idle" | bc)
        fi
        cpu_int=${cpu_usage%.*}
        if [[ -z "$cpu_int" ]]; then cpu_int=0; fi

        # RAM usage
        ram_usage=$(free -m | awk '/^Mem:/ {print $3}')

        # Idle user detection
        idle_ms=$(xprintidle 2>/dev/null || echo 0)
        idle_sec=$(( idle_ms / 1000 ))

        echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] CPU=${cpu_int}% RAM=${ram_usage}MB Idle=${idle_sec}s" | tee -a "$LOG_FILE"

        # Emergency restart if RAM is dangerously high
        if (( ram_usage >= CRITICAL_RAM )); then
            echo "[🚨] Critical RAM usage (${ram_usage}MB). Restarting immediately!" | tee -a "$LOG_FILE"
            kill_all "$PID"
            break
        fi

        # Force restart after set duration
        if (( elapsed_session >= FORCE_RESTART_AFTER )); then
            echo "[⏱] Force restart after 1 hour ($elapsed_session sec)" | tee -a "$LOG_FILE"
            kill_all "$PID"
            break
        fi

        # Restart if user is idle too long
        if (( idle_sec >= IDLE_LIMIT )); then
            echo "[💤] No user input for $idle_sec seconds. Restarting..." | tee -a "$LOG_FILE"
            kill_all "$PID"
            break
        fi

        # Sustained overload detection
        if (( cpu_int > FORCE_CPU )) || (( ram_usage > FORCE_RAM )); then
            if [[ $overload_start -eq 0 ]]; then
                overload_start=$now
            else
                overload_elapsed=$(( now - overload_start ))
                echo "[🔥] High usage | Elapsed: ${overload_elapsed}s" | tee -a "$LOG_FILE"
                if (( overload_elapsed >= OVERLOAD_DURATION )); then
                    echo "[🔥] High usage sustained. Restarting..." | tee -a "$LOG_FILE"
                    kill_all "$PID"
                    break
                fi
            fi
        else
            overload_start=0
        fi

        # Optional: Detect frozen process with near 0% CPU
        pid_cpu=$(ps -p "$PID" -o %cpu= | awk '{print int($1)}')
        if (( pid_cpu < 1 )); then
            idle_proc_count=$(( idle_proc_count + 1 ))
        else
            idle_proc_count=0
        fi

        if (( idle_proc_count >= 5 )); then
            echo "[🐌] Process appears frozen (CPU=${pid_cpu}%) for too long. Restarting..." | tee -a "$LOG_FILE"
            kill_all "$PID"
            break
        fi

        sleep "$MONITOR_INTERVAL"
    done

    sleep 10
done
