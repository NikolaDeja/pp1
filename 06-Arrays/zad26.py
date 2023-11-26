arr=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
max=0
for i in arr:
    if len(i)>=max:
        max_str=i
        max=len(i)

print(max_str)