# Check whether 2 segments are intesected or not
# segment is a lise of [beginneng, end]
def isIntesected(seg1, seg2):
    pass

# Merge a list of segments and one new segment and return the merged segment
def merge(segs, newseg):
    pass

# Read input to lines list
with open("Section 1.2/milk2/milk2.in") as fInput:
    lines = fInput.readlines()

# Form input segments
inSegments = [line.strip().split() for line in lines[1:]]


# Initialize result segments
resSegments = inSegments[0]

# Check every input segments against every result segment
for inSeg in inSegments[1:]:
    toBeMergedSegments = []
    for resSeg in resSegments:
        if isIntesected(inSeg, resSeg): 
            toBeMergedSegments.append(resSeg)

    if len(toBeMergedSegments) == 0: # No intesection to any result segments
        resSegments.append(inSeg)
    else: # There is intersection
        # remove toBeMerged from resultSegments
        for seg in toBeMergedSegments:
            resSegments.remove(seg)
        resSegments.append(merge(toBeMergedSegments, inSeg))

# Find the result(maxSeg, maxIdel) from result segments
resSegments = sorted(resSegments, key=lambda x: x[0])
maxSeg = max(resSegments, key=lambda x: x[1] - x[0])

maxIdle = 0
for i in range(len(resSegments) - 1):
    if seg[i + 1][0] - seg[1] > maxIdle:
        maxIdle = seg[i + 1][0] - seg[1]

# Write output
with open("Section 1.2/milk2/milk2.out", 'w') as fOutput:
    fOutput.write(str(maxSeg) + " " + str(maxIdle) + "\n")


    
    


