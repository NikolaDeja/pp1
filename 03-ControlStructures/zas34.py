#a is an amaunt
a=int(input("Enter the amount in PLN: "))
#c is for counting
c5=0
c2=0
c1=0
while a!=0:
    if a-5>-1:
        a-=5
        c5+=1
    elif a-2>-1:
        a-=2
        c2+=1
    else:
        a-=1
        c1+=1

print(f"5 zl- {c5}")
print(f"2 zl- {c2}")
print(f"1 zl- {c1}")

