
#!/usr/bin/env bash
set -o nounset      # error on undefined variables
set -o pipefail     # catch failing pipes
# (We *dont* set -e because we want the loop to continue on non-fatal errors.)

# 1) Trap Ctrl+C so it exits cleanly
trap "echo '[] Interrupted by userexiting.'; exit 0" SIGINT

# 2) Configuration
IDLE_LIMIT=300000       # 5 min in ms
SCRIPT_TIMEOUT=4000     # 1 hour in s
GRACE_PERIOD=220         #  1 min in s
SCRIPT_CMD="python3 main5.py --farm 1 --fresh 3"

# 3) Make sure xprintidle is available
if ! command -v xprintidle &>/dev/null; then
  echo "[W] xprintidle not found. Please: sudo apt install xprintidle"
  exit 1
fi

# 4) Main loop: runs forever until the VPS is powered off or you kill this launcher
while true; do
  echo "=== =聙 Launching at $(date) ==="

  # 5) Start your Python script with a hard timeout
  timeout "$SCRIPT_TIMEOUT" $SCRIPT_CMD &
  PID=$!

  # 6) Give it a grace period to do its first pyautogui.move()
  echo "[贸] Waiting $GRACE_PERIOD s for PyAutoGUI to move the mouse&"
  sleep "$GRACE_PERIOD"

  # 7) Monitor for idleness
  while kill -0 "$PID" 2>/dev/null; do
    idle=$(xprintidle)
    if [ "$idle" -gt "$IDLE_LIMIT" ]; then
      echo "[L] Detected $((idle/1000)) s of idlekilling script at $(date)."
      kill -9 "$PID"        || true
      pkill -f chrome        || true
      break
    fi
    sleep 5
  done

  # 8) Cleanup & wait before next restart
  echo "[=] Restarting in 10 s at $(date)&"
  pkill -f chrome  || true
  pkill -f main5.py || true
  sleep 10
done
