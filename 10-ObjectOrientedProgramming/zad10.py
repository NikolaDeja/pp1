class Song():
    
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year
    
    def __str__(self):
        return  "Performer: " + self.artist + "\n"+ "Song:" + self.track_title + "\n" +"Album:"+ self.album +"\n"+ "Year:" + str(self.year) + "\n"
    
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
print(song1)      

song2 = Song("Adele", "Hallo", "25", 2015)
print(song2)
