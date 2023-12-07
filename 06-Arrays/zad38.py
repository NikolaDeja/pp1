def if_greater(arr,n):
    count=0
    for i in arr:
        if i>n:
            count+=1
    return count

arr=[2.4, 11.6, 43.5, 65.3, 23.7]
n=float(input("Number: "))

print(if_greater(arr,n))