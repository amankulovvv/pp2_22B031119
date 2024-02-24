import re
cond = r'[a-z]+|[A-Z][a-z]*'
string = input("Enter your string: ")

newString = re.findall(cond, string)

print(f"Split string: {newString}")