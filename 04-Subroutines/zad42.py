def f(number1,number2,number3):
    max=0
    min=0
    if number1<number2:
        min=number1
    elif min<number2:
        min=number2
    else:
        min=number3

    print(min)
    
    if number1>number2:
        max=number1
    elif max<number2:
        max=number2
    elif max<number3:
        max=number3
    print(max)
    
    return max-min

print(f(2,8,12))