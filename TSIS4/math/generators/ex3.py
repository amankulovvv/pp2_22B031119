def div(num):
    i = 0
    while i <= num:
        if i % 3 == 0 and i % 4 == 0 and i != 0:
            yield i
        i += 1

N = int(input())
for i in div(N):
    print(i, end = " ")