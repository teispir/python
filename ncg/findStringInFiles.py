def find_string_in_file(filepath, target_string):
    lines_with_string = []
    with open(filepath, 'r') as file:
        for line in file:
            if target_string in line:
                lines_with_string.append(line)
    return lines_with_string
	
filepath = "path/to/your/file.txt"
target_string = "string you want to find"
string = find_string_in_file(filepath, target_string)
print(string)	