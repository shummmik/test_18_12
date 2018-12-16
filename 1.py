l = [[-20,0.3],[-10,0.1],[0,0.2],[10,0.1],[20,0.3],]



def expected(inList):
    res = 0
    for i in inList:
        res += i[0]*i[1]
    return res


def dispersion(inList):
    res = 0
    ex = expected(inList)
    for i in inList:
        res += (i[0]-ex)**2*i[1]
    return res


print(expected(l))
print(dispersion(l))