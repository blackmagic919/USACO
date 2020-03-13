"""
 ID: actuato2
 LANG: PYTHON3
 TASK: preface
"""
I = 0
V = 0
X = 0
L = 0
C = 0
D = 0
M = 0

def getNum(rn):
    global I
    global V
    global X
    global L
    global C
    global D
    global M
    for n in rn:
        if n == 'I':
            I += 1
        elif n == 'V':
            V += 1
        elif n == 'X':
            X += 1
        elif n == 'L':
            L += 1
        elif n == 'C':
            C += 1
        elif n == 'D':
            D += 1
        elif n == 'M':
            M += 1

with open('preface.in') as fIn:
    lines = fIn.readlines()
    pages = int(lines[0].strip())

rn = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
for i in range(1, pages+1):
    rConverted = []
    pageNum = str(i)
    digit = 1
    for n in pageNum[::-1]:
        d = 0
        while d < int(n):
            if int(n)-d >= 9:
                rConverted.append(rn[10*digit])
                rConverted.append(rn[digit])
                d += 9
                continue
            elif int(n)-d >= 6:
                rConverted.append(rn[5*digit])
                rConverted.append(rn[digit])
                d += 6
                continue
            elif int(n)-d >= 5:
                rConverted.append(rn[5*digit])
                d += 5
                continue
            elif int(n)-d >= 4:
                rConverted.append(rn[5*digit])
                rConverted.append(rn[digit])
                d += 4
                continue
            rConverted.append(rn[digit])
            d += 1
        digit *= 10
    getNum(rConverted)
    print(rConverted)



with open('preface.out', 'w') as fOut:
    if I == 0:
        pass
    else:
       fOut.write('I ' + str(I))
       fOut.write('\n')
    if V == 0:
        pass
    else:
       fOut.write('V ' + str(V))
       fOut.write('\n')
    if X == 0:
        pass
    else:
       fOut.write('X ' + str(X))
       fOut.write('\n')
    if L == 0:
        pass
    else:
       fOut.write('L ' + str(L))
       fOut.write('\n')
    if C == 0:
        pass
    else:
       fOut.write('C ' + str(C)) 
       fOut.write('\n')
    if D == 0:
        pass
    else:
       fOut.write('D ' + str(D))
       fOut.write('\n')
    if M == 0:
        pass
    else:
       fOut.write('M ' + str(M)) 
       fOut.write('\n')