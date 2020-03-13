"""
 ID: actuato2
 LANG: PYTHON3
 TASK: subset
"""
partitions = []
def findAllPartitions(sn, look, sol):
    if look == 1 or look == 2:
        sol += 1
        return
    else:
        findAllPartitions(sn[0::len(sn)-1], look-sn[-1], sol)
        if sum()

            


with open('subset.in') as fIn:
    lines = fIn.readlines()
    N = int(lines[0].strip())
setNumbers = [n for n in range(1, N+1)]

sol = 0

findAllPartitions(setNumbers, sum(setNumbers)/2, sol)

