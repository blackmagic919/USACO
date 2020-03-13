"""
 ID: actuato2
 LANG: PYTHON3
 TASK: sprime
"""
def generatePrimes(length, ret):
    rt = []
    if length > 0:
        for n in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            r = [rm + n for rm in ret if not(hasfactors(int(rm+n)))]
            rt.extend(r)
        return generatePrimes(length-1, rt)
    else:
        return ret


def hasfactors(num):
    for f in range(2, int(num**0.5)+1):
        if num%f == 0:
            return True
    return False


with open('sprime.in') as fIn:
    lines = fIn.readlines()
    a = int(lines[0].strip())

ans = sorted(generatePrimes(a-1, ['2', '3', '5', '7']))

with open('sprime.out', 'w') as fOut:
    for a in ans:
        fOut.write(a + '\n')