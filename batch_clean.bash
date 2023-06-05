#!/bin/bash

# Save the output of find to a file
find /scratch/bf996/datasets/commoncrawl -type f > filelist.txt

min_lines=50

# Iterate over the file
while IFS= read -r file
do
    # Run command and capture output
    num_lines=$(cat "$file" | wc -l)
    # Set the value you want to check against

    # Check if num_lines is less than max_lines
    if (( num_lines < min_lines )); then
        rm -f "$file"
    fi
done < filelist.txt