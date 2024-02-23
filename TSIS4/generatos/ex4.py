def sqr(a,b):
    for i in range(a, b+1):
        yield i ** 2
        
x = int(input())
y = int(input())
for i in sqr(x, y):
    print(i, end = " ")