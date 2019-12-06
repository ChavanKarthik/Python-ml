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

# print(df[df.Embarked.isnull()])
# to get distinct values and there counts
# print(df.Embarked.value_counts())

# impute the missing values with s
df.Embarked.fillna('C', inplace=True)

# cross-check fillna function
# print(df[df.Embarked.isnull()])


median_fare = df.loc[(df.Pclass == 3) & (df.Embarked == 'S')].median()
# print(median_fare[1])
df.Fare.fillna(median_fare[1], inplace=True)

# print(df.loc[df['PassengerId'].isin('1044')])
pd.options.display.max_rows = 10
(df[df.Age.isnull()])

# to get the median age
median_age = df.Age.median()

# print(df.groupby('Sex').Age.median())
# filling the missing data
df.Age.fillna(median_age, inplace=True)
# print(df.info())
