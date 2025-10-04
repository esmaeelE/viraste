# force to RTL


# read a file line by line add char

# U+202E
char_to_add = "‮"
char_to_add.encode("utf8")

# Open the file in read mode
with open("input.txt", "r", encoding="utf-8") as file:
    # Read lines and add the character to the start of each line
    modified_lines = [char_to_add + line for line in file]

    # Optionally, write the modified lines to a new file
with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(modified_lines)
