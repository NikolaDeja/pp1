def if_str(t):
    for i in t:
        if isinstance(i,str):
            return i
        
def if_30(t):
    for i in t:
        if type(i)==list:
            for j in i:
                if j==30:
                    return j 

t=("Seven", [10, 20, 30], (5, 15, 25)) 

print(if_str(t))
print(if_30(t))
