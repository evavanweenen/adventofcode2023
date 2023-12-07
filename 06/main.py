import numpy as np 

# --------------- part A
data = {}
with open('input.txt') as f:
    for line in f:
        key, value = line.split(':')
        value = [int(v) for v in value.rstrip('\n').split()]
        data[key] = value

n = []
for time, record in zip(*data.values()):
    distance = np.array([(time - hold) * hold for hold in range(time)])
    n.append(len(distance[distance > record]))
print(np.prod(n))

# --------------- part B
data = {}
with open('input.txt') as f:
    for line in f:
        key, value = line.split(':')
        data[key] = int(value.rstrip('\n').replace(' ', ''))

time, record = data.values()
n = int(np.floor(np.sqrt(time**2 - 4*record)))
print(n)