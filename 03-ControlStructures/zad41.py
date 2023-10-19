pin="0805"
count=0
for i in range(3):
    guess=input("Enter the PIN code: ")
    if guess!=pin:
        print("Incorrect...")
        count+=1
        if count==3:
            print("Sorry, your payment card has been blocked.")
    else:
        break
    


