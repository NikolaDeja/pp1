arr1=[4,36,12,28,9,44,5] 
arr2=[5,1,36]
count=0
for i in arr1:
    for j in arr2:
        if i!=j:
            count+=1
    if count==3:
        print(i)
    count=0
