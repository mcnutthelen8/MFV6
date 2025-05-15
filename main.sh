#!/usr/bin/env bash
set -o nounset
set -o pipefail

# Trap Ctrl+C to exit cleanly
trap "echo '[!] Interrupted by user, exiting.'; exit 0" SIGINT

# Configuration
IDLE_LIMIT_MS=150000       # 2.4 minutes in milliseconds
GRACE_PERIOD=200            # Initial wait time in seconds
SCRIPT_CMD="python3 main4.py --farm 1 --fresh 3"
FORCE_RESTART_INTERVAL=1800  # 30 minutes in seconds

# Check if xprintidle is installed
if ! command -v xprintidle &>/dev/null; then
    echo "[W] xprintidle not found. Please: sudo apt install xprintidle"
    exit 1
fi

# Function to kill script and Chrome gracefully
kill_all() {
    local pid="$1"
    echo "[⚠] Killing process $pid and Chrome at $(date)"
    kill "$pid" 2>/dev/null || true
    sleep 2
    kill -9 "$pid" 2>/dev/null || true
    pkill -f "chrome" 2>/dev/null || true
    pkill -f "main5.py" 2>/dev/null || true
}

while true; do
    echo "=== 🚀 Launching at $(date) ==="
    eval "$SCRIPT_CMD" &
    PID=$!
    START_TIME=$(date +%s)

    echo "[⏳] Waiting $GRACE_PERIOD seconds for PyAutoGUI to move the mouse..."
    sleep "$GRACE_PERIOD"

    while kill -0 "$PID" 2>/dev/null; do
        IDLE_TIME_MS=$(xprintidle)
        NOW=$(date +%s)
        ELAPSED=$(( NOW - START_TIME ))

        if [ "$IDLE_TIME_MS" -gt "$IDLE_LIMIT_MS" ]; then
            echo "[⚠️] Idle time exceeded: $((IDLE_TIME_MS / 1000)) seconds"
            kill_all "$PID"
            break
        fi

        if [ "$ELAPSED" -ge "$FORCE_RESTART_INTERVAL" ]; then
            echo "[🔄] 30 minutes elapsed, restarting script at $(date)"
            kill_all "$PID"
            break
        fi

        sleep 5
    done

    echo "[🔁] Restarting in 10 seconds at $(date)..."
    sleep 10
done
