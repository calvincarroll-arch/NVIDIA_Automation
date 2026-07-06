#!/bin/bash

# ==========================================
# Iron Logic LLC: Variable & Glob Diagnostic
# ==========================================

# 1. VARIABLE ASSIGNMENT (Notice: No spaces around '=')
WORKSPACE_DIR="iron_logic_staging"
TODAY=$(date +%F) # Command substitution assigned to a variable

echo "--- Initializing Protocol for $TODAY ---"

# 2. ENVIRONMENT PREP
# Create a fresh directory and some mixed dummy files to test our globs
mkdir -p "$WORKSPACE_DIR"
cd "$WORKSPACE_DIR" || exit

touch network_node1.log
touch network_node2.log
touch database_main.log
touch user_configs.txt
touch system_keys.pem

echo "Created test files in $WORKSPACE_DIR:"
ls -l

echo " "
echo "--- Executing Glob Search ---"

# 3. THE GLOB IN ACTION (*.log)
# We are telling the loop to only look at files ending in .log
for FILE in *.log; do
    # Using safety wrapping ${} to append text to the variable
    NEW_NAME="${TODAY}_${FILE}"
    
    # Rename the file
    mv "$FILE" "$NEW_NAME"
    echo "Processed: $FILE -> renamed to $NEW_NAME"
done

echo " "
echo "--- Final Directory State ---"
# Notice that .txt and .pem files were completely ignored by the glob
ls -l

# Return to original directory
cd ..