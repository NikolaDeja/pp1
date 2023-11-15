def f(n, even):
    n=str(n)
    s=0
    if even:
        for i in n:
            if int(i)%2==0:
                s+=int(i)
    else:
        for i in n:
            if int(i)%2!=0:
                s+=int(i)
    return s


