#!/bin/bash
echo "Parsing and Analyzing folder: "

if [[ $# -gt 1 ]]; then
echo "Usage: bash gdiff.sh <path to Software>"
echo "More than one argument. Exit..."
exit 0
fi

APP_PATH="$1"

echo "${APP_PATH}"

cd "${APP_PATH}"
pwd
