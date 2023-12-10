def f(number):
    number=str(number)
    n=[]
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i]==number[j]:
                n.append(number[i])
                break
        number.replace(number[i],"")
    for i in n:
        if i in n:
            n.append(i)
    return n
            

    
        
print(f(513553007))