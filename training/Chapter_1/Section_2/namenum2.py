def GetPossibleNames(Number):
    ret = []
    if len(Number) == 1:
        return(list(numToLetters[Number[0]]))
    CurrentTransform = Number[0]
    LeaveToRest = GetPossibleNames(Number[1:])
    for e in range(3):
        for x in range(len(LeaveToRest)):
                ret.append(numToLetters[Number[0]][e] + LeaveToRest[x])
    return(ret)

with open("namenum.in2") as fInput:
    lines = fInput.readlines()
    lines = ([int(x.strip()) for x in lines[0].strip()])

numToLetters = {2:'ABC',5: 'JKL',8:'TUV',3: 'DEF',6:'MNO',9:'WXY',4: 'GHI',7: 'PRS'}

PossibleNames = GetPossibleNames(lines)

ret = []

1==1