#!/bin/bash
# question 1
# for file in *.txt; do
#     if [ -f "$file" ]; then
#         mv -- "$file" "${file%.txt}.bak"
#         echo "rename is complited"
#     fi
# done

# question 2
# read -p "gimme a name for a file: " filename
# if [! -f "$filename"]; then
#     touch "$filename"
#     echo "file created"
# else 
#     if [! -s "$filename"]; then
#         echo "file is empty"
#     else 
#         line_count=$(wc -1 < "$filename")
#         echo "$filename" has "$line_count" lines
#     fi
# fi

# question3
# read -p "gimme a file name: " filename
# read -p "gimme a text: " user_string

# if [ ! -f "$filename" ]; then
#     echo "$user_string" > "$filename"
#     echo "file created and content added"
# else
#     count=$(grep -oF "$user_string" "$filename" | wc -l)
#     if [ "$count" -gt 0 ]; then
#         echo "'$user_string' exists $count times in '$filename'."
#     else
#         echo "$user_string" >> "$filename"
#         echo "'$user_string' was not found. added to the end of '$filename'."
#     fi
# fi