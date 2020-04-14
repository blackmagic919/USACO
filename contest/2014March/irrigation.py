import heapq

Record = []

points = []

with open("irrigation.in") as fInput:
    lines = fInput.readlines()
    N, C = (int(n) for n in lines[0].strip().split())
    for l in range(1, N+1):
        v1, v2 = (int(v) for v in lines[l].strip().split())
        points.append([v1, v2])
        Record.append(False)
    

def PollNext(x1, y1, PQ, points):
    for p in range(len(points)):
        if (points[p][0]-x1)**2 + (points[p][1]-y1)**2 >= C:
            heapq.heappush(PQ, ((points[p][0]-x1)**2 + (points[p][1]-y1)**2, points[p][0], points[p][1], p))

    ret = 0
    for _ in PQ:
        poll = heapq.heappop(PQ)
        if Record[poll[3]] == False:
            Record[poll[3]] = True
            ret += PollNext(poll[1], poll[2], PQ, points) + poll[0]
    return ret

Record = Record[1::]
PQ = []
heapq.heapify(PQ)
x1 = points[0][0]
y1 = points[0][1]
points = points[1::]
sol = PollNext(x1, y1, PQ, points)

with open("irrigation.out", 'w') as fOutput:
    fOutput.write(str(sol) + '\n')


