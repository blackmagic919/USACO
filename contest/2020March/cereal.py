

def checkRemove(cows):  
    checked = []
    satisfied = 0
    cow = 0 
    while len(cows) > cow:
        for preference in cows[cow]:
            if preference in checked:
                pass
            else:
                satisfied += 1
                checked.append(preference)
                break
        cow += 1
    return satisfied

with open('cereal.in') as fInput:
    lines = fInput.readlines()
    N, M = lines[0].strip().split()
    N = int(N)
    M = int(M)

cows = [[int(preference) for preference in lines[cow].strip().split()]for cow in range(1, N+1)]

ret = []

for cow in range(len(cows)):
    ret.append(checkRemove(cows[cow:len(cows)]))

with open("cereal.out", 'w') as fOutput:
    for n in ret:
        fOutput.write(str(n) + '\n')