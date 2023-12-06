import pandas as pd 

df = pd.read_csv('input.txt', header=None, sep=':', names=['card', 'numbers'])
df['card'] = df['card'].str.lstrip('Card').str.strip(' ').astype(int)
df = df.set_index('card')

df = df['numbers'].apply(lambda x: x.split('|')).apply(pd.Series)
df.columns = ['win', 'own']
df['win'] = df['win'].apply(lambda x: x.split())
df['own'] = df['own'].apply(lambda x: x.split())

# --------------- part A
df['match'] = 0

for i in df.index:
    for card in df.loc[i, 'own']:
        if card in df.loc[i, 'win']:
            df.loc[i,'match'] += 1
df['score'] = df['match'].apply(lambda x: 2.**(x-1) if x != 0 else 0)
print(df['score'].sum())

# --------------- part B
df['ncards'] = 1
for i in df.index:
    n = df.loc[i, 'match']
    df.loc[i+1:i+n,'ncards'] += df.loc[i, 'ncards']
print(df['ncards'].sum())