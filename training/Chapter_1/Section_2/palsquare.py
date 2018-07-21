"""
 ID: actuato2
 LANG: PYTHON3
 TASK: palsquare
"""
#Will become list of SquarePalindromes
SquarePalindromes = []

BASE_DICT = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K'}

with open("palsquare.in") as fInput:
    lines = fInput.readlines()
    base = int(lines[0].strip())

#Yasss I used Recursion on my own, Hallelujah
def ConvertUsingBase(Number,Base):
    PreConversion = int(Number) % Base
    Conversion = BASE_DICT[PreConversion]
    if int(Number) - PreConversion == 0:
        return(str(Conversion))
    return (ConvertUsingBase(str(int((int(Number) - PreConversion)/Base)),Base) + str(Conversion))

for e in range(1, 300):
    Number = ConvertUsingBase(str(e), base)
    SquareNumber = ConvertUsingBase(str(e*e), base)
    if SquareNumber == SquareNumber[::-1]:
        SquarePalindromes.append([Number,SquareNumber])

with open("palsquare.out", 'w') as fOutput:
    for i in range(len(SquarePalindromes)):
        fOutput.write(str(SquarePalindromes[i][0]) + ' ' + str(SquarePalindromes[i][1]) + '\n')