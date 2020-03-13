import math
with open('berries.in') as fInput:
    lines = fInput.readlines()
    M, K = lines[0].strip().split()
    M = int(M)
    K = int(K)
    trees = [int(t) for t in lines[1].strip().split()]

m = 0

for b in range(1, max(trees)+1):
    l = []
    for t in trees:
        if t >= b:
            for _ in range(math.floor(t/b)):
                l.append(b)
            l.append(t%b)
        else:
            l.append(t)
    l.sort()
    l = l[::-1]
    if len(l) > K:
        l = l[:K]
    elif len(l) < K:
        for b in range(K-len(l)):
            l.append(0)
    if sum(l[int(len(l)/2)::]) > m:
        m = sum(l[int(len(l)/2)::])


with open("berries.out", "w") as fOutput:
    fOutput.write(str(m))

