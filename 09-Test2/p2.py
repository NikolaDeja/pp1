def f(arr):
    l1=arr[0]
    l2=0
    s1=0
    s2=0
    for i in arr:
        if l1==i:
            s1+=1
        else:
            l2=i
            s2+=1
    if s1==1:
        return l1
    else:
        return l2
    
if __name__=="__main__":
    print(f([7,7,7,5,7,7]))
    print(f([2,3,2,2]))
    

