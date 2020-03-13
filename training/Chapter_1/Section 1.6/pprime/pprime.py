import math
"""
 ID: actuato2
 LANG: PYTHON3
 TASK: pprime
"""
def generatePalindromes(start, end):
    ret = []
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    ret.append(1000000*a + 100000*b + 10000*c + 1000*d + 100*c +10*b + a)
                ret.append(100000*a + 10000*b + 1000*c + 100*c +10*b + a)
                ret.append(10000*a + 1000*b + 100*c +10*b + a)
            ret.append(1000*a + 100*b + 10*b + a)
            ret.append(100*a + 10*b + a)
        ret.append(10*a+a)
        ret.append(a)
    return ret


def hasfactors(num):
    for f in range(2, int(math.sqrt(num))+1):
        if num%f == 0:
            return True
    return False

def findPrimePalindromes(start, end):
    ret = []
    p = generatePalindromes(start, end+1)
    for num in p:
        if not(hasfactors(num)) and num >= start and num <= end+1:
            ret.append(num)
    return ret


with open('pprime.in') as fIn:
    lines = fIn.readlines()
    a, b = lines[0].strip().split()

ans = sorted(findPrimePalindromes(int(a), int(b)))
with open('pprime.out', 'w') as fOut:
    for a in ans:
        fOut.write(str(a) + '\n')