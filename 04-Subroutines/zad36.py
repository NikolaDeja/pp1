def f(detector):
    plus=0
    for i in detector:
        if i=="+":
            plus+=1
            if plus==3:
                return True
        else:
            plus-=1
    return False

print(f("+-++-++-+---"))