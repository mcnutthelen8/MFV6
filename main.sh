\#!/usr/bin/env bash
set -o nounset
set -o pipefail

# Trap Ctrl+C to exit cleanly

trap "echo '\[!] Interrupted by user, exiting.'; exit 0" SIGINT

# Configuration

IDLE\_LIMIT=160000       # 5 minutes in ms
GRACE\_PERIOD=200        # Initial wait time in seconds
SCRIPT\_CMD="python3 main5.py --farm 1 --fresh 3"
FORCE\_RESTART\_INTERVAL=1800  # 20 minutes in seconds

# Check if xprintidle is installed

if ! command -v xprintidle &>/dev/null; then
echo "\[W] xprintidle not found. Please: sudo apt install xprintidle"
exit 1
fi

while true; do
echo "=== 🚀 Launching at \$(date) ==="

# Start the Python script

\$SCRIPT\_CMD &
PID=\$!

# Record start time for forced restart

start\_time=\$(date +%s)

echo "\[⏳] Waiting \$GRACE\_PERIOD seconds for PyAutoGUI to move the mouse..."
sleep "\$GRACE\_PERIOD"

while kill -0 "\$PID" 2>/dev/null; do
idle=\$(xprintidle)
now=\$(date +%s)
elapsed=\$(( now - start\_time ))

```
# Kill if idle too long
if [ "$idle" -gt "$IDLE_LIMIT" ]; then
  echo "[⚠️] Detected $((idle/1000))s of idle. Killing script at $(date)."
  kill -9 "$PID" 2>/dev/null || true
  pkill -f chrome 2>/dev/null || true
  break
fi

# Force restart every 20 minutes regardless of idle
if [ "$elapsed" -ge "$FORCE_RESTART_INTERVAL" ]; then
  echo "[⏳] 20 minutes elapsed. Force restarting script at $(date)."
  kill -9 "$PID" 2>/dev/null || true
  pkill -f chrome 2>/dev/null || true
  break
fi

sleep 5
```

done

echo "\[🔄] Restarting in 10 seconds at \$(date)..."
pkill -f chrome 2>/dev/null || true
pkill -f main5.py 2>/dev/null || true
sleep 10
done

explain
