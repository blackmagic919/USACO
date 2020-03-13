import sys
import time


sys.setrecursionlimit(50000)




def groupBarns(roads, groups, parent, index, milk, first):
    if groups[parent] != 0:
        return
    groups[parent] = index     
    for child in roads[parent]:
        if milk[parent] == milk[child] and groups[child] == 0:
            groupBarns(roads, groups, child, index, milk, False)
    if first == True:
        for g in range(parent-1, len(groups)):
            if groups[g] == 0:
                groupBarns(roads, groups, g, index+1, milk, True)
                break
    

with open('milkvisits.in') as fIn:
    lines = fIn.readlines()
    N, M = lines[0].strip().split()
    N = int(N)
    M = int(M)

connected = [[] for _ in range(N)]
MilkType = lines[1].strip()

used = []
for i in range(N-1):
    num1 =int(lines[i+2].strip().split()[0])-1
    num2 =int(lines[i+2].strip().split()[1])-1
    connected[num1].append(num2)
    connected[num2].append(num1)



req = []
for p in range(M):
    req.append([d for d in lines[p+N+1].strip().split()])

ret = [0 for _ in range(N)]
groupBarns(connected, ret, 0, 1, MilkType, True)
sol = ''


for p in req:
    if ret[int(p[0])-1] == ret[int(p[1])-1] and p[2] == MilkType[int(p[0])-1]:
        sol += '1'
    elif ret[int(p[0])-1] != ret[int(p[1])-1]:
        sol += '1'
    else:
        sol += '0'

with open('milkvisits.out', 'w') as fOut:
    fOut.write(sol)
    fOut.write('\n')


