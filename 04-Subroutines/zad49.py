def f(dice):
    count=0
    max=0
    max_count=0
    for i in range(1,len(dice)):
        current_number=dice[i-1]
        next_number=dice[i]
        if current_number==next_number:
            count+=1
            if count>max_count:
                max=dice[i]
                max_count=count
        else:
            count=0
    return max

print(f("23133"))
        