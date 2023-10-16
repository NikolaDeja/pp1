c=int(input("Enter tree circumference: "))
czy_prawda=True

d=(c/3.14)

if d>=50:
    czy_prawda=True
else:
    czy_prawda=False

print(f"Tree can be cut down: {czy_prawda}")