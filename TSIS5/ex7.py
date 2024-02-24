import re
cond = r'_([a-z])'

snakeString = input("Enter your string: ")

camelString = re.sub(cond, lambda x: x.group(1).upper(), snakeString)

print(f"Camel case string: {camelString}")