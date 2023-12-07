def formatted(arr):
    print("-"*41)
    print("|", end="")
    for i in arr:
        if i<10:
            print(" "*3+str(i)+"|", end="")
        elif 10<=i<=99:
            print(" "*2+str(i)+"|", end="")
        else:
            print(" "+str(i)+"|", end="")
    print()
    print("-"*41)

arr=[1,23,5,382,1,17,4,906]

formatted(arr)