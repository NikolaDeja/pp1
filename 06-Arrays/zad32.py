def occurs(number, array) :
    for i in array:
        if number==i:
            return True
    return False

n=int(input("Number: "))
arr=[15, 38, 7, 23, 14]

print("Array: ", end="")
for i in arr:
    print(i, end=" ")
    
print()

if occurs(n, arr):
    print(f"Result: number {n} appears in the array")

