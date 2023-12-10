import json

def f(years, course):
    av=0
    students=0
    with open("data.json", "r") as file:
        f=json.load(file)
        for dict in f:
            if dict["age"]<years:
                continue
            for i in dict["studies"]["courses"]:
                if i["name"]==course:
                    av=sum(i["grades"])/len(i["grades"])
                    if av>=4:
                        students+=1
    return students

if __name__=="__main__":
    print(f(21, "statistics"))