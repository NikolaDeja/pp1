arr=[2, 3, 2, 5, 8, 1, 9, 8]
alone=[]
for i in range(len(arr)):
        if arr[i] not in arr[:i] and arr[i] not in arr[i+1:]:
            alone.append(arr[i])

for i in alone:
    print(i)