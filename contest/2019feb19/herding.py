with open('herding.in') as input:
    lines = input.readlines()
    B, E, M = lines[0].strip().split()

cows = [int(B), int(E), int(M)]
cows.sort()
if cows[2] - cows[1] == 2 or cows[1] - cows[0] == 2:
    minMoves = 1
else:
    minMoves = 2

if cows[2] - cows[1] > cows[1] - cows[0]:
    maxMoves = cows[2]-cows[1]-1
else:
    maxMoves = cows[1]-cows[0]-1

if cows[0] + 1 == cows[1] and cows[1] + 1 == cows[2]:
    minMoves = 0
    maxMoves = 0
    
with open("herding.out", "w") as output:
    output.write(str(minMoves)+'\n' + str(maxMoves)+'\n')


