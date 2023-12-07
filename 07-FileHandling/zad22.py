import random


with open("text2.txt", "a") as f:
    for i in range(1,50):
        f.write(str(random.randint(100,999))+"\n")

f.close()