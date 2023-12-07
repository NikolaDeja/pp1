s=input("File name: ")

file=open(s,"r")

count=0
for line in file:
    count+=1
    
print(count)

print(f"Number of lines: {count}")

file.close()