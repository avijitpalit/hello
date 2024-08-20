#!/bin/bash

response=$(zenity --forms --title="Overwrite Prompt" --text="Enter your details" \
    --add-entry="Prompt" \
    --add-entry="Negative_prompt")

# Extract the individual inputs
first_input=$(echo "$response" | awk -F '|' '{print $1}')
second_input=$(echo "$response" | awk -F '|' '{print $2}')

echo "First Input: $first_input"
echo "Second Input: $second_input"