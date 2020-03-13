"""
 ID: actuato2
 LANG: PYTHON3
 TASK: barn1
"""
def findGap(Value1, Value2):
    return Value2 - Value1

def findLargestGaps(gaps, gapamount):
    gaps.sort(reverse = True)
    if gapamount > len(gaps):
        gapamount = len(gaps)
    ret = [gaps[i] for i in range(gapamount)]
    return ret

with open("barn1.in") as fInput:
    lines = fInput.readlines()

M, S, C = [int(i) for i in lines[0].strip().split()]
occupiedStalls = sorted([int(lines[i].strip()) for i in range(1, C+1)])
Gaps = []
CoveredStalls = 1

for i in range(0, C-1):
    Gaps.append([findGap(occupiedStalls[i], occupiedStalls[i+1]), i])

Seperations = findLargestGaps(Gaps, M-1)
Seperations.sort(key=lambda x:x[1])

for i in range(0, C-1):
    if Seperations:
        if Seperations[0][1] != i:
            CoveredStalls += occupiedStalls[i+1] - occupiedStalls[i]
        else:
            Seperations.remove(Seperations[0])
            CoveredStalls += 1
    else:
        CoveredStalls += occupiedStalls[i+1] - occupiedStalls[i]

with open("barn1.out", 'w') as fOutput:
    fOutput.write(str(CoveredStalls)+'\n')


