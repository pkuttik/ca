def fib(n,t1,t2):
    if n == 0:
        return t1
    elif n == 1:
        return t2**2
    print(n-2,n-1,n)
    return fib(n-2,t1,t2) + fib((n-1),t1,t2)**2
t1,t2,n= list(map(int, input().strip().split()))
# print (t1,t2,n)
print(fib(n-1,t1,t2))
#1 2 3 4 5
#0 1 1 2 5