file1=open("MeatAndFish.txt", "r")
file2=open("GrainsAndBread.txt","r")


all=open("allproducts.txt","a")

for line in file1:
    all.write(line)

for i in file2:
    all.write(i)

file1.close()
file2.close()
all.close()



