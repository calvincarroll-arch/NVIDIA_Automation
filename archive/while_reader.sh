#!/bin/bash

# ==========================================
# Iron Logic LLC: The While-Read Pipeline
# ==========================================

TARGET_FILE=$1

# Safety Check
if [ ! -e "$TARGET_FILE" ]; then
    echo "[ERROR] Cannot find file: $TARGET_FILE"
    exit 1
fi

echo "--- Commencing Server Roster Scan ---"

# THE WHILE LOOP
# 'read -r LINE' pulls one line of text at a time from the file.
# The loop keeps spinning as long as 'read' successfully pulls a line.
while read -r LINE; do
    
    echo "Pinging Target: $LINE"
    
    # We use a ping command. 
    # -c 1 means "send exactly 1 ping packet"
    # -W 1 means "only wait 1 second for a reply" (don't hang forever)
    # > /dev/null throws away the messy output so our screen stays clean.
    ping -c 1 -W 1 "$LINE" > /dev/null 2>&1
    
    # We check the exit status ($?) of the ping command.
    if [ $? -eq 0 ]; then
        echo "  [SUCCESS] Server $LINE is ONLINE."
    else
        echo "  [FAILED] Server $LINE is unreachable!"
    fi

# The '<' operator at the end feeds the entire TARGET_FILE into the loop's input.
done < "$TARGET_FILE"

echo "--- Scan Complete ---"

