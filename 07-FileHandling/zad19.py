file=open("sample3.txt","r")


copy=open("copylines.txt","a")

for line in file:
    copy.write(line)

file.close()
copy.close()