import os

import numpy as np
import pandas as pd

# Dataframe initialization
raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')
train_data_file_path = os.path.join(raw_data_path, 'train.csv')
test_data_file_path = os.path.join(raw_data_path, 'test.csv')
train_df = pd.read_csv(train_data_file_path, index_col='PassengerId')
test_df = pd.read_csv(test_data_file_path, index_col='PassengerId')
test_df['Survived'] = -123
df = pd.concat((train_df, test_df), axis=0)
df.Embarked.fillna('C', inplace=True)
median_fare = df.loc[(df.Pclass == 3) & (df.Embarked == 'S')].median()
df.Fare.fillna(median_fare[1], inplace=True)
pd.options.display.max_rows = 10
median_age = df.Age.median()
df.Age.fillna(median_age, inplace=True)
# ===============================================

# adding a new column and filling according to age group
df['AgeState'] = np.where(df['Age'] >= 18, 'Adult', 'Child')

# print(df['AgeState'].value_counts())
# print(pd.crosstab(df[df.Survived != -123].Survived, df[df.Survived != -123].AgeState))
