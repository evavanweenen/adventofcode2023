import pandas as pd 

df = pd.read_csv('input.txt', header=None, names=['input'])

# --------------- part A
df['numA'] = df['input'].str.replace('\D+', '', regex=True)

print((df['numA'].apply(lambda x: x[0])+
       df['numA'].apply(lambda x: x[-1])).astype(int).sum())

# --------------- part B
repl = {'one' : 'o1e',
        'two' : 't2o',
        'three' : 't3e',
        'four' : 'f4r',
        'five' : 'f5e',
        'six' : 's6x',
        'seven' : 's7n',
        'eight' : 'e8t',
        'nine' : 'n9e'}

df['repl'] = df['input']
for k, v in repl.items():
    df['repl'] = df['repl'].str.replace(f'({k})', v, regex=True)

df['numB'] = df['repl'].str.replace('\D+', '', regex=True)

print((df['numB'].apply(lambda x: x[0])+
       df['numB'].apply(lambda x: x[-1])).astype(int).sum())