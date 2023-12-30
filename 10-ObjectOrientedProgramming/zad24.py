class C():
    def __init__(self, arr2d):
        self.arr=arr2d

    def m(self, n):
        sum=0
        for i in self.arr:
            countj=0
            for j in i:
                if j>0:
                    countj+=1
            if countj==2:
                sum+=1
        if sum>=n:
            return True
        else:
            return False
        
c=C([[2,3],[1,8],[-6,4],[3,-7]])

if c.m(2):
    print("True")
else:
    print("Flase")

if c.m(3):
    print("True")
else:
    print("Flase")
        