#c is a current price
c=140.00
#p is a previous price
p=200.00

procent=((p-c)/p)*100

if procent>=10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(procent)}%")