import re
cond = r'[ ,.]'

string = input("Enter your string: ")

newString = re.sub(cond, ':', string)

print(f"New string: {newString}")