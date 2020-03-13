"""
 ID: actuato2
 LANG: PYTHON3
 TASK: milk3
"""
def transfer(Max, exisitingQuant, quantity):
    if quantity > Max-exisitingQuant:
        if exisitingQuant == Max:
            return(exisitingQuant, quantity)
        else:
            if quantity > Max-exisitingQuant:
                return(exisitingQuant+(Max-exisitingQuant), quantity-(Max-exisitingQuant))
            else:
                return(0, exisitingQuant+quantity)
    else:
        return(exisitingQuant+quantity, 0)

def mixTogether(maxA, maxB, maxC, QA, QB, QC, checked, ret):
    if (QA, QB, QC) in checked:
        return ret
    else:
        checked.add((QA, QB, QC))
    if QA == 0:
        ret.add(QC)
    if QC > 0:
        QA1, QC1 = transfer(maxA, QA, QC)
        mixTogether(maxA, maxB, maxC, QA1, QB, QC1, checked, ret)
        QB1, QC1 = transfer(maxB, QB, QC)
        mixTogether(maxA, maxB, maxC, QA, QB1, QC1, checked, ret)
    if QB > 0:
        QA1, QB1 = transfer(maxA, QA, QB)
        mixTogether(maxA, maxB, maxC, QA1, QB1, QC, checked, ret)
        QC1, QB1 = transfer(maxC, QC, QB)
        mixTogether(maxA, maxB, maxC, QA, QB1, QC1, checked, ret)
    if QA > 0:
        QB1, QA1 = transfer(maxB, QB, QA)
        mixTogether(maxA, maxB, maxC, QA1, QB1, QC, checked, ret)
        QC1, QA1 = transfer(maxC, QC, QA)
        mixTogether(maxA, maxB, maxC, QA1, QB, QC1, checked, ret)

    return ret

with open('milk3.in') as fIn:
    lines = fIn.readlines()
    A, B, C = lines[0].strip().split()

ans = sorted(list(mixTogether(int(A), int(B), int(C), 0, 0, int(C), set(), set())))

result = ' '.join([str(a) for a in ans])
with open('milk3.out', 'w') as fOut:
    fOut.write(result + '\n')
