"""
 ID: actuato2
 LANG: PYTHON3
 TASK: milk2
"""
with open("milk2.in") as fInput:
    lines = fInput.readlines()

NumberOfFarmers = int(lines[0].strip())
Successor = 0
Milked = 0
NotMilked = 0
MergedTime = []

for i in range(1, NumberOfFarmers+1, 1):
    Beginning, End =  lines[i].strip().split()
    MergedTime.append([int(Beginning),int(End)])

MergedTime.sort(key = lambda x: x[0])

Successor = [MergedTime[0][0], MergedTime[0][1]]

if NumberOfFarmers == 1:
    Milked = Successor[1] - Successor[0]
    NotMilked = 0
else:
    for z in range(NumberOfFarmers):
        BeginningTime = MergedTime[z][0]
        EndTime = MergedTime[z][1]
        if BeginningTime <= Successor[1]:
            if EndTime >= Successor[1]:
                Successor[1] = EndTime
        elif MergedTime[z][0] - Successor[1] > NotMilked:
            NotMilked = MergedTime[z][0] - Successor[1]
            if Successor[1] - Successor[0] > Milked:
                Milked = Successor[1] - Successor[0]
            Successor = [MergedTime[0][0],MergedTime[0][1]]

with open("milk2.out", 'w') as fOutput:
    fOutput.write(str(Milked) + ' ' + str(NotMilked) + "\n")
    