def getNewRangeAndPos(Newpos, grass, cur):
    for f in range(cur, len(grass)):
        if Newpos >= grass[f][0] and Newpos <= grass[f][1]:
            return(Newpos, f)
        if Newpos < grass[f][0]:
            return(grass[f][0], f)

def EnumerateField(interval, grass, cows):
    position = grass[0][0]
    Range = 0
    for _ in range(1, cows):
        if position + interval > grass[-1][1]:
            break
        if position + interval <= grass[Range][1]:
            position += interval
        else:
            position, Range = getNewRangeAndPos(position+interval, grass, Range)
    else:
        return True
    return False

def BinarySearchPossibilities(grass, N, upperBound, lowerBound):
    mean = (upperBound + lowerBound)/2

    if upperBound - lowerBound < 1:
        if EnumerateField(round(upperBound), grass, N):
            return round(upperBound)
        else:
            return round(upperBound)-1

    
    if EnumerateField(mean, grass, N):
        lowerBound = mean
    else:
        upperBound = mean
    

    return BinarySearchPossibilities(grass, N, upperBound, lowerBound)






with open('socdist.in') as fInput:
    lines = fInput.readlines()
    N, M = lines[0].strip().split()
    N = int(N)
    M = int(M)

Grass = sorted([[int(n) for n in lines[interval].strip().split()]for interval in range(1, M+1)])

sol = str(BinarySearchPossibilities(Grass, N, (Grass[-1][1])/(N-1), 0))

with open("socdist.out", 'w') as fOutput:
    fOutput.write(sol + '\n')