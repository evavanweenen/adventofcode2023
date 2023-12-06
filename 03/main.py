import pandas as pd 

df = pd.read_csv('input.txt', delimiter=None, dtype=str, header=None)[0]
df = df.apply(lambda x: list(x)).apply(pd.Series)
df = df.replace('.','')

sym = df.apply(lambda x: x.str.match('\D'))
num = df.apply(lambda x: x.str.match('\d'))

def check_neighbours(df:pd.DataFrame, i, j)->bool:
    # check top
    if i != 0:
        if df.loc[i-1, j]: # top middle
            return (i-1, j)
        if j != 0: 
            if df.loc[i-1, j-1]: # top left
                return (i-1, j-1)
        if j != df.columns[-1]: 
            if df.loc[i-1, j+1]: # top right
                return (i-1, j+1)
    
    # check middle
    if j != 0: 
        if df.loc[i, j-1]: # middle left
            return (i, j-1)
    if j != df.columns[-1]: 
        if df.loc[i, j+1]: # middle right
            return (i, j+1)

    # check bottom
    if i != df.index[-1]: 
        if df.loc[i+1, j]: # bottom middle
            return (i+1, j)
        if j != 0: 
            if df.loc[i+1, j-1]: # bottom left
                return (i+1, j-1)
        if j != df.columns[-1]: 
            if df.loc[i+1, j+1]: # bottom right
                return (i+1, j+1)
    return False

# --------------- part A
number_list = []

for i in num.index:
    num_start = False
    keep_num = False
    for j in num.columns:
        if num.loc[i][j]:
            if not num_start: # identify start of a number
                num_start = True
                number = ''
            number += df.loc[i][j]
            
            if not keep_num: # only check neighbours if still False
                keep_num = check_neighbours(sym, i, j)

            if j == num.columns[-1] and keep_num:
                number_list.append(int(number))

        else:
            if keep_num:
                number_list.append(int(number))

            keep_num = False
            num_start = False

print(sum(number_list))

# --------------- part B
ast = df == '*'
ast_xy = ast.stack()
ast_xy = ast_xy[ast_xy]
ast_xy = ast_xy.apply(lambda x: [])

for i in num.index:
    ref_ast = False
    num_start = False
    for j in num.columns:
        if num.loc[i][j]:
            if not num_start: # identify start of a number
                num_start = True
                number = ''
            number += df.loc[i][j]
            
            if not ref_ast: # only check neighbours if still False
                ref_ast = check_neighbours(ast, i, j)

            if j == num.columns[-1] and ref_ast:
                ast_xy.loc[ref_ast].append(int(number))

        else:
            if ref_ast:
                ast_xy.loc[ref_ast].append(int(number))

            ref_ast = False
            num_start = False

ast_xy = ast_xy.apply(pd.Series)
ast_xy = ast_xy.dropna()
print((ast_xy[0] * ast_xy[1]).sum())