import random

#computer rolls the dice
a = random.randint(1,6)
#user guesses the number
g=int(input("Guess the number: "))

if a==g:
    print("True")
else:
    print("False")