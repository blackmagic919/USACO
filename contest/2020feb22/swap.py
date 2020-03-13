
def swap(l, rev):
    s = rev[0]-1
    e = rev[1]
    l[s:e] = l[s:e][::-1]
    return l

def runProcess(l, process, repeats):
    for _ in range(repeats):
        for p in process:
            l = swap(l, p)
    return l

with open('swap.in') as finput:
    lines = finput.readlines()
    N, M, K = (int(n) for n in lines[0].strip().split())
    process = [[int(i) for i in lines[int(n)].strip().split()]for n in range(1, M+1)]

f = runProcess([n+1 for n in range(N)], process, K)

with open('swap.out', "w") as fOutput:
    for n in f:
        fOutput.write(str(n) + '\n')
