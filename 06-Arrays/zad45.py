import math
import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(0,360):
    x = x + [n]

# create y values
for n in x:
    y = y + [math.sin(math.radians(n))]

# display chart
plt.plot(x, y)
plt.show()
