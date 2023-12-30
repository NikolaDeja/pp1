class C():
    def __init__(self, sectors):
        self.sectors=sectors

    def m1(self,s,n):
        count=0
        for key in self.sectors:
            if key!=s:
                count+=0
            else:
                self.sectors[s]=n
        if count==len(self.sectors):
            self.sectors[s]=n
    def m2(self, s):
        sum=0
        for i in s:
            for key in self.sectors:
                if i==key:
                    sum+=self.sectors[key]
        print(sum)

    def display(self):
        print(self.sectors)

c=C({"A":120,"D":150,"G":90,"K":110})

c.m1("J",130)
c.display()
c.m2("GD")
c.m2("KEJ")

        

        