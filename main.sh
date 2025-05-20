

#!/usr/bin/env bash
set -o nounset
set -o pipefail

trap "echo '[!] Interrupted by user, exiting.'; exit 0" SIGINT

SCRIPT_CMD="python3 main3.py --farm 1 --fresh 3"
GRACE_PERIOD=80
FORCE_CPU=95
FORCE_RAM=3700
OVERLOAD_DURATION=14
MONITOR_INTERVAL=5
FORCE_RESTART_AFTER=1800       # Force restart after 1 hour
IDLE_LIMIT=180                 # Idle limit in seconds (3 minutes)
LOG_FILE="watchdog.txt"

kill_all() {
    local pid="${1:-}"
    if [[ -n "$pid" ]]; then
        echo "[⚠] Killing PID $pid and all Chrome and python3 processes at $(date)" | tee -a "$LOG_FILE"
        kill "$pid" 2>/dev/null || true
        sleep 2
        kill -9 "$pid" 2>/dev/null || true
    else
        echo "[⚠] No PID provided. Killing all Chrome and python3 processes at $(date)" | tee -a "$LOG_FILE"
    fi
    pkill -f "main3.py" 2>/dev/null || true
    pkill -f "chrome" 2>/dev/null || true
}



while true; do
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] === 🚀 Starting new session ===" | tee -a "$LOG_FILE"
    kill_all
    eval "$SCRIPT_CMD" &
    PID=$!
    overload_start=0
    session_start=$(date +%s)

    echo "[⏳] Waiting $GRACE_PERIOD seconds for setup..." | tee -a "$LOG_FILE"
    sleep "$GRACE_PERIOD"

    while kill -0 "$PID" 2>/dev/null; do
        # Get current time and elapsed time
        now=$(date +%s)
        elapsed_session=$(( now - session_start ))

        # CPU usage check
        if command -v mpstat &>/dev/null; then
            cpu_idle=$(mpstat 1 1 | awk '/Average/ {print $12}')
            cpu_usage=$(echo "100 - $cpu_idle" | bc)
        else
            cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk -F',' '{print $4}' | awk '{print $1}')
            cpu_usage=$(echo "100 - $cpu_idle" | bc)
        fi

        cpu_int=${cpu_usage%.*}
        if [[ -z "$cpu_int" ]]; then cpu_int=0; fi

        ram_usage=$(free -m | awk '/^Mem:/ {print $3}')

        # IDLE detection via xprintidle
        idle_ms=$(xprintidle 2>/dev/null || echo 0)
        idle_sec=$(( idle_ms / 1000 ))

        # Log optional
        #echo "[INFO] CPU=${cpu_int}% RAM=${ram_usage}MB Idle=${idle_sec}s" | tee -a "$LOG_FILE"

        # Force restart after 1 hour
        if (( elapsed_session >= FORCE_RESTART_AFTER )); then
            echo "[⏱] Force restart after 1 hour ($elapsed_session sec)" | tee -a "$LOG_FILE"
            kill_all "$PID"
            break
        fi

        # Idle user detection
        if (( idle_sec >= IDLE_LIMIT )); then
            echo "[💤] No user input for $idle_sec seconds. Restarting..." | tee -a "$LOG_FILE"
            kill_all "$PID"
            break
        fi

        # Resource overload check
        if (( ram_usage > FORCE_RAM )); then
            if [[ $overload_start -eq 0 ]]; then
                overload_start=$(date +%s)
            else
                elapsed=$(( now - overload_start ))
                echo "[🔥] High usage | Elapsed: ${elapsed}s" | tee -a "$LOG_FILE"
                echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] CPU=${cpu_usage}% | RAM=${ram_usage}MB" | tee -a "$LOG_FILE"
                if (( elapsed >= OVERLOAD_DURATION )); then
                    echo "[🔥] High usage sustained. Restarting..." | tee -a "$LOG_FILE"
                    kill_all "$PID"
                    break
                fi
            fi
        else
            overload_start=0
        fi

        sleep "$MONITOR_INTERVAL"
    done

    sleep 10
done
