def diffrent(a,b,c):
    if a!=b and b!=c and a!=c:
        return True
    else:
        return False
    

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))



if diffrent(a,b,c):
    print(f"Number {a} {b}, and {c} are different")
else:
    print(f"Number {a} {b}, and {c} are not different")

