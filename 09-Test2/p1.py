def f(player1,player2):
    s1=0
    s2=0
    for i in player1:
        if i=="A" or i=="K" or i=="Q" or i=="J" or i=="T":
            s1+=10
        else:
            s1+=int(i)
    for i in player2:
        if i=="A" or i=="K" or i=="Q" or i=="J" or i=="T":
            s2+=10
        else:
            s2+=int(i)
    if s1>=s2:
        return True
    else:
        return False
    
if __name__=="__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8") )
    
