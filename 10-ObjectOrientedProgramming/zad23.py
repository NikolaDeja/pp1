class C():
    def __init__(self, name, surname, age, seniority):
        self.name=name
        self.surname=surname
        self.age=age
        self.sen=seniority

    def __str__(self):
        if self.age>18:
            return self.surname.upper()+self.name[0].upper()+str(self.sen)
        else:
            return self.surname.lower()+self.name[0].lower()+str(self.sen)


p1=C("Anna","May",17,7) 
p2=C("George","Brown",21,4) 

print(p1)
print(p2)

