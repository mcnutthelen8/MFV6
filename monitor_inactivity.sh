#!/bin/bash

# Set timeout in milliseconds (4 minutes = 240,000 ms)
TIMEOUT=240000

# Path to your Python script
PYTHON_SCRIPT="python3 main.py --farm 1 --fresh 3"

# Function to kill chrome and python processes
kill_processes() {
    pkill -f chrome      # Kills Chrome processes
    pkill -f python      # Kills Python processes
}

# Function to restart the script
restart_script() {
    $PYTHON_SCRIPT &
}

# Infinite loop to check idle time
while true; do
    # Get the idle time in milliseconds
    idle_time=$(xprintidle)

    # Check if idle time exceeds the timeout threshold
    if [ "$idle_time" -gt "$TIMEOUT" ]; then
        echo "Inactivity detected for more than 4 minutes. Restarting..."

        # Kill all Chrome and Python processes
        kill_processes

        # Restart the script
        restart_script
    fi

    # Sleep for a while before checking again (optional: avoid continuous polling)
    sleep 5
done
