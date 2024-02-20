def fun(num):
    i =1
    while i <= num:
        yield i**2
        i +=1

N = int(input())
for i in fun(N):
    print(i, end = " ")