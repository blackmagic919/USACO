def findMaxTwo(xd, yd, points):
    sq0 = 0
    sq1 = 0
    for p in points:
        y = max(xd[p[0]]) - p[1]
        x = max(yd[p[1]]) - p[0]
        area = x*y*(1/2)
        if area >= sq0:
            sq0 = area
        elif area > sq1:
            sq1 = area
        else:
            if len(xd[p[0]]) > 1:
                px = sorted(xd[p[0]])[len(xd[p[0]])-2]
            else:
                px = 0
            if len(yd[p[1]]) > 1:
                py = sorted(yd[p[1]])[len(yd[p[1]])-2]
            else:
                py = 0
            y1 = px - p[1]
            x1 = py - p[0]
            area = max(x1*y*(1/2), x*y1*(1/2), x1*y1*(1/2))
            if area > sq1:
                sq1 = area
    return sq0, sq1

with open('triangles.in') as finput:
    lines = finput.readlines()
    points = [[int(i) for i in lines[int(n)].strip().split()]for n in range(1, len(lines))]

xd = dict()
yd = dict()
for p in points:
    if p[0] in xd:
        xd[p[0]].append(p[1])
    else:
        xd[p[0]] = [p[1]]
    if p[1] in yd != None:
        yd[p[1]].append(p[0])
    else:
        yd[p[1]] = [p[0]]

s1, s2 = findMaxTwo(xd, yd, points)

with open('triangles.out', "w") as fOutput:
    fOutput.write(str(int(2*(s1+s2))) + '\n')