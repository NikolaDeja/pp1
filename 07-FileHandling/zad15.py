with open("filename.txt") as f:
    line=f.readline()
    while line!="":
        print(line, end="")
        line=f.readline()
    f.close()

