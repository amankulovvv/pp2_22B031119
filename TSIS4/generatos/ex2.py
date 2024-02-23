def even(num):
    i = 0
    while i <= num:
        if i % 2==0:
           yield i
        i +=1
        
N = int(input())
for i in even(N):
    print(i, end = " ")