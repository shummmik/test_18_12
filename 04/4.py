def getP(s):
    return (7-s)/6

def factorial(n):
    res = 1
    i = 0
    while i < n:
        i += 1
        res = i * factorial(n-1)
    return res

def getP_Bernuli(n,m,s):
    p = getP(s)
    return factorial(n)/(factorial(m)*factorial(n-m))* p**m * (1-p)**(n-m)

print(getP_Bernuli(4,4,3))
