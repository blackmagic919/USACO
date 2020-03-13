"""
 ID: actuato2
 LANG: PYTHON3
 TASK: frac1
"""
def deleteDuplicates(di):
    checked = {}
    remove = []
    for e in di:
        if di.get(e) in checked:
            if int(e[e.index('/')+1:]) < int(checked[di.get(e)][checked[di.get(e)].index('/')+1:]):
                remove.append((checked[di.get(e)]))
            else:
                remove.append(e)
        else:
            checked[di.get(e)] = e
    for u in remove:
        di.pop(u)
    di = sorted(di, key = lambda x: di.get(x))
    return di

with open('frac1.in') as fIn:
    lines = fIn.readlines()
    denominator = int(lines[0].strip())

ans = {}

for a in range(1, denominator+1):
    for b in range(0, a+1):
        ans[str(b)+'/'+str(a)] = b/a


ans = [i for i in deleteDuplicates(ans)]


with open('frac1.out', 'w') as fOut:
    for a in ans:
        fOut.write(a + '\n')