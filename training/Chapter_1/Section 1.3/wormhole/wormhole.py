"""
 ID: actuato2
 LANG: PYTHON3
 TASK: wormhole
"""
#global variables
cycleCount = 0

#Backstage Functions
class Wormhole:
    def __init__(self, x, y):
        self.pair = None
        self.next = None
        self.x = x
        self.y = y

    def pairTogether(self, hole):
        self.pair = hole
        hole.pair = self

    def unpairBoth(self, hole):
        self.pair = None
        hole.pair = None

    @property
    def paired(self):
        return self.pair != None

def populateWormholes(lines):
    holes = []
    for l in lines[1:]:
        x, y = l.strip().split(' ')
        holes.append(Wormhole(x, y))
    return holes

def setNext(holes):
    lY = list(set(h.y for h in holes))
    holeLines = [[] for s in lY]
    for h in holes:
        holeLines[lY.index(h.y)].append(h)
    for i in range(len(holeLines)):
        holeLines[i].sort(key=lambda h: h.x)
        for hi in range(len(holeLines[i])-1):
            holeLines[i][hi].next = holeLines[i][hi+1]

def isCycle(wormHoles):
    for h in range(len(wormHoles)):
        cur_check = wormHoles[h]
        for _ in range(len(wormHoles)):
            cur_check = cur_check.pair
            if cur_check.next != None:
                cur_check = cur_check.next
            else:
                break
        else:
            return True

    return False



def pairing(wormHoles):
    global cycleCount
    for i in range(len(wormHoles)):
        if not wormHoles[i].paired:
            break       
    else:
        if isCycle(wormHoles):
            cycleCount += 1
        return
    
    for j in range(i + 1, len(wormHoles)):
        if not wormHoles[j].paired:    
            wormHoles[i].pairTogether(wormHoles[j])
            pairing(wormHoles)
            wormHoles[i].unpairBoth(wormHoles[j])



# main program
with open('wormhole.in') as fIn:
    lines = fIn.readlines()


wormHoles = populateWormholes(lines)
setNext(wormHoles)
pairing(wormHoles)

with open('wormhole.out', 'w') as fOut:
    fOut.write(str(cycleCount) + '\n')
        