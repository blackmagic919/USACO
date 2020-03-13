import math

def simulateBumps(time, cows):
    time *= 2
    bumps = 0

    cowQue = []
    for c in cows:
        if c[2] == 1:
            cowQue.append(c[1])
        else:
            queAdd = None
            Citer = 0
            while queAdd == None and Citer < len(cowQue):
                if c[1] - cowQue[Citer] <= time:
                    queAdd = Citer
                    break
                Citer += 1
            if queAdd != None:
                bumps += len(cowQue)-Citer
    return bumps

def simulateTime(cows, barn, totalWeight):
    rightNumCows = sum([1 if c[2] == 1 else 0 for c in cows])
    leftNumCows = len(cows) - rightNumCows
    rightCowsR = [cows[c] for c in range(len(cows)-1, leftNumCows-1, -1)]
    rightCowsR = rightCowsR[::-1]
    leftCowsR = [cows[c] for c in range(0, leftNumCows)]
    rightCowsT = [c[1] for c in cows if c[2] == 1]
    leftCowsT = [c[1] for c in cows if c[2] == -1]
    for c in range(len(rightCowsR)):
        rightCowsR[c].append(L - rightCowsT[c])
    for c in range(len(leftCowsR)):
        leftCowsR[c].append(leftCowsT[c])
    
    ret = rightCowsR + leftCowsR
    ret.sort(key=lambda x: x[3])

    w = 0
    for c in range(len(ret)):
        w += ret[c][0]
        if w >= totalWeight/2:
            time = ret[c][3]
            break
    
    return simulateBumps(time, cows)



with open('meetings.in') as fIn:
    lines = fIn.readlines()
    N, L = lines[0].strip().split()
    N = int(N)
    L = int(L)

cows = [[int(n) for n in lines[c].strip().split()]for c in range(1, N+1)]
cows.sort(key=lambda x: x[1])
totalWeight = sum([c[0] for c in cows])

ret = simulateTime(cows, L, totalWeight)

with open('meetings.out', 'w') as fOut:
    fOut.write(str(ret))
    fOut.write('\n')