from cmath import sqrt


a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

cir=a+b+c

half=cir/2

area=sqrt(half*(half-a)*(half-b)*(half-c))


print(f"Triangle area: {area}")
print(f"Triangle circumference: {cir}")