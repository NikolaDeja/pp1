class TV():
    def __init__(self,is_on):
        self.is_on = is_on
    def turn_on(self):
        self.is_on= True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            return print("TV is on")
        else:
            return print("TV is off")

tv=TV(False)

tv.show_status()
tv.turn_on()
tv.show_status()
tv.turn_off()
tv.show_status()