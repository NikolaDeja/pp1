def f(amount_to_pay):
    coins=0
    while amount_to_pay!=0:
        if amount_to_pay-5>=0:
            coins+=1
            amount_to_pay-=5
        elif amount_to_pay-2>=0:
            coins+=1
            amount_to_pay-=2
        else:
            coins+=amount_to_pay
            amount_to_pay=0
    return coins

n=int(input())

if __name__=="__main__":
    print(f(n))