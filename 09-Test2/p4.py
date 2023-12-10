def f(subjects):
    sub=""
    av=0
    count=0
    average=0
    for key,values in subjects.items():
        for i in values:
            av+=i
            count+=1
        if average<(av/count):
            average=av/count
            sub=key
    return sub

if __name__=="__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
