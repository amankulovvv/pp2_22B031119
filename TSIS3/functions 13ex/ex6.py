text = input().split()
def reverse_words(words):
    revWords = words[::-1]
    for i in revWords:
        print(i, end =" ")
reverse_words(text)