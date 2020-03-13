
def checkPasture(combination, condition):
    for i in range(len(condition)):
        if combination[condition[i][0]-1] == combination[condition[i][1]-1]:
            return True
    return False

def convertToBase4(number):
    ret = number.copy()
    for i in range(len(ret)-1, -1, -1):
        if int(ret[i]) > 4:
            ret[i-1] = int(ret[i-1]) + 1
            ret[i] = 1
    return ret

with open('revegetate.in') as input:
    lines = input.readlines()
    N, M = lines[0].strip().split()
    N = int(N)
    M = int(M)

cowToPasture = []
for i in range(1, M+1):
    cowToPasture.append([int(i) for i in lines[i].strip().split()])

Pasture = [1 for i in range(N)]

while checkPasture(Pasture, cowToPasture):
    P = ''.join(str(e) for e in Pasture)
    P = str(int(P)+1)
    Pasture = convertToBase4([int(P[i]) for i in range(len(str(int(P) + 1)))])

with open("revegetate.out", "w") as output:
    for i in range(N):
        output.write(str(Pasture[i]))