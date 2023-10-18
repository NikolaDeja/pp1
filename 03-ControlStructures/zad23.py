age=int(input("Enter the dog's age in human years: "))


if age>2:
    h_age=10.5+((age-2)*4)
else:
    h_age=10.5

print(f"The dog's age in dog’s years is {h_age} years.")
