import statistics 
"""
 ID: actuato2
 LANG: PYTHON3
 TASK: skidesign
"""
with open("skidesign.in") as fInput:
    lines = fInput.readlines()

N = int(lines[0].strip())
ret = 0
hills = [int(lines[i].strip()) for i in range(1, N+1)]
hills.sort()
costs = []
Min = min(hills)
Max = min(hills) + 17

for i in range(max(hills) - min(hills)-17):
    cost = 0
    for e in range(len(hills)):
        if hills[e] < Min:
            cost += (Min - hills[e])**2
        elif hills[e] > Max:
            cost += (hills[e] - Max)**2
    costs.append(cost)
    Min += 1
    Max += 1

if costs == []:
    costs = [0]

with open("skidesign.out", 'w') as fOutput:
    fOutput.write(str(int(min(costs)))+'\n')