import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return

    if not os.access(file_path, os.W_OK):
        print(f"Error: You do not have write access to {file_path}.")
        return

    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    except Exception as e:
        print(f"Error: {e}")

file_path = "example.txt"
delete_file(file_path)