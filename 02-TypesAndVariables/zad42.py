b=int(input("Enter binary number: "))
d=0
power=0

while b!=0:
    cyfra=b%10
    if cyfra!=0:
        d+=2**power
    b//=10
    power+=1
    

print(f"Binary number in decimal notation: {d}")
  
    

