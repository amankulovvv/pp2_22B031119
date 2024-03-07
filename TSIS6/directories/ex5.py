def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

filename = "example.txt"
data = ["Hello", "World", "It's"]
write_list_to_file(filename, data)
print(f"The list {data} has been written to the file '{filename}'.")