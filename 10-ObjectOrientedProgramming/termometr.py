import random
class Termometr():
    def __init__(self):
        pass

    def turn_on(self):
        self.is_on=True

    def turn_off(self):
        self.is_on=False

    def measure(self):
        self.temp=round(random.uniform(34.0,42.0),1)
        
    def show(self):
        print(self.temp, end="")
        if 37.0<=self.temp<41.0:
            print(" (fever)")
        elif self.temp>=41.0:
            print(" CRITICAL TEMPERATURE!!")


    