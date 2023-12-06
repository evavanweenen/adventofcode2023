import pandas as pd 
import numpy as np

def count_color(sample:list, cname:str)->int:
    for i in sample:
        if cname in i:
            return int(i.strip(f' {cname}'))
    return 0

df = pd.read_csv('input.txt', header=None, sep=':', names=['game', 'samples'])

df['game'] = df['game'].str.lstrip('Game ').astype(int)
df = df.set_index('game')

df['samples'] = df['samples'].apply(lambda samples: [[i.strip(' ') for i in sample.split(',')]\
                                                                   for sample in samples.split(";")])
df = df['samples'].apply(pd.Series)
df = df.stack().to_frame()
df.columns = ['samples']

df['red'] = df['samples'].apply(count_color, cname='red')
df['green'] = df['samples'].apply(count_color, cname='green')
df['blue'] = df['samples'].apply(count_color, cname='blue')
#df = df.drop('samples', axis=1).astype(int)

# --------------- part A
excl = (df['red'] > 12) | (df['green'] > 13) | (df['blue'] > 14)
df_A = df.drop(df[excl].index.get_level_values(0))
print(np.sum(df_A.index.get_level_values(0).unique()))

# --------------- part B
df_B = df.groupby(level=0).max()
print((df_B['red'] * df_B['green'] * df_B['blue']).sum())