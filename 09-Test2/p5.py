def f(first_letter,last_letter):
    count=0
    with open("data.txt", "r",encoding="utf-8") as f:
        text=f.read()
        first=text[0]
        for i in text:
            if i==" " and first==first_letter and i-1==last_letter:
                count+=1
                first=i+1
    return count

if __name__=="__main__":
    print(f("w","d"))