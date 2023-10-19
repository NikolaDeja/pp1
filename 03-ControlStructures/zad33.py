#d is a number in decimal system
#b in a number in binary system
#r is only to to write the result
#r is for reminder
d=int(input("Enter decimal number: "))
r=d
b=""

while d!=0:
    if d%2==0:
        b="0"+b
    else:
        b="1"+b
    d//=2

print(f"{r}(10) = {b}(2)")