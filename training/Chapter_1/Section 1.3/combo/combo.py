"""
 ID: actuato2
 LANG: PYTHON3
 TASK: combo
"""
def convertDial(number, maxDial):
    ret = number
    while ret > maxDial or ret <= 0:
        if ret > maxDial:
            ret -= maxDial
        else:
            ret += maxDial
    return ret

with open("combo.in") as fInput:
    lines = fInput.readlines()
N = int(lines[0].strip())
FJCombo = [int(i) for i in lines[1].strip().split()]
MasterCombo = [int(i) for i in lines[2].strip().split()]
PossibleCombos = set()

for e in range(-2, 3):
    for x in range(-2, 3):
        for y in range(-2, 3):
            PossibleCombos.add(str(convertDial(FJCombo[0]+ e, N)) + str(convertDial(FJCombo[1]+ x, N)) + str(convertDial(FJCombo[2]+ y, N)))
            PossibleCombos.add(str(convertDial(MasterCombo[0]+e, N)) + str(convertDial(MasterCombo[1]+x, N)) + str(convertDial(MasterCombo[2]+y, N)))

with open("combo.out", 'w') as fOutput:
    fOutput.write(str(len(PossibleCombos))+'\n')