import math
def findMultiplesInsideAndAdd(prevNums, n):
    num = (math.floor(n/5) + math.floor(n/3)) - math.floor(n/15)
    if num-prevNums==0:
        return num
    return findMultiplesInsideAndAdd(num, num-(prevNums)+n)

with open('moobuzz.in') as fIn:
    lines = fIn.readlines()
    N = int(lines[0].strip())

num = N + findMultiplesInsideAndAdd(0, N)

with open('moobuzz.out', 'w') as fOut:
    fOut.write(str(num))
    fOut.write('\n')

