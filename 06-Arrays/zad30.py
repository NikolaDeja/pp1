def bubblesort(array):
    for i in array:
        for j in range(0,len(arr)-1-i):
            if j>j+1:
                i, j = j, i
    return array

arr={5,4,6,7,3}

bubblesort(arr)

for i in arr:
    print(i)
                