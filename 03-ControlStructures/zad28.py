number=input("Enter EAN-13 article number: ")

if len(number)==13 and number[0:3]=="590":
    print("Article number is correct")
    print("Article manufactured in Poland")
elif len(number)==13:
    print("Article number is correct")
