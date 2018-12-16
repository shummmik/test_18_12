def lenV1(v):
    return sum(list(map(lambda x: x**2,v)))**.5


def lenV(v):
    res = 0
    for i in list(x**2 for x in v):
        res += i
    return res**0.5    

print(lenV1([1,2,3]))
print(lenV([1,2,3]))
