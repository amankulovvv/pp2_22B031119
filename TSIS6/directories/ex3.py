import os

def test_path(path):
    if os.path.exists(path):
        print(f"{path} exists")
        dirname = os.path.dirname(path)
        print(f"Directory: {dirname}")
        filename = os.path.basename(path)
        print(f"Filename: {filename}")
    else:
        print(f"{path} does not exist")

path = "/path/to/file"
test_path(path)