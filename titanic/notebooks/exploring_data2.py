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
# print(df.info())

# to plot a histogram with 100 buckets in age column
# df.Age.plot(kind='hist', title='Histogram for Age column', color='g', bins=30)
# plt.show()

# to plot a KDE(Kernel distribution ) with 100 buckets in age column
# df.Age.plot(kind='kde', title='Kernel density for Age column', color='c')
# plt.show()

# print(df.Age.skew())  # to get skewness of age

# to get a graph to find proportionality
# df.plot.scatter(x='Pclass', y='Fare', color='c', title='Bi-variate plot', alpha='0.2')
# plt.show()

# print(df.groupby(['Sex']).Age.median())
