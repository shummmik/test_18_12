import time

N=7
M=23


def defEnd(n):
    i = 1
    res = 0
    while i <= n:
        res += 10**(n-i)*9
        i += 1
    return res





def countM(n,m):
    start = 10**(n-1)
    listN = list()
    end = defEnd(n)
    if start < m:
        start = m
    ost = start%m

    while ost != 0:
        start += 1
        ost = start%m
    
    while start <= end:
        listN.append(start)
        start += m
    return len(listN)

def countM1(n,m):
    start = 10**(n-1)
    countN = 0
    end = defEnd(n)
    if start < m:
        start = m
    ost = start%m

    while ost != 0:
        start += 1
        ost = start%m
    
    while start <= end:
        countN += 1
        start += m
    
    return countN

def countM2(n,m):
    start = 10**(n-1)
    end = defEnd(n)
    return round((end-start)/m)


t1 = time.time()
li = countM(N,M)
t2 = time.time()

print(t2-t1)
print(li)

t1 = time.time()
li1 = countM1(N,M)
t2 = time.time()

print(t2-t1)
print(li1)

t1 = time.time()
li2 = countM2(N,M)
t2 = time.time()

print(t2-t1)
print(li2)