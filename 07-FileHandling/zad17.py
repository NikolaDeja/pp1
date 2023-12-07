file=open("Nowy dokument tekstowy.txt","r")
count=1
for line in file:
    print(line)
    if count==5:
        input()
        count=1
    count+=1

file.close()