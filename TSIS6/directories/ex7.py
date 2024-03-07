def copy_file(source_filename, destination_filename):
    with open(source_filename, 'r') as source_file:
        with open(destination_filename, 'w') as destination_file:
            for line in source_file:
                destination_file.write(line)

source_filename = "example.txt"
destination_filename = "copy.txt"
copy_file(source_filename, destination_filename)
print(f"The contents of '{source_filename}' have been copied to '{destination_filename}'.")