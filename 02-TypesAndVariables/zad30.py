import random


a = random.randint(1,6)

b=True

if a==1 or a==6:
    b=True
else:
    b=False

print(f"Dice rolled: {a}")
print(f"Special number: {b}")