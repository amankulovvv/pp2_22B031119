import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is the file for the letter '{letter}'.\n")

generate_files()
print("26 files have been created.")