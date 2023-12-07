def subset(arr1,arr2):
    count=0
    for i in arr1:
        for j in arr2:
            if i==j:
                count+=1
    if count==len(arr2):
        return True
    else:
        return False


arr1=[2,3,5,7,8,9,10]
arr2=[3,7,9,5]

if subset(arr1,arr2):
    print("Yas")
else:
    print("No")
