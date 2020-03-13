"""
 ID: actuato2
 LANG: PYTHON3
 TASK: milk2
"""
MilkTime = []
IdleTime = []
Log = [[],[]]
TBMerge = []
maxMilkTime = 0
minMilkTime = 0
NewGroup = False

# Merge 2 ranges.
def Merge(Range):
    SmallVal = 999999999999
    BigVal = -1
    for i in Range:
        if i in MilkTime:
            MilkTime.remove(i)
        if i[0] < SmallVal:
            SmallVal = i[0]
        if i[1] > BigVal:
            BigVal = i[1] 
    return[SmallVal, BigVal]

# Intesection check between 2 ranges(Beginning-End, TimeCheck)
# Params:
#   TimeCheck is a list of [beginning, end] to be checked.
#   Beginning is the beginning to check against.
#   End is the end to check against.
# Returns:
#   1 - TimeCheck is within Beginning-End
#   false - TimeCheck and Beginning-End not interstected.
#   [resultBegin, resultList] - Merged range if TimeCheck and Bebinning-End intersected.
def CheckIntersection(Beginning, End, TimeCheck):
    if TimeCheck[0] <= End and TimeCheck[1] >= Beginning:
        return True
    else:
        return False
        
def CreateAlternateGroup(LineNo):
    TBMerge = []
    for e in range(len(MilkTime)):
        CheckInt = CheckIntersection(Log[0][LineNo], Log[1][LineNo], MilkTime[e])
        if CheckInt:
            TBMerge.append(MilkTime[e])
    return TBMerge



def MatchEachLine():
    for i in range(1, Lines_in_Log):
        GroupData = CreateAlternateGroup(i)
        if GroupData == []:
            MilkTime.append([Log[0][i], Log[1][i]])
        else:
            GroupData.append([Log[0][i], Log[1][i]])
            MilkTime.append(Merge(GroupData))

    

with open("milk2.in") as fInput:
    lines = fInput.readlines()

Lines_in_Log = int(lines[0].strip())
for i in range(Lines_in_Log):
    a, b = lines[i+1].strip().split()
    Log[0].append(int(a))
    Log[1].append(int(b))


MilkTime.append([Log[0][0], Log[1][0]])

MatchEachLine()

MilkTime = sorted(MilkTime)
print(MilkTime)

for e in range(len(MilkTime)):
    if MilkTime[e][1] - MilkTime[e][0] > maxMilkTime:
        maxMilkTime = MilkTime[e][1] - MilkTime[e][0]
    if e != len(MilkTime)-1:
        if MilkTime[e+1][0] - MilkTime[e][1] > minMilkTime:
            minMilkTime = MilkTime[e+1][0] - MilkTime[e][1] 


with open("milk2.out", 'w') as fOutput:
    fOutput.write(str(maxMilkTime) + " " + str(minMilkTime) + "\n")
