def f(number, even):
    sum=0
    
    for i in str(number):
        if even:
            if int(i)%2==0:
                sum+=int(i)
        else:
            if int(i)%2!=0:
                sum+=int(i)
    return sum

n=1234
even=False

print(f(n,even))