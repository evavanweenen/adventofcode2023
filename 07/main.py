import pandas as pd
import numpy as np

# --------------- part A
card_order = {x: i for i, x in enumerate(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1])}
type_order = {x: i for i, x in enumerate(['5K', '4K', 'FH', '3K', '2P', '1P', 'H'][::-1])}

def get_type(hand:str)->str:
    _, counts = np.unique(list(hand), return_counts=True)
    if np.max(counts) == 5:
        return '5K'
    elif np.max(counts) == 4:
        return '4K'
    elif np.max(counts) == 3:
        if len(counts) == 2:
            return 'FH'
        elif len(counts) == 3:
            return '3K'
    elif np.max(counts) == 2:
        if len(counts) == 3:
            return '2P'
        elif len(counts) == 4:
            return '1P'
    else:
        return 'H'

df = pd.read_csv('input.txt', header=None, sep=' ', names=['hand', 'bid'])
df['type'] = df['hand'].apply(get_type)
for n in range(5):
    df[f'card{n+1}'] = df['hand'].str[n]
df = df.sort_values(by=['type']+[f'card{n+1}'for n in range(5)], key=lambda x: x.map(dict(**card_order, **type_order)))
df = df.reset_index(drop=True)

df['rank'] = df.index+1
df['score'] = df['bid'] * df['rank']
print(df['score'].sum())

# --------------- part B
card_order = {x: i for i, x in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1])}

def get_type(hand:str)->str:
    njoker = np.sum(np.array(list(hand)) == 'J')
    jokerless = [h for h in list(hand) if h != 'J']
    _, counts = np.unique(jokerless, return_counts=True)

    if njoker == 0:
        if np.max(counts) == 5:
            return '5K'
        elif np.max(counts) == 4:
            return '4K'
        elif np.max(counts) == 3:
            if len(counts) == 2:
                return 'FH'
            elif len(counts) == 3:
                return '3K'
        elif np.max(counts) == 2:
            if len(counts) == 3:
                return '2P'
            elif len(counts) == 4:
                return '1P'
        else:
            return 'H'

    elif njoker == 1:
        if np.max(counts) == 4:
            return '5K'
        elif np.max(counts) == 3:
            return '4K'
        elif np.max(counts) == 2:
            if len(counts) == 2:
                return 'FH'
            elif len(counts) == 3:
                return '3K'
        else:
            return '1P'

    elif njoker == 2:
        if np.max(counts) == 3:
            return '5K'
        elif np.max(counts) == 2:
            return '4K'
        else:
            return '3K'

    elif njoker == 3:
        if np.max(counts) == 2:
            return '5K'
        else:
            return '4K'

    else:
        return '5K'

df = pd.read_csv('input.txt', header=None, sep=' ', names=['hand', 'bid'])
df['type'] = df['hand'].apply(get_type)
for n in range(5):
    df[f'card{n+1}'] = df['hand'].str[n]
df = df.sort_values(by=['type']+[f'card{n+1}'for n in range(5)], key=lambda x: x.map(dict(**card_order, **type_order)))
df = df.reset_index(drop=True)

df['rank'] = df.index+1
df['score'] = df['bid'] * df['rank']
print(df['score'].sum())