"""
 ID: actuato2
 LANG: PYTHON3
 TASK: milk
"""
def GetMilkAmount(requirement, deal):
    if deal > requirement:
        return requirement
    else:
        return deal

def GetCost(units, cperu):
    return units*cperu

with open("milk.in") as fInput:
    lines = fInput.readlines()

N, M = [int(i) for i in lines[0].strip().split()]
#I did so many things in this one line below
Pi_Ai = sorted([[int(e) for e in lines[i+1].strip().split()] for i in range(M)])
cost = 0


while N > 0:
   units = GetMilkAmount(N, Pi_Ai[0][1])
   cost += GetCost(units, Pi_Ai[0][0])
   Pi_Ai.remove(Pi_Ai[0])
   N -= units


with open("milk.out", 'w') as fOutput:
    fOutput.write(str(cost)+'\n')