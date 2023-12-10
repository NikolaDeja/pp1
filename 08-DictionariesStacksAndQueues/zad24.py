import stack

n=18

while n!=0:
    stack.push(n%2)
    n//=2

stack.display()