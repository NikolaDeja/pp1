def f(binary_number):
    for i in binary_number:
        if i!="1" and i!="0":
            return False
    return True
 
n="1101010101"
if f(n):
    print("Binary")
else:
    print("Not Binary")