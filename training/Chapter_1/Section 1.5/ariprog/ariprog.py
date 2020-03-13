"""
 ID: actuato2
 LANG: PYTHON3
 TASK: ariprog
"""
def getAllPossibilities(M):
    ret = set()
    for p in range(M+1):
        for q in range(M+1):
            ret.add(p**2+q**2)
    
    return ret

def checkForAriprogs(Combos, N, M):
    ret = []
    for a in Combos:
        for b in range(1, int((M**2*2-a)/(N-1))+1):
            for n in range(N):
                if a+(b*n) in Combos:
                    pass
                else:
                    break
                if n == N-1:
                    ret.append([a, b])
    return ret

#Main Program
with open('ariprog.in') as fIn:
    lines = fIn.readlines()
    N = int([r.strip() for r in lines][0])
    M = int([r.strip() for r in lines][1])

    Possibilities = list(set(getAllPossibilities(M)))
    ans = checkForAriprogs(Possibilities, N, M)
    if ans == []:
        with open('ariprog.out', 'w') as fOut:
            fOut.write('NONE' + '\n')
    else:
        ans.sort(key = lambda p: p[1])
        with open('ariprog.out', 'w') as fOut:
            for a in ans:
                fOut.write(str(a[0]) + ' ' + str(a[1]) + '\n')
    