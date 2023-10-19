washing_product = "shoes"
rinse = True
spin = False
time=0
if washing_product=="shoes":
    time=20
elif washing_product=="underwear":
    time=70
elif washing_product=="jacket":
    time=40

if rinse and spin:
    time+=24
elif rinse:
    time+=15
elif spin:
    time+=9

print(f"Total washing time: {time} minutes")

