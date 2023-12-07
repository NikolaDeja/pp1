import re


file=open("allproducts.txt","r")
f=file.read()
file.close

words=re.findall("\w{6}\w",f)

print(words)