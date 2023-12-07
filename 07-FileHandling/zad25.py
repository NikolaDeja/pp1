import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)

sum=0
for i in temperatures:
        sum+=int(i)

avrage=sum/3

print(avrage)