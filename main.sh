#!/bin/bash

trap "echo '= Script interrupted by user. Exiting...'; exit" SIGINT

IDLE_LIMIT=300000       # 5 minutes in ms
SCRIPT_TIMEOUT=3600     # 1 hour max run time
GRACE_PERIOD=250         # 1 minute grace after script starts
SCRIPT="python3 main5.py --farm 2 --fresh 3"

while true; do
    idle_ms=$(xprintidle)
    if [ "$idle_ms" -gt "$IDLE_LIMIT" ]; then
        echo "==脩 System already idle for 5+ minutes. Waiting for user activity..."

        # Kill any running instances
        pkill -f main5.py
        pkill -f chrome

        # Wait until user becomes active
        while [ "$(xprintidle)" -gt "$IDLE_LIMIT" ]; do
            sleep 5
        done

        echo "= User is active again. Continuing..."
    fi

    echo "==聙 Starting Python script at $(date)..."
    timeout "$SCRIPT_TIMEOUT" $SCRIPT &
    SCRIPT_PID=$!

    # Wait for grace period before checking idleness
    echo "=贸 Waiting $GRACE_PERIOD seconds grace before checking idle..."
    sleep $GRACE_PERIOD

    # Monitor script for idle timeout
    while kill -0 $SCRIPT_PID 2>/dev/null; do
        idle_now=$(xprintidle)
        if [ "$idle_now" -gt "$IDLE_LIMIT" ]; then
            echo "=聽  Idle detected during script. Killing script..."
            kill -9 $SCRIPT_PID
            pkill -f chrome
            break
        fi
        sleep 5
    done

    echo "== Restart loop in 10 seconds at $(date)..."
    sleep 10
done
