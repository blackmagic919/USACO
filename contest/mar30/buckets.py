def sameAsRockXU(Cow, Barn, Rock):
    return Barn[0] == Rock[0] and Cow[0]+1 == Rock[0] and ((Cow[1] <= Rock[1] and Rock[1] < Barn[1]) or (Cow[1] >= Rock[1] and Rock[1] > Barn[1]))

def sameAsRockXD(Cow, Barn, Rock):
    return Barn[0] == Rock[0] and Cow[0]-1 == Rock[0] and ((Cow[1] <= Rock[1] and Rock[1] < Barn[1]) or (Cow[1] >= Rock[1] and Rock[1] > Barn[1]))

def sameAsRockYU(Cow, Barn, Rock):
    return Barn[1] == Rock[1] and Cow[1]+1 == Rock[1] and ((Cow[0] <= Rock[0] and Rock[0] < Barn[0]) or (Cow[0] >= Rock[0] and Rock[0] > Barn[0]))

def sameAsRockYD(Cow, Barn, Rock):
    return Barn[1] == Rock[1] and Cow[1]-1 == Rock[1] and ((Cow[0] <= Rock[0] and Rock[0] < Barn[0]) or (Cow[0] >= Rock[0] and Rock[0] > Barn[0]))


with open("buckets.in") as fInput:
    lines = fInput.readlines()

lines = [i.strip() for i in lines]
rocks = []


1==1
for i in range(10):
    for e in range(10):
        if lines[i][e] == 'R':
            Rock = [e, 10-i]
        if lines[i][e] == 'B':
            Barn = [e, 10-i]
        if lines[i][e] == 'L':
            Lake = [e, 10-i]

CC = Lake
Cows = 0

while not((CC[0]+1 == Barn[0] and CC[1] == Barn[1]) or (CC[0]-1 == Barn[0] and CC[1] == Barn[1]) or (CC[0] == Barn[0] and CC[1]+1 == Barn[1]) or (CC[0] == Barn[0] and CC[1]-1 == Barn[1])):
    if CC[0] < Barn[0] and not(sameAsRockXU(CC, Barn, Rock)):
        Cows += 1
        CC[0] += 1
        if CC == Rock:
            Cows -= 1
            CC[0] -= 1
    elif CC[0] > Barn[0] and not(sameAsRockXD(CC, Barn, Rock)):
        Cows += 1
        CC[0] -= 1
        if CC == Rock:
            Cows -= 1
            CC[0] += 1
    elif CC[1] < Barn[1] and not(sameAsRockYU(CC, Barn, Rock)):
        Cows += 1
        CC[1] += 1
        if CC == Rock:
            Cows -= 1
            CC[1] -= 1
    elif CC[1] > Barn[1] and not(sameAsRockYD(CC, Barn, Rock)):
        Cows += 1
        CC[1] -= 1
        if CC == Rock:
            Cows -= 1
            CC[1] += 1
    
    if CC[0] == Rock[0] and Barn[0] == Rock[0] and ((CC[1] <= Rock[1] and Rock[1] < Barn[1]) or (CC[1] >= Rock[1] and Rock[1] > Barn[1])):
        if CC[0] == 10:
            CC[0] -= 1
        elif CC[0] == 0:
            CC[0] += 1
        else:
            CC[0] += 1
        Cows += 1
    elif CC[1] == Rock[1] and Barn[1] == Rock[1] and((CC[0] <= Rock[0] and Rock[0] < Barn[0]) or (CC[0] >= Rock[0] and Rock[0] > Barn[0])):
        if CC[1] == 10:
            CC[1] -= 1
        elif CC[1] == 0:
            CC[1] += 1
        else:
            CC[1] += 1
        Cows += 1

with open("buckets.out", 'w') as fOutput:
    fOutput.write(str(Cows) + '\n')