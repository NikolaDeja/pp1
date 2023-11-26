def compere(arr1, arr2):
    if len(arr1)!=len(arr2):
        return False
    i=0
    while i<len(arr1):
        if arr1[i]!=arr2[i]:
            return False 
        i+=1
    return True

arr1=[5,3,1]   
arr2=[6,3,2]

if compere(arr1,arr2):
    print("tak")
else:
    print("nie")
