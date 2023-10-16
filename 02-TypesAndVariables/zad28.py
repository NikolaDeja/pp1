h=int(input("Enter your height: "))
w=int(input("Enter your weight: "))

cm=h/100

bmi= w/(cm**2)

correct= True

if bmi< 18.5:
    correct=False
elif 18.5<= bmi <= 30:
    correct =True
else:
    correct =False

print(f"Your BMI index: {bmi}")
print(f"Correct weight: {correct}")




