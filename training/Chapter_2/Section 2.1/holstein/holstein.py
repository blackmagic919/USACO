"""
 ID: actuato2
 LANG: PYTHON3
 TASK: holstein
"""
import math
remaining = dict()
def getRemaining(new, requirements):
    ret = []
    for i in range(len(requirements)):
        if requirements[i] - feeds[new][i]< 0:
            ret.append(0)
        else:
            ret.append(requirements[i] - feeds[new][i])
    return ret

def getFeedNumbers(feeds, possibility):
    ret = []
    for p in possibility:
        ret.append(feeds.index(list(p)))
    ret.sort()
    return ret

def makeFirstRem():
    for f in feeds:
        remaining[str(f)] = getRemaining(f, requirements)

def createFeedTree(feeds, requirements, possibilities):
    newPossibilities = []
    for p in possibilities:
        for f in range(len(feeds))[p[-1]+1::]:
            rem = getRemaining(f, remaining[" ".join(str(i) for i in p)])
            p1 = p.copy()
            p1.append(f)
            if sum(rem) <= 0:
                return p1
            newPossibilities.append(p1)
            remaining[" ".join(str(i) for i in p1)] = rem
    return createFeedTree(feeds, requirements, newPossibilities)

with open('holstein.in') as fIn:
    lines = fIn.readlines()
    requirements = [int(n) for n in lines[1].strip().split()]
    feedNum = [[int(n1) for n1 in lines[n].strip().split()]for n in range(3, len(lines))]

feeds = dict()
for i in range(len(feedNum)):
    feeds[i] = feedNum[i]


def initialCheck(requirements, check):
    for c in check:
        if sum(getRemaining(c[0], requirements))<=0:
            return c
    return False

if initialCheck(requirements, [[f] for f in feeds]):
    solution = initialCheck(requirements, [[f] for f in feeds])
else:
    makeFirstRem()
    solution = createFeedTree(feeds, requirements, [[f] for f in feeds])

with open('holstein.out', 'w') as fOut:
    fOut.write(str(len(solution)))
    for a in range(len(solution)):
        fOut.write(' ' + str(solution[a]+1))
    fOut.write('\n') 