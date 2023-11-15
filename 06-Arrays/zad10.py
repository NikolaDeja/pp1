arr=[1,2,3,4,5]

for i in arr:
    print(i, end=" ")
print()


arr[0]-=1

for i in arr:
    print(i, end=" ")
print()

arr[-1]+=4

for i in arr:
    print(i, end=" ")
print()

arr[len(arr)//2]*=2

for i in arr:
    print(i, end=" ")
print()


