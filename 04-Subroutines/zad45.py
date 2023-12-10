def f(expression):
    exp=str(expression)
    p=0
    w=0
    if exp[1]=="+":
        p+=int(exp[0])+int(exp[2])
    elif exp[1]=="-":
        p+=int(exp[0])-int(exp[2])

    for i in range(3,len(exp)):
        if exp[i]=="+":
            w=p+int(exp[i+1])
            p=w
        elif exp[i]=="-":
            w=p-int(exp[i+1])
            p=w
    return w

print(f("3+8+1+2"))