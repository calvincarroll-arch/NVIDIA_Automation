#!/bin/bash

# ==========================================
# Iron Logic LLC: Conditional Logic Test
# ==========================================

TARGET_FILE="node_status.log"

echo "--- Phase 1: The Missing File Test ---"

# The '-e' flag checks if the file Exists.
# Notice the mandatory spaces inside the brackets!
if [ -e "$TARGET_FILE" ]; then
    echo "[PASS] $TARGET_FILE found. Proceeding with rename..."
    mv "$TARGET_FILE" "archived_$TARGET_FILE"
else
    echo "[BLOCKED] $TARGET_FILE does not exist! Skipping rename to prevent system errors."
fi

echo " "
echo "--- Phase 2: Creating the file and retrying ---"
touch "$TARGET_FILE"
echo "System simulated file creation: $TARGET_FILE"
echo " "

# We run the exact same logic block again
if [ -e "$TARGET_FILE" ]; then
    echo "[PASS] $TARGET_FILE found. Proceeding with rename..."
    mv "$TARGET_FILE" "archived_$TARGET_FILE"
    echo "Operation Complete. Run 'ls -l' to verify."
else
    echo "[BLOCKED] $TARGET_FILE does not exist! Skipping rename to prevent system errors."
fi

