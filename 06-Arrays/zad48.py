def create_2d_arr(x,y):
    arr=[]
    for i in range(y-1):
            arr.append([0]*x)
    return arr


print(create_2d_arr(3,5))