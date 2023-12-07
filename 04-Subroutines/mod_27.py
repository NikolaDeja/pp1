def f(card_number):
    s=""
    index=0
    for i in card_number:
        if index<=1 or index>=12:
            s+=i
        else:
            s+="*"
        index+=1
    return s