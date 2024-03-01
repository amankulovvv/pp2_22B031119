def is_palindrome(string):
    return string == string[::-1]

string = input()
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")