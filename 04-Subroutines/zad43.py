def f(name):
    s=name[0]
    index=0
    for i in name:
        if i==" ":
            s+=name[index+1]
        index+=1
    return s

print(f("Internet of Things"))