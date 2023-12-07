def e_or_o(arr):
    even=[]
    odd=[]
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even+odd

arr=[2,9,7,8,3,4,6]

print(e_or_o(arr))