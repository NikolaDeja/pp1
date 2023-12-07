with open("text.txt", "a") as f:
    for i in range(1,50):
        f.write(str(i)+"\n")

f.close()