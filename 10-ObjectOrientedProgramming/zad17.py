class TV():
    def __init__(self, volume):
        self.vol=volume
    def up(self):
        if self.vol<10:
            self.vol+=1
    def down(self):
        if self.vol>0:
            self.vol-=1
    def show(self):
        print(self.vol)

tv=TV(0)

tv.show()
tv.up()
tv.show()
tv.up()
tv.show()
tv.down()
tv.show()
tv.down()
tv.down()
tv.down()
tv.show()