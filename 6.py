

def func(x):
    return x**4-x**3-2*x**2+3*x-3

def half(a,b,e):
    fA = func(a)
    fB = func(b)
    while fA*fB < 0 and b-a > e:
        c = (a+b)/2
        fC = func(c)
        if fA * fC < 0:
            b = c
        else:
            a = c 
    return [a,b,(a+b)/2]

print(half(1,2,0.0001))