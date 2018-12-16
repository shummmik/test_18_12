a = [1,2,3]
b = [4,5,6]

def scalyar1(a,b):
    return sum(list(map(lambda x,y: x*y,a,b)))

def scalyar(a,b):
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    return res

print(scalyar(a,b))
print(scalyar1(a,b))
