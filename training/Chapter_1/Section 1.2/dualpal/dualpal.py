"""
 ID: actuato2
 LANG: PYTHON3
 TASK: dualpal
"""
def ConvertToBase(base, num):
    if num/base < 1:
        return str(num%base)
    return str(num%base) + str(ConvertToBase(base, int(num/base)))

def CheckIfDualPal(PP):
    e = 0
    for i in range(2, 11):
        converted = ConvertToBase(i, PP)
        if converted[::-1] == converted:    
            e += 1
        if e == 2:
            return True
    return False
            

with open("dualpal.in") as fInput:
    lines = fInput.readlines()

N, S = [int(i) for i in lines[0].strip().split()]
i = 1
Palindromes = []

while N > 0:
    if CheckIfDualPal(S+i):
        Palindromes.append(S+i)
        N -= 1
    i += 1

with open("dualpal.out", 'w') as fOutput:
    for i in Palindromes:
        fOutput.write(str(i) + '\n')