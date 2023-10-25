
def numbers(n):
    s=""
    for i in range(1,n+1):
        s=s+str(i)+" "
    return s

n1=15
n2=7
print(f"Numbers <1,15>: {numbers(n1)}")
print(f"Numbers <1,7>: {numbers(n2)}")