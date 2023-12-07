def count(t,n):
    c=0
    for i in t:
        if i==n:
            c+=1
    return c

t=(50,20,40,50,30,50)

n=int(input("Number: "))
print(count(t,n))