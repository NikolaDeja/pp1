def f(n):
    n1=0
    n2=1
    fib=[0,1]
    for i in range(n):
        n3=n1+n2
        n1=n2
        n2=n3
        fib.append(n3)
    return fib[n-1]

print(f(9))