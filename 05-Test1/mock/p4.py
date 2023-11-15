def f(cn):
    w=""
    for i in range(len(cn)):
        if(1<i<12):
            w+="*"
        else:
            w+=cn[i]
    return w

