time24=input("Enter time (24-hour format): ")
#d_n is responisble for am and pm
if int(time24[0:2])>=12:
    time12=int(time24[0:2])-12
    d_n="pm"
    print(f"Time in 12-hour format: {time12}:{time24[3:5]}{d_n}")
else:
    d_n="am"
    print(f"Time in 12-hour format: {time24}{d_n}")

