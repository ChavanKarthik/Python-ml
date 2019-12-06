import os

import pandas as pd

# set path for data files

raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')
train_data_file_path = os.path.join(raw_data_path, 'train.csv')
test_data_file_path = os.path.join(raw_data_path, 'test.csv')

# read raw data with pandas and index PassengerId(primary key)
train_df = pd.read_csv(train_data_file_path, index_col='PassengerId')
test_df = pd.read_csv(test_data_file_path, index_col='PassengerId')

# to know type of dataframe
# print(type(train_df))

# basic information abt dataframe(df)
# print(train_df.info())

# adding a new column
test_df['Survived'] = -123

# to club two df data into one
df = pd.concat((train_df, test_df), axis=0, sort=False)
# print(df.info())

# to get first 5 rows with headers
# print(df.head(5))

# to get last 5 rows with headers
# print(df.tail(5))

# to get specific columns data with primary key
# print(df[['Name']])
# print(df.Name)

# To return distinct values
# print(df.drop_duplicates(subset=['Sex', 'Age']))

# print(df.groupby(['Sex', 'Survived']).count())

# To return not null values
# print(df[df.Cabin.notnull()])

# To return null values
# print(df[df.Cabin.isnull()])

# label based indexing :
# to get records from 6 to 9 all columns
# print(df.loc[6:9])

# to get records from 2 to 5 and Age to Fare columns
# print(df.loc[2:5, 'Age':'Fare'])

# to get specific columns
# print(df.loc[8:15, ['Age', 'Fare', 'Sex']])

# position based indexing :
# to get rows and columns on index base
# print(df.iloc[2:5, 0:3])

# filter rows based on condition(where)
males = df.loc[df.Sex == 'male', :]
# print(len(males))

# to filter with multiple conditions
males_1st_class = df.loc[((df.Sex == 'male') & (df.Pclass == 1)), :]
# print(len(males_1st_class))

# to get brief stats abt all numerical columns
# print(df.describe())

# print(df.Age.mean())  # for mean
# print(df.Age.median())  # for median
# print((df.Age.max())-df.Age.min())  # for range
# print(df.Age.quantile(0.25))  # for 25 quartile
# print(df.Age.quantile(0.5))  # for 50 quartile
# print(df.Age.quantile(0.75))  # for 75 quartile
# print(df.Age.var())  # for variance
# print(df.Age.std())  # for standard deviation

# df.Fare.plot(kind='box')  # make a box plt
# plt.show()  # visualize

# print(df.describe(include='all'))  # describe including categorical columns

# print(df.Sex.value_counts())  # group by Sex column with counts
# print(df.Sex.value_counts(normalize='True'))  # group by Sex column in %'s
# print(df.Pclass.value_counts().plot(kind='bar'))  # bar plot 'Pclass' column with counts
# plt.show()
