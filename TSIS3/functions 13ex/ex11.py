word = input()
def is_palindrome(word):
    if word == word[::-1]:
        print("Yes, it is!")
    else:
        print("No, it's not!")
is_palindrome(word)