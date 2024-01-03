points=[(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

for i in points:
    mini=min(i)
    maxi=max(i)
    suma=sum(i)-mini-maxi
    print(suma)

#suma= lambda x: sum(x)

#print(list(map(suma, exclude)))