import stack

e="(2+3)*(4+5)="

operators=["+","-","*","/"]

w=""
for i in e:
    if i not in operators and i!="(" and i!=")":
       w+=i 
    elif i in operators:
        stack.push(i)
    elif i==")":
        w+=stack.returning()
        stack.pop()
    elif i=="=":
        w+=stack.returning()+"="
    
print(w)


