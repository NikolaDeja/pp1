temp={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
t=temp.items()

plus= list(filter(lambda x:x[1]>0, t))
for i in plus:
    print(i[0])