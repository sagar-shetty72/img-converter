#!/bin/bash
# Activate the virtual environment
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/.venv/bin/activate"

# Define the input/output file paths
INPUT_FILE="$SCRIPT_DIR/$1"
OUTPUT_FILE="$SCRIPT_DIR/$2"

# Run the Python script
python3 "$SCRIPT_DIR/img_converter.py" "$INPUT_FILE" "$OUTPUT_FILE" "$3"
