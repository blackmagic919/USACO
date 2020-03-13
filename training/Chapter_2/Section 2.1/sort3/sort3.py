"""
 ID: actuato2
 LANG: PYTHON3
 TASK: sort3
"""
switch = 0

def exchange(l, n1, n2):
    ret = l.copy()
    ret[n1] = l[n2]
    ret[n2] = l[n1]
    return ret

def minswitch(s):
    global switch
    if s < switch:
        switch = s

with open('sort3.in') as fIn:
    lines = fIn.readlines()
    l = [int(lines[n].strip()) for n in range(1, len(lines))]

lsort = sorted(l)

def findAllPerfect(l, sort):
    global switch
    for n in range(len(l)):
        if l[n] != sort[n]:
             for n1 in range(len(l)):
                 if l[n1] != sort[n1]:
                    if l[n] == sort[n1] and l[n1] == sort[n]:
                            l = exchange(l, n, n1)
                            switch += 1
    return l


def findAllNonPerfect(l, sort):
    global switch
    for n in range(len(l)):
        if l[n] != sort[n]:
            for n1 in [i for i in range(len(l)) if sort[i] == l[n] and l[i] != sort[i] and l[i] != l[n]]:
                l = exchange(l, n, n1)
                switch += 1
                break

findAllNonPerfect(findAllPerfect(l, lsort), lsort)


with open('sort3.out', 'w') as fOut:
        fOut.write(str(switch) + '\n')