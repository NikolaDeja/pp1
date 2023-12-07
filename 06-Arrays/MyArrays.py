def f1(arr):
    arr.sort()
    return arr[-2]

def f2(arr):
    arr.sort()
    return arr[-1]-arr[0]

def f3(arr):
    arr.sort()
    if len(arr)%2!=0:
        return arr[len(arr)//2]
    if len(arr)%2==0:
        w=arr[len(arr)//2-1]+arr[(len(arr)//2)]
        return w/2
    
def f4(arr):
    arr1=[]
    arr.sort()
    arr1.append(arr[0])
    arr1.append(arr[-1])
    return arr1

def f5(arr):
    s=""
    for i in arr:
        s+=str(i)+"-"
    return s

    

arr=[3,9,7,8,1,2]

if __name__=="__main__":
    print(f1(arr))
    print(f2(arr))
    print(f3(arr))
    print(f4(arr))
    print(f5(arr))
    
        