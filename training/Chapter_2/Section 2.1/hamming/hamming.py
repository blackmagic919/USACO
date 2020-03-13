"""
 ID: actuato2
 LANG: PYTHON3
 TASK: hamming
"""

def generateBinaryList(binaryLen):
    base = [0 for _ in range(binaryLen)]
    ret = [base]
    while True:
        new = []

        n = 0
        while True:
            if n == binaryLen:
                new.append(1)
                break
            if ret[-1][n] == 0:
                new.append(1)
                new.extend(ret[-1][n+1::])
                break
            else:
                new.append(0)
            n+=1
        if len(new) > binaryLen:
            break
        else:
            ret.append(new)
    ret = [sum([l[n]*10**n for n in range(len(l))]) for l in ret]
    return ret

def getHammingDistance(gn, ln):
    dist = 0
    gn = str(gn)
    ln = ''.join(['0' for _ in range(len(str(gn))-len(str(ln)))]) + str(ln)
    for n in range(len(gn)-1, -1, -1):
        if ln[n] != gn[n]:
            dist += 1
    return dist

def checkHammingDistance(l, developed, hd, length):
    for n in l:
        for d in developed:
            if not(getHammingDistance(n, d) >= hd):
                break
        else:
            developed.append(n)
        if len(developed) >= length:
            return developed

def convertToBase10(binaryList):
    ret = []
    for b in binaryList:
        ret.append(int(str(b), 2))
    return ret

with open('hamming.in') as fIn:
    lines = fIn.readlines()
    N,B,D = lines[0].strip().split()

binaryList = generateBinaryList(int(B))
sol = convertToBase10(checkHammingDistance(binaryList, [0], int(D), int(N)))

with open('hamming.out', 'w') as fOut:
    n = len(sol)
    while True:
        for i in range(10):
            if i != 0:
                fOut.write(' ')
            fOut.write(str(sol[len(sol) - n]))
            n -= 1
            if n < 1:
                break
        fOut.write('\n')
        if n < 1:
            break