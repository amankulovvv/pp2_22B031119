import re
condition = r'a[b]*'

string = input()

if re.match(condition, string):
    print(f"{string} follows condition.")
else:
    print(f"{string} does not follow condition.")