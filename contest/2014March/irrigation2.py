
Edges = []
points = []

with open("irrigation.in") as fInput:
    lines = fInput.readlines()
    N, C = (int(n) for n in lines[0].strip().split())
    for l in range(1, N+1):
        v1, v2 = (int(v) for v in lines[l].strip().split())
        points.append((v1, v2))



for i in range(0, N-1):
    for j in range(1, N):
        v1 = points[i]
        v2 = points[j]
        x1 = v1[0]
        y1 = v1[1]
        x2 = v2[0]
        y2 = v2[1]
        w = (x1-x2)**2 + (y1-y2)**2
        if w>=C:
            Edges.append((w, i, j))

Edges.sort()

groups = []
def find(v):
    for group in groups:
        if v in group:
            return group
    return None

def unify(v1, v2):
    g1 = find(v1)
    g2 = find(v2)
    if g1 == g2 and g1 != None:
        return False
    else:
        if g1 != None and g2 == None:
            g1.add(v2)
        elif g2 != None and g1 == None:
            g2.add(v1)
        elif g1 == None and g2 == None:
            groups.append(set([v1, v2]))
        elif g1 != g2:
            g1.update(g2)
            groups.remove(g2)
        return True

result = 0
for edge in Edges:
    w = edge[0]
    v1 = edge[1]
    v2 = edge[2]
    if unify(v1, v2):
        result += w

if len(groups) > 1:
    result =-1

with open("irrigation.out", 'w') as fOutput:
    fOutput.write(str(result) + '\n')
