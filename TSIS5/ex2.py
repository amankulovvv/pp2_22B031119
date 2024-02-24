import re
condition = r'a[b]{2,3}'

string = input()

if re.match(condition, string):
    print(f"{string} follows condition.")
else:
    print(f"{string} does not follow condition.")