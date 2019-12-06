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

# group by sex and then find median in each category
# print(df.groupby(['Sex']).Age.median())

# group by P_class and find median of age and fare
# print(df.groupby(['Pclass'])['Age', 'Fare'].median())

# diff aggregate function on multiple columns with
# print(df.groupby('Pclass').agg({'Age': 'mean', 'Fare': 'median'}))


# print(df.groupby(['Pclass', 'Sex']).Age.median())
