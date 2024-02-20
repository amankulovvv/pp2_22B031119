def fun(num):
    i = num
    while i >= 0:
        yield i
        i -= 1

N = int(input())
for i in fun(N):
    print(i, end = " ")