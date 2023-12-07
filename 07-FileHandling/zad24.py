file=open("studentslist.csv","r")


data=file.readlines()

for line in data[1:]:
    data=line.split(",")
    if int(data[2])<int(30):
        print(f"{data[0]}, {data[1]}, {data[4]}")