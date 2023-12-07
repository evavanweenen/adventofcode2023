import pandas as pd
import numpy as np

data = {}
with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        if line != '':
            if len(line.split(':')) > 1:
                key, value = line.split(':')
                if value != '':
                    data[key] = [value.lstrip(' ')]
                else:
                    data[key] = []
            else:
                    data[key].append(line)

data = {k: [[int(n) for n in i.split()] for i in v] for k, v in data.items()}
data['seeds'] = data['seeds'][0]

# --------------- part A
df = pd.DataFrame(data=data['seeds'])[0]

for mapping in list(data.keys())[1:]:
    for i in df.index:
        for dest, src, rng in data[mapping]:
            if src <= df.loc[i] < src+rng:
                df.loc[i] -= (src-dest)
                break
print(df.min())

# --------------- part B
seeds = {'unmapped' : [],
         'mapped' : [[data['seeds'][i],data['seeds'][i]+data['seeds'][i+1]] \
                        for i in range(0, len(data['seeds']), 2)]}

for mapping in list(data.keys())[1:]:
    print(mapping)
    seeds['unmapped'] = seeds['mapped']
    seeds['mapped'] = []

    while len(seeds['unmapped']) > 0:
        smin, smax = seeds['unmapped'][0]
        if smin >= smax:
            del seeds['unmapped'][0]
            continue
        detected = False
        for dest, src, rng in data[mapping]:
            if src <= smin < src+rng:
                if src < smax < src+rng: # inner
                    seeds['mapped'].append([smin + dest-src, smax + dest-src])
                    del seeds['unmapped'][0]
                    detected = True; break
                else: # right
                    seeds['mapped'].append([smin + dest-src, dest+rng])
                    seeds['unmapped'][0] = [src+rng, smax]
                    detected = True; break
            elif src > smin:
                if src < smax < src+rng: # left
                    seeds['mapped'].append([dest, smax + dest-src])
                    seeds['unmapped'][0] = [smin, src]
                    detected = True; break
                elif smax >= src+rng: # outer
                    seeds['mapped'].append([dest, dest+rng])
                    seeds['unmapped'].append([smin, src])
                    seeds['unmapped'].append([src+rng, smax])
                    del seeds['unmapped'][0]
                    detected = True; break
        if not detected:
            seeds['mapped'].append(seeds['unmapped'][0])
            del seeds['unmapped'][0]

print(min(np.array(seeds['mapped'])[:,0]))