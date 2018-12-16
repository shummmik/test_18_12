

nodes1 = ["1", "2", "3", "4", "5"]
nodes = ["a", "b", "c", "d", "e", "f"]

ribs1 = [("1", "2", 10),  ("1", "4", 30),  ("1", "5", 100), ("2", "3", 50),
               ("3", "5", 10), ("3", "4", 20), ("4", "5", 60)]

ribs = [("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)]
def minV(l):

    min = l[0]
    for i in l:
        if min > i:
            min = i
    return min

def minNode(node1, node2):
    if node1[0] < node2[0]:
        return node1
    else:
        return node2



def minD(l):
    li = list(i[0] for i in l.values() if i[1] == False)
    m = minV( li )
    for i in l.keys():
        if l[i][0] == m:
            return i

def reGraf(grafNodes,rib,i,start):
    listN = grafNodes[start][2].copy()
    listN.append(start)
    grafNodes[rib[i]] = minNode(grafNodes[rib[i]], 
                                          [rib[2]+grafNodes[start][0],grafNodes[rib[i]][1],listN])


def deis(nodes, ribs, start, end):
    grafNodes = {i: [float('inf'), False,[]] for i in nodes}
    grafNodes[start][0] = 0   #way
    while start != end: 
        grafNodes[start][1] = True
        for rib in ribs:
            if rib[0] == start :
                reGraf(grafNodes,rib,1,start)
            if rib[1] == start:
                reGraf(grafNodes,rib,0,start)
        start = minD(grafNodes)
    way = grafNodes[end][2].copy()
    way.append(end)
    return [way,grafNodes[end][0]]


print(deis(nodes, ribs,'a','f'))

print(deis(nodes1, ribs1,'1','5'))
