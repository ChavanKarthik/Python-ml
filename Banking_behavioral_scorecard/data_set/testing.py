import numpy as np
import pandas as pd

df = pd.DataFrame([[1, 2, 6, 0, 'male'],
                   [2, 4, np.nan, 1, 'female'],
                   [3, 6, 4, 5, 'male'],
                   [3, 6, 4, 5, 'male'],
                   [3, 6, 4, 5, 'male'],
                   [1, 1, 5, np.nan, 'male'],
                   [1, 1, 5, np.nan, 'male']
                   ],
                  columns=list('ABCDE'))

# print(df.groupby('A')['B','C'].product())
# dataframe.mode()['Column'][0]

# mode_df = df.mode()['A'][0]
# print(mode_df)
# df = df.replace(np.nan, ' ', regex=True)
df['test'] = df[['A', 'E']].groupby('E').transform('nunique')
# print(df['test'])
print(df)
# print(df.groupby('A').prod())
# print(df.groupby('A')['B', 'C'].sum())
# print(df.groupby('A')['B', 'C'].prod())
# df['new_col'] = 5
# test = df['new_col']
# df.insert(1, 'Col2', 999)
# print(df.iloc[:, :-1])
# df = df.iloc[:, 1:-1]
# print(df.iloc[:, 2:3].columns())
# columns = df.columns.values.tolist()
# training_df = df[df['A'] != 3]
# print(df)
