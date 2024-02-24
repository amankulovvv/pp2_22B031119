import re
condition = r'[A-Z][a-z]+'

string = input()

seq = re.findall(condition, string)

print(seq)