import os

import pandas as pd

# set path for data files
raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')
train_data_file_path = os.path.join(raw_data_path, 'train.csv')
test_data_file_path = os.path.join(raw_data_path, 'test.csv')

# read raw data with pandas and index PassengerId(primary key)
train_df = pd.read_csv(train_data_file_path, index_col='PassengerId')
test_df = pd.read_csv(test_data_file_path, index_col='PassengerId')

# adding a new column
test_df['Survived'] = -123

# to club two df data into one
df = pd.concat((train_df, test_df), axis=0)

# print(pd.crosstab(df.Sex, df.Pclass))


# print(pd.crosstab(df.Sex, df.Pclass).plot(kind='bar'))
# plt.show()


# pivot table
# print(df.pivot_table(index='Sex', columns='Pclass', values='Age', aggfunc='mean'))


# pivot table with groupby function and unstack
# print(df.groupby(['Sex', 'Pclass']).Age.mean().unstack())
