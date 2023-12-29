from numpy import sort


class Statistics():
    def __init__(self, array):
        self.arr=array
    def add(self):
        self.arr.append(int(input("Enter number: ")))
    def display(self):
        for i in self.arr:
            print(f"{i},", end="")
        print()
    def gratest(self):
        max=self.arr[0]
        for i in self.arr:
            if i>max:
                max=i
        print(max)
    def smallest(self):
        min=self.arr[0]
        for i in self.arr:
            if i<min:
                min=i
        print(min)
    def mean(self):
        sum=0
        for i in self.arr:
            sum+=i
        print(sum/len(self.arr))
    def median(self):
        sort(self.arr)
        if len(self.arr)%2==0:
            print((self.arr[len(self.arr)//2]+self.arr[(len(self.arr)//2)+1])/2)
        else:
            print(self.arr[len(self.arr)//2])

a=Statistics([12, 37, 6, 9, 17])
a.add()
a.display()
a.gratest()
a.smallest()
a.mean()
a.median()
