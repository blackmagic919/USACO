"""
 ID: actuato2
 LANG: PYTHON3
 TASK: castle
"""
roomToCoords = dict()
bestWall = '10000000 1000000000 E'

def findDifference(s1, s2):
    dif = [s for s in s1]
    for n in s2:
        dif.remove(n)
    return dif

def checkConnection(room):
    ret = []
    xr, yr = room.strip().split()
    for x in range(-1, 2, 2):
        if (str(x+int(xr)) + ' ' + str(0+int(yr))) in roomToCoords:
            ret.append([roomToCoords[str(int(xr) + x) + ' ' + str(int(yr) + 0)], room])
            if x == -1:
                ret[-1].append('W')
            else:
                ret[-1].append('E')
    for y in range(-1, 2, 2):
        if (str(0+int(xr)) + ' ' + str(y+int(yr))) in roomToCoords:
            ret.append([roomToCoords[str(int(xr) + 0) + ' ' + str(int(yr) + y)], room])
            if y == -1:
                ret[-1].append('N')
            else:
                ret[-1].append('S')
    return ret

def floodFillRooms(connected, roomCheck, castle, unchecked, ret):
    newRCheck = []
    if len(roomCheck) == 0:
        return 0 
    for r in roomCheck:
        if r in unchecked:
            unchecked.remove(r)
        connected.extend(checkConnection(r))
        noWalls = findDifference('NSEW', castle[r])
        coords = [int(n) for n in r.split()]
        for d in noWalls:
            if d == 'N':
                if (str(coords[0]) + ' ' + str(coords[1]-1)) in unchecked:
                    newRCheck.append(str(coords[0]) + ' ' + str(coords[1]-1))
                    unchecked.remove(str(coords[0]) + ' ' + str(coords[1]-1))
            elif d == 'S':
                if (str(coords[0]) + ' ' + str(coords[1]+1)) in unchecked:
                    newRCheck.append(str(coords[0]) + ' ' + str(coords[1]+1))
                    unchecked.remove(str(coords[0]) + ' ' + str(coords[1]+1))
            elif d == 'E':
                if (str(coords[0]+1) + ' ' + str(coords[1])) in unchecked:
                    newRCheck.append(str(coords[0]+1) + ' ' + str(coords[1]))
                    unchecked.remove(str(coords[0]+1) + ' ' + str(coords[1]))
            elif d == 'W':
                if (str(coords[0]-1) + ' ' + str(coords[1])) in unchecked:
                    newRCheck.append(str(coords[0]-1) + ' ' + str(coords[1]))
                    unchecked.remove(str(coords[0]-1) + ' ' + str(coords[1]))
    ret.extend(newRCheck)
    return floodFillRooms(connected, newRCheck, castle, unchecked, ret) + len(roomCheck)


def getWallForBest(room, size, most):
    global bestWall
    bY, bX, bD = bestWall.strip().split()
    bX = int(bX)
    bY = int(bY)
    nX, nY = room[1].strip().split()
    nX = int(nX)
    nY = int(nY)
    nD = room[2]
    if not(nD == 'E' or nD == 'N'):
        if nD == 'W':
            nX -= 1
            nD = 'E'
        else:
            nD = 'N'
            nY += 1
    if room[0] + size > most:
        bestWall = str(nY) + ' ' + str(nX) + ' ' + str(nD)
        return
    elif nX < bX:
        bestWall = str(nY) + ' ' + str(nX) + ' ' + str(nD)
        return
    elif nX == bX:
        if nY > bY:
            bestWall = str(nY) + ' ' + str(nX) + ' ' + str(nD)
            return
        elif nY == bY:
            if nD == 'N' and bD == 'E':
                bestWall = str(nY) + ' ' + str(nX) + ' ' + str(nD)
                return

def checkMaxConnected(cRooms, size, mostRooms):
    best = None
    for r in cRooms:
        if (r[0] + size) >= mostRooms:
            getWallForBest(r, size, mostRooms)
            best = r[0] + size
            mostRooms = r[0] + size
    if best != None:
        return best
    else:
        return mostRooms

def addToDict(rooms, size):
    for r in rooms:
        roomToCoords[r] = size

def layoutRooms(castle):
    uncheckedRooms = [r for r in castle]
    rooms = 0
    largestRoom = 0
    maximum = 0
    while len(uncheckedRooms) > 0:
        initRoom = [uncheckedRooms[0]]
        roomConnection = []
        roomsIn = initRoom.copy()
        connected = floodFillRooms(roomConnection, initRoom, castle, uncheckedRooms, roomsIn)
        addToDict(roomsIn, connected)
        maximum = checkMaxConnected(roomConnection, connected, maximum)
        if connected > largestRoom:
            largestRoom = connected
        rooms += 1
    return [rooms, largestRoom, maximum, bestWall]
        
        


with open('castle.in') as fIn:
    lines = fIn.readlines()
    N,M = lines[0].strip().split()

N = int(N)
M = int(M)
castle = {}
roomWalls = {15: 'NSEW', 14: 'NSE', 13: 'SEW', 12:'SE', 11:'NSW', 10:'NS', 9:'SW', 8:'S', 7:'NEW', 6:'NE', 5:'EW', 4: 'E', 3:'NW', 2:'N', 1:'W', 0:''}
for c in range(1, M+1):
    ca = [int(n) for n in lines[c].strip().split()]
    for room in range(N):
        castle[str(room+1)+' '+str(c)] = roomWalls[ca[room]]

sol = layoutRooms(castle)

with open('castle.out', 'w') as fOut:
    for s in sol:
        fOut.write(str(s))
        fOut.write('\n')

