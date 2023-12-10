import re

def f(arr):
    count=0
    low=0
    number=0
    under=0
    for i in arr:
        for j in i:
            if re.search("[a-z]",j):
                low+=1
            if re.search("\d",j):
                number+=1
            if re.search("_",j):
                under+=1
        if low>0 and number>0 and under>0:
            count+=1
        low=0
        number=0
        under=0
    return count

if __name__=="__main__":
    print(f(["uek","water_7_x","anna.may_6","a_b_c_d_e_f"]))
    print(f(["Hej_12", "HASLO"]))