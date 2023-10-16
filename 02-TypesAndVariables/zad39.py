price=float(input("Enter price: "))
discount=int(input("Enter discount %: "))

procent=discount/100

price_after=price*procent

print(f"Price with discount: {round(price-price_after,2)}")
print(f"Reduction: {round(price_after,2)}")
