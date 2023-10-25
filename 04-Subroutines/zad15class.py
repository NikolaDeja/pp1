def phone_keyboard():
    count=1
    for i in range(1,10):
        if count<=2:
            print(i, end=" ")
            count+=1
        else:
            print(i, end=" ")
            print()
            count=1


phone_keyboard()