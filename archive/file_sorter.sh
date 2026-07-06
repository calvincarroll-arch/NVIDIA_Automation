#!/bin/bash

# ==========================================
# Iron Logic LLC: Parameter & Loop Organizer
# ==========================================

# 1. THE BOUNCER ($#)
# $# holds the NUMBER of arguments the user typed. 
# We require exactly 2: the extension ($1) and the folder name ($2).
if [ $# -ne 2 ]; then
    echo "[ERROR] Invalid usage."
    echo "Usage: $0 <extension> <target_folder>"
    echo "Example: $0 txt my_text_files"
    exit 1
fi

# 2. VARIABLE ASSIGNMENT FROM POSITIONAL PARAMETERS
EXTENSION=$1
TARGET_DIR=$2

echo "--- Iron Logic Sorter Initialized ---"
echo "Target Extension : .$EXTENSION"
echo "Destination Folder: $TARGET_DIR"

# 3. DIRECTORY PREP (LBYL - Look Before You Leap)
if [ ! -d "$TARGET_DIR" ]; then
    echo "Creating directory: $TARGET_DIR"
    mkdir "$TARGET_DIR"
fi

# 4. THE ASSEMBLY LINE (for loop)
# We use a glob to find all files ending in the chosen extension
echo "Starting sort..."
COUNT=0

for FILE in *."$EXTENSION"; do
    # Safety Check: If no files match, the loop might try to move a literal file named '*.txt'
    if [ -e "$FILE" ]; then
        mv "$FILE" "$TARGET_DIR/"
        echo " -> Moved: $FILE"
        COUNT=$((COUNT + 1))
    fi
done

echo "--- Sort Complete ---"
echo "Total files moved: $COUNT"

