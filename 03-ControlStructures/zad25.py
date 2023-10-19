number=int(input("Number of products purchased: "))
price=int(input("Product price: "))

if number>2:
    discount=price*0.25*(number-2)
    print(f"Amount to pay: {price*number-discount}")
else:
    print(f"Amount to pay: {price*number}")