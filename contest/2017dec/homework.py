with open("homework.in") as fInput:
    lines = fInput.readlines()
    N = int(lines[0].strip())
    scores = [int(l) for l in lines[1].strip().split()]



mean = sum(scores)/N
highest = 0
highestIndex = []

for ind in range(0, len(scores)-2):
    score = scores[ind]
    mean = (mean*(N - ind) - score)/(N-(ind+1))
    if mean > highest:
        highest = mean
        highestIndex = [ind + 1]
    elif mean == highest:
        highestIndex.append(ind + 1)


with open("homework.out", 'w') as fOutput:
    for h in highestIndex:
        fOutput.write(str(h) + '\n')