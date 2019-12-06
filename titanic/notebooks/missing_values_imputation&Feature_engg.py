import os

import numpy as np
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

# print(df.Embarked.value_counts())
# imputing missing values with mode in that column
df.Embarked.fillna('S', inplace=True)

# print(df[df.Fare.isnull()])
# Declare variable with for missing fare
median_fare = df.loc[(df.Pclass == 3) & (df.Embarked == 'S'), 'Fare'].median()
df.Fare.fillna(median_fare, inplace=True)

# setting limit on result set rows
pd.options.display.max_rows = 10


# print(df[df.Age.isnull()])
# print(df.Name.map(lambda x: GetTitle(x)).unique())
# title is relevant feature of age
# function to extract title from name and categorize them
def GetTitle(name):
    title_group = {'mr': 'Mr',
                   'mrs': 'Mrs',
                   'miss': 'Miss',
                   'master': 'Master',
                   'don': 'Sir',
                   'rev': 'Sir',
                   'dr': 'Officer',
                   'mme': 'Mrs',
                   'ms': 'Mrs',
                   'major': 'Officer',
                   'lady': 'Lady',
                   'sir': 'Sir',
                   'mlle': 'Miss',
                   'col': 'Officer',
                   'capt': 'Officer',
                   'the countess': 'Lady',
                   'jonkheer': 'Sir',
                   'dona': 'Lady',
                   }
    first_name_with_title = name.split(',')[1]
    title = first_name_with_title.split('.')[0]
    title = title.strip().lower()
    return title_group[title]


# adds new column 'title' to impute their titles
df['Title'] = df.Name.map(lambda x: GetTitle(x))

median_age = df.groupby('Title').Age.transform('median')
df.Age.fillna(median_age, inplace=True)

# histogram for fare
# df.Fare.plot(kind='hist', title='Histogram of Fare', bins=20, color='c')
# df.Fare.plot(kind='box')
# plt.show()

# Explore more into outliers
# print(df.loc[df.Fare == df.Fare.max()])
# treat outliers of fare to reduce skewness by log transformations

Log_Fare = np.log(df.Fare + 1.0)
# Adding 1 to accommodate zero fares : log(0) is not defined

# checking if transformation reduces skewness
# Log_Fare.plot(kind='hist', bins=20, color='c')
# plt.show()

# binning the fare into four categories
# pd.qcut(df.Fare, 4, labels=['very_low', 'low', 'high', 'very_high'])  # discretization

# create fare bin feature
df['Fare_Bin'] = pd.qcut(df.Fare, 4, labels=['very_low', 'low', 'high', 'very_high'])

# Age_state based on Age
df['Age_State'] = np.where(df['Age'] >= 18, 'Adult', 'Child')
# print(df['Age_State'].value_counts())

# Family size feature
df['Family_Size'] = df.Parch + df.SibSp + 1  # 1 for self
# print(pd.crosstab(df[df.Survived != -123].Survived, df[df.Survived != -123].Family_Size))

# is mother feature

df['Is_Mother'] = np.where(((df.Sex == 'female') & (df.Parch > 0) & (df.Age > 18) & (df.Title != 'Miss')), 1, 0)
# print(pd.crosstab(df[df.Survived != -123].Survived, df[df.Survived != -123].Is_Mother))

# print(df.Cabin.unique())
# replace odd cabin number to NaN
df.loc[df.Cabin == 'T', 'Cabin'] = np.NaN


def get_deck(Cabin):
    return np.where(pd.notnull(Cabin), str(Cabin)[0].upper(), 'Z')


df['Deck'] = df['Cabin'].map(lambda x: get_deck(x))
# print(pd.crosstab(df[df.Survived != -123].Survived, df[df.Survived != -123].Deck))

# categorical feature for Sex
df['Is_Male'] = np.where(df.Sex == 'male', 1, 0)

# get_dummies does self categorical feature
df = pd.get_dummies(df, columns=['Deck', 'Pclass', 'Title', 'Fare_Bin', 'Embarked', 'Age_State'])

# Dropping unnecessary columns
df.drop(['Cabin', 'Name', 'Ticket', 'Parch', 'SibSp', 'Sex'], axis=1, inplace=True)

# Reordering columns
columns = [column for column in df.columns if column != 'Survived']
columns = ['Survived'] + columns
df = df[columns]

# save the processed train data and test data
processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
write_train_path = os.path.join(processed_data_path, 'train.csv')
write_test_path = os.path.join(processed_data_path, 'test.csv')

# train data
df.loc[df.Survived != -123].to_csv(write_train_path)
# test data
columns = [column for column in df.columns if column != 'Survived']
df.loc[df.Survived == -123, columns].to_csv(write_test_path)

# print(df.info())
# print(df.head())
print(df.describe())
