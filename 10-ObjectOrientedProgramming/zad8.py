class Telephone():
    def __init__(self,brand,color,memory):
        self.brand = brand
        self.color = color
        self.memory = memory
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def clean_memory(self,cleand_memory):
        self.current_memory = cleand_memory

phone = Telephone(
        "Samsung",
        "Cream",256)

print(phone.brand,end="")
print(phone.color ,end="")
print(phone.memory)

phone.open()
phone.clean_memory(20)



