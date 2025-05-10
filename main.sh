#!/usr/bin/env bash
set -o nounset
set -o pipefail

# Trap Ctrl+C to exit cleanly
trap "echo '[!] Interrupted by user, exiting.'; exit 0" SIGINT

# Configuration
IDLE_LIMIT=200000       # 5 minutes in ms
GRACE_PERIOD=200        # Initial wait time in seconds
SCRIPT_CMD="python3 main5.py --farm 1 --fresh 3"

# Check if xprintidle is installed
if ! command -v xprintidle &>/dev/null; then
  echo "[W] xprintidle not found. Please: sudo apt install xprintidle"
  exit 1
fi

# Infinite loop
while true; do
  echo "=== 🚀 Launching at $(date) ==="

  # Start the Python script
  $SCRIPT_CMD &
  PID=$!

  # Wait for initial movement
  echo "[⏳] Waiting $GRACE_PERIOD seconds for PyAutoGUI to move the mouse..."
  sleep "$GRACE_PERIOD"

  # Monitor for user idleness
  while kill -0 "$PID" 2>/dev/null; do
    idle=$(xprintidle)
    if [ "$idle" -gt "$IDLE_LIMIT" ]; then
      echo "[⚠️] Detected $((idle/1000))s of idle. Killing script at $(date)."
      kill -9 "$PID" 2>/dev/null || true
      pkill -f chrome 2>/dev/null || true
      break
    fi
    sleep 5
  done

  # Wait before restarting
  echo "[🔄] Restarting in 10 seconds at $(date)..."
  pkill -f chrome 2>/dev/null || true
  pkill -f main5.py 2>/dev/null || true
  sleep 10
done
