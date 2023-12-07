def f1(s):
    count=0
    for i in s:
        if i==" ":
            count+=1
    return count+1

def f2(s):
    arr=[]
    for i in s:
        arr=s.split(" ")
    arr.sort(key=len, reverse=True)
    return arr
    
def f3(s1):
    arr1=[]
    for i in s1:
        arr1=s1.split(" ")
    arr1.sort()
    return arr1
    
s="An apple a day keeps the doctor away"

if __name__=="__main__":
    print(f1(s))
    print(f3(s))
    print(f2(s))