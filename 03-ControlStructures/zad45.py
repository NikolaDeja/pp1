def prime(a):
    if a==2 or a==3:
        return True
    
    if a%2==0 or a<2:
        return False
    
    for i in range(3,a):
        if a%i==0:
            return False
        i+=2

    return True

n=int(input("Enter number: "))
count=0
number=2

while count!=n:
    if prime(number):
        print(number)
        count+=1
    number+=1