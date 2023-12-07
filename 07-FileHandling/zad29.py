import re


file=open("grades.txt","r")
f=file.readlines()

grades=re.findall("[\d+]\.[\d+]", f[1])

sum=0
for i in grades:
    sum+=float(i)

a=sum/len(grades)

print(a)

file.close()