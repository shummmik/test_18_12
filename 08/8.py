def getM(n):
    res = 0
    for i in range(1,n+1):
        res += len(str(i))
    return res


def getN(m):
    
    if m < 10:
        return m
    m -= 9
    n = 9
    i = 1
            
    while m > 0:
        rang = 9*10**i

        if m <= rang*(i+1):
            
            n += int(m/(i+1))
            m = 0
        else:
            n += rang
            m -= rang*(i+1)
        i += 1
            
    return n
print(getN(555565)) #525
print(getM(111111))
