with open("text3.txt", "a") as f:
    for i in range(1,11):
        f.write(str(i)+","+str(i**2)+","+str(i**3)+"\n")

f.close()
