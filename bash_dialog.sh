#!/bin/bash

# Create a form with two input fields
response=$(dialog --title "Input Form" --form "Enter your details" 15 50 0 \
    "First Input:" 1 1 "" 1 20 20 \
    "Second Input:" 2 1 "" 2 20 20 \
    3>&1 1>&2 2>&3)

# Separate the inputs
first_input=$(echo "$response" | sed -n '1p')
second_input=$(echo "$response" | sed -n '2p')

echo "First Input: $first_input"
echo "Second Input: $second_input"
