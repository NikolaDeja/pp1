arr=[-15, 8, -31, 47, -2, 19]
min=100
max=0
for i in arr:
    if min>i:
        min=i
    if max<i:
        max=i

print(min, max)