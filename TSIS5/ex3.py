import re
condition = r'[a-z]+_[a-z]+'

string = input()

seq = re.findall(condition, string)

print(seq)