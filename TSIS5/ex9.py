import re
cond = r'(?<=.)([A-Z])'

string = input("Enter your string: ")

newString = re.sub(cond, r' \1', string)

print(f"Your new string: {newString}")