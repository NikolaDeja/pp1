def prime(how_many):
    primes=[]
    count=0
    for i in range(100):
        if i==0 or i==1:
            continue
        if i==2:
            primes.append(2)
        if i%2==0:
            continue
        for j in range(3,how_many, 2):
            if i%j==0:
                continue
        primes.append(i)
        count+=1
        if count==how_many:
            return primes[how_many]

print(prime(5))

