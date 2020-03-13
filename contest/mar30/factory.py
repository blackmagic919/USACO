def CanGetTo(goal):
    check = 0
    for i in range(1, Stations+1):
        Station = i
        for _ in range(Stations):
            if Station == goal:
                check += 1
            Station = ConveyerBelts.get(Station)
    if check == Stations:
        return True
    return False

with open("factory.in") as fInput:
    lines = fInput.readlines()

Stations = int(lines[0].strip())
ConveyerBelts = {}

for i in range(1, len(lines)):
    line = lines[i].strip().split()
    ConveyerBelts.update({int(line[0]): int(line[1])})

Center = False

for i in range(1, Stations+1):
    Station = i
    if CanGetTo(i):
        Center = Station
        break
if Center == False:
    Center = -1

with open("factory.out", 'w') as fOutput:
    fOutput.write(str(Center) + '\n')