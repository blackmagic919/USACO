"""
 ID: actuato2
 LANG: PYTHON3
 TASK: crypt1
"""
def checkFit(Set, InsertList, PartorProd):
    Set = list(tuple(sorted(Set)))
    for i in Set:
        if i in InsertList:
            if PartorProd == 0 and len(Set) == 3:
                continue
            elif PartorProd == 1 and len(Set) == 4:
                continue
            else:
                return False
        else:
            return False
    return True

def getProduct(f1, f2):
    if type(f1) == list:
        f1 = int(''.join(map(str, f1)))
    if type(f2) == list:
        f2 = int(''.join(map(str, f2)))
    return [int(d) for d in str(f1*f2)]



with open("crypt1.in") as fInput:
    lines = fInput.readlines()

acceptedNums = sorted([int(i) for i in lines[1].strip().split()])
factor1 = []
factor2 = []
partialProduct1 = []
partialProduct2 = []
product = []
solutions = 0

for m in acceptedNums:
    for y in acceptedNums:
        factor2 = [m, y]
        for i in acceptedNums:
            for e in acceptedNums:
                for x in acceptedNums:
                    factor1 = [i,e,x]
                    partialProduct1 = getProduct(factor1, factor2[0])
                    partialProduct2 = getProduct(factor1, factor2[1])
                    product = getProduct(factor1, factor2)
                    if checkFit(partialProduct1, acceptedNums, 0) and checkFit(partialProduct2, acceptedNums, 0) and checkFit(product, acceptedNums, 1):
                        solutions += 1
                        print(str(factor1)+str(factor2)+str(partialProduct1)+str(partialProduct2)+str(product) )

with open("crypt1.out", 'w') as fOutput:
    fOutput.write(str(solutions)+'\n')