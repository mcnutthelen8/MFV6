#!/bin/bash

trap "echo '=Ñ Script interrupted by user. Exiting...'; exit" SIGINT

while true; do
    idle_ms=$(xprintidle)
    if [ "$idle_ms" -gt 300000 ]; then
        echo "=¤ System idle for more than 5 minutes. Pausing..."
        sleep 60
        continue
    fi

    echo "= Starting Python script at $(date)..."
    timeout 3600 python3 main5.py --farm 2 --fresh 3
    echo "ù Script ended or timed out at $(date)."

    pkill -f chrome
    pkill -f main5.py

    echo "=R Restarting in 10 seconds..."
    sleep 10
done
