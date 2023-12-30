class Contact_list():
    def __init__(self):
        self.arr=[]
    
    def add(self, contact):
        self.arr.append(contact)

    def display(self):
        for i in self.arr:
            print(i)