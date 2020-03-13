with open('traffic.in') as input:
    lines = input.readlines()
    N = int(lines[0].strip())

traffic = []
for i in range(1, N+1):
    ramp, mi, ma = lines[i].strip().split()
    mi = int(mi)
    ma = int(ma)
    traffic.append([ramp, mi, ma])

before = [0,0]
after = [0,0]

for i in range(len(traffic)):
    

1==1



