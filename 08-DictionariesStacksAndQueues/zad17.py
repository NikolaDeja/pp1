ICAO={
"A":    "Alfa",
"B":    "Bravo",
"C":    "Charlie",	
"D":    "Delta",
"E":    "Echo",	
"F":    "Foxtrot",
"G":	"Golf",	
"H":	"Hotel",	
"I":	"India",	
"J":	"Juliett", 
"K":	"Kilo",
"L":	"Lima",	
"M":	"Mike",	
"N":	"November",
"O":	"Oscar",	
"P":	"Papa",	
"Q":	"Quebec",	
"R":	"Romeo",	
"S":	"Sierra",	
"T":	"Tango",	
"U":	"Uniform",	
"V":	"Victor",	
"W":    "Whiskey",	
"X":	"Xray",
"Y":	"Yankee",
"Z":	"Zulu",
}

s=input("Enter text:").upper()
w=[]
for i in range(len(s)):
    if s[i] in ICAO.keys():
        w.append(ICAO[s[i]])

print(w)
