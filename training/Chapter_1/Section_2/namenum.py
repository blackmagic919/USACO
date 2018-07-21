"""
 ID: actuato2
 LANG: PYTHON3
 TASK: namenum
"""

def GetPossibleNames(PossibleNames, Number):
    NamePart = []
    if len(PossibleNames[0]) == len(lines):
        return(PossibleNames)
    for e in range(3):
        NamePart += [PossibleNames[x]+ numToLetters[lines[Number]][e] for x in range(len(PossibleNames))]
    return GetPossibleNames(NamePart, Number+1)

with open("dict.txt") as fInput:
    lines2 = fInput.readlines()
    lines2 = set(x.strip() for x in lines2)

with open("namenum.in") as fInput:
    lines = fInput.readlines()
    lines = ([int(x.strip()) for x in lines[0].strip()])

numToLetters = {2:'ABC',5: 'JKL',8:'TUV',3: 'DEF',6:'MNO',9:'WXY',4: 'GHI',7: 'PRS'}
Named = False

PossibleNames = GetPossibleNames(list(numToLetters[lines[0]]),1)

PossibleNames.sort()

with open("namenum.out", 'w') as fOutput:
    for e in PossibleNames:
        if e in lines2:
            fOutput.write(str(e) + '\n')
            Named = True

if Named == False:
    with open("namenum.out", 'w') as fOutput:
        fOutput.write("NONE" + '\n')

