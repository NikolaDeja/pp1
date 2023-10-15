reg=input("Enter registration number: ")

if reg[0]=="K" and (reg[1]=="K" or reg[1]=="R"):
    print("Car from Krakow: True")
else:
    print("Car from Krakow: False")