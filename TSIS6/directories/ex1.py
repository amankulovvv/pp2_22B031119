import os

def list_directories(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(f"Directories in {dirpath}:")
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
        print(f"Files in {dirpath}:")
        for filename in filenames:
            print(os.path.join(dirpath, filename))

def list_only_directories(path):
    for dirpath, dirnames, _ in os.walk(path):
        print(f"Directories in {dirpath}:")
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))

def list_only_files(path):
    for dirpath, _, filenames in os.walk(path):
        print(f"Files in {dirpath}:")
        for filename in filenames:
            print(os.path.join(dirpath, filename))

path = "/path/to/directory"
list_directories(path)
list_only_directories(path)
list_only_files(path)