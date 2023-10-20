from statistics import mean


n=[]
number=int(input("Enter number: "))
n.append(number)
while number!=0:
    number=int(input("Enter number: "))
    n.append(number)

sum=sum(n)
elements=len(n)-1
arth=sum/elements
print(f"RESULT: Quantity={elements}, Sum={sum}, Mean={arth}")