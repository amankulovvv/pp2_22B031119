import re
cond = r'(?<!^)(?=[A-Z])'

camelString = input("Enter your string: ")

snakeString = re.sub(cond, '_', camelString).lower()

print(f"Snake case string: {snakeString}")