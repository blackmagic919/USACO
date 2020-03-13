def CheckIndividual(trait, exclusion):
    for generation in SubPop:
        if trait in generation and exclusion not in generation:
            return True
            

with open("evolution.in") as fInput:
    lines = fInput.readlines()

N = int(lines[0].strip())
SubPop = []

for i in range(1, N+1):
    SubPop.append([e for e in lines[i].strip().split()])
    if SubPop[i-1][0] == '0':
        SubPop[i-1][0] = 'none'
    else:
        SubPop[i-1] = SubPop[i-1][1:]

Possible = 'yes'

Individuals = []
for generation in SubPop:
    for gene in generation:
        if len(generation) >= 2:
            check = generation.copy()
            check.remove(gene)
            for i in check:
                if CheckIndividual(gene, i): 
                    if CheckIndividual(i, gene):
                        Possible = 'no'

with open("evolution.out", 'w') as fOutput:
    fOutput.write(Possible + '\n')