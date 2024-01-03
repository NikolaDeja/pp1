arr=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]

names= lambda x: x[0].upper()+","+x[1]

#print(list(map(names, arr)))


for i in list(map(names, arr)):
    print(i)

