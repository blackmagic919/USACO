import math
import sys
# K - Days 
# N - Loan amount of Milk
# M - minumum pay
sys.setrecursionlimit(50000)

DAYS = 0
def getNumDays(milk, i, end, s, K):
    global DAYS
    portion = (milk-s)/i
    if DAYS > K:
        return None
    if portion < end:
        return 0
    if portion * (K-DAYS) < milk:
        return None
    DAYS += 1
    ret = getNumDays(milk-s, i, end, ((milk-s)/i), K)
    if ret == None:
        return ret
    else:
        return portion + ret


with open('loan.in') as fInput:
    lines = fInput.readlines()
    N, K, M = lines[0].strip().split()
    N = int(N)
    K = int(K)
    M = int(M)

m = 0

for d in range(1, N):
    DAYS = 0
    ret = getNumDays(N, d, M, 0, K)
    if ret == None:
        break
    elif ret + (K-DAYS)*M > N:
        if d > m:
            m = d
    else:
        break

with open("loan.out", "w") as fOutput:
    fOutput.write(str(m))