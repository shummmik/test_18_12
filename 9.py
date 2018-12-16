m = [[2,2,6,3],[4,5,6,3],[7,8,9,3],[5,2,3,5]]
n = [[1,2],[3,4]]

def getMatrix(m,n,j):
    r = 1 # row
     # column
    l = 1

    c1 = 0

    mOut = []
    while l < n:
        mOut.append(list())
        l += 1
    
    while r < n:
        c = 0
        while c < n:
            if c == j:
                c += 1
                continue
            mOut[r-1].append(m[r][c]) 
            c += 1
            c1 += 1
        r += 1
    #print(mOut)
    return mOut


def determinantM(m):
    n = len(m)
    res = 0
    j = 0  #columns

    if n == 1:
        return m[0][0]
    
    while j < n:
        res += (-1)**(j+2)*m[0][j]*determinantM(getMatrix(m,n,j))
        j += 1
    #print(res)
    return res

print(determinantM(n))
print(getMatrix(n,2,0))