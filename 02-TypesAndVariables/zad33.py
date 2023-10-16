#p is password
p=input("Enter password: ")
# v "if valid"
v=True;
if len(p)>=8:
    v=True
else:
    v=False

print(f"Password is valid: {v}")