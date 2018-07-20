"""
 ID: actuato2
 LANG: PYTHON3
 TASK: transform
"""

def Mirror(Shape):
    ret = []
    for i in range(len(Shape)):
        ret.append([Shape[i][x] for x in range(len(Shape[i])-1, 0-1,  -1)])
    return(ret)

def Rotate(Shape):
    ret = []
    for e in range(len(Shape)):
        ret.append([Shape[x][e] for x in range(len(Shape[e])-1,0-1,-1)])
    return(ret)

def End(Number):
    with open("transform.out", 'w') as fOutput:
        fOutput.write(str(Number) + '\n')



with open("transform.in") as fInput:
    lines = fInput.readlines()

side = int(lines[0].strip())
PreSquare = []
Square = []

for i in range(1, side+1, 1):
    PreSquare.append(lines[i].strip())

for i in range(side+1, side*2+1, 1):
    Square.append([lines[i].strip()[x] for x in range(side)])

if Rotate(PreSquare) == Square:
    End(1)
elif Rotate(Rotate(PreSquare)) == Square:
    End(2)
elif Rotate(Rotate(Rotate(PreSquare))) == Square:
    End(3)
elif Mirror(PreSquare) == Square:
    End(4)
elif Rotate(Mirror(PreSquare)) == Square or Rotate(Rotate(Mirror(PreSquare))) == Square or Rotate(Rotate(Rotate(Mirror(PreSquare)))) == Square:
    End(5)
elif PreSquare == Square:
    End(6)
else:
    End(7)