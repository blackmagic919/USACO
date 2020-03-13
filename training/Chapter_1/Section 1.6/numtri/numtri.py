"""
 ID: actuato2
 LANG: PYTHON3
 TASK: numtri
"""


def CheckAllSums(tri, line, parents):
    for line in range(1, len(tri)):
        p = []
        p.append(int(parents[0]) + int(tri[line][0]))
        for point in range(1, len(tri[line])-1):
            if point == len(tri[line])-2:
                p.append(int(tri[line][point]) + int(max([parents[point-1], parents[point]])))
            else:
                p.append(int(tri[line][point]) + int(max([parents[point-1], parents[point]])))
        p.append(int(parents[-1]) + int(tri[line][-1]))
        if line == len(tri)-1:
            return max(p)
        else:
            parents = p.copy()

        

with open('numtri.in') as fIn:
    lines = fIn.readlines()
    triangle = [lines[l].strip().split() for l in range(1, len(lines))]

if len(triangle) > 1:
    greatestSum = CheckAllSums(triangle, 1, triangle[0])
else:
    greatestSum = int(triangle[0][0])

with open('numtri.out', 'w') as fOut:
    fOut.write(str(greatestSum) + '\n')