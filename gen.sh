#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Requires an arg" >&2
    exit 1
fi

TARGET_DIR=$1

if [ -e "$TARGET_DIR" ]; then
    echo "${TARGET_DIR} already exists." >&2
    exit 1
fi

echo atcoder-tools gen --lang python --workspace . --template ./atcoder_template.py "$TARGET_DIR"
atcoder-tools gen --lang python --workspace . --template ./atcoder_template.py "$TARGET_DIR"
