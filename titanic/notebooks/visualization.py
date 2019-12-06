import os

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

# to get a histogram
# plt.hist(df.Age, bins=8, color='c')
# plt.title('Histogram : Age')
# plt.xlabel('Bins')
# plt.ylabel('Age_Value')
# plt.show()

# (1, 3) sub-plots in a single plot
# f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
# ax1.hist(df.Age, bins=20, color='c')
# ax1.set_title('Histogram : Age')
# ax1.set_xlabel('Bins')
# ax1.set_ylabel('Age_Value in years')
#
# ax2.hist(df.Fare, bins=20, color='b')
# ax2.set_title('Histogram : Fare')
# ax2.set_xlabel('Bins')
# ax2.set_ylabel('Fare_Value')
#
# ax3.hist(df.Pclass, bins=20, color='g')
# ax3.set_title('Histogram : Pclass')
# ax3.set_xlabel('Bins')
# ax3.set_ylabel('Passenger class')
#
# plt.show()

# multiple subplots :
# f, ax_arr = plt.subplots(2, 3, figsize=(15, 5))
#
# # plot 1
# ax_arr[0, 0].hist(df.Age, bins=20, color='y')
# ax_arr[0, 0].set_title('Histogram : Age')
# ax_arr[0, 0].set_xlabel('Bins')
# ax_arr[0, 0].set_ylabel('Age in years')
#
# # plot 2
# ax_arr[0, 1].hist(df.Fare, bins=20, color='g')
# ax_arr[0, 1].set_title('Histogram : Fare')
# ax_arr[0, 1].set_xlabel('Bins')
# ax_arr[0, 1].set_ylabel('Fare')
#
# # plot 3
# ax_arr[0, 2].boxplot(df.Fare.values)
# ax_arr[0, 2].set_title('Boxplot : Fare')
# ax_arr[0, 2].set_xlabel('Bins')
# ax_arr[0, 2].set_ylabel('Fare')
#
# # plot 4
# ax_arr[1, 0].boxplot(df.Age.values)
# ax_arr[1, 0].set_title('Boxplot : Age')
# ax_arr[1, 0].set_xlabel('Bins')
# ax_arr[1, 0].set_ylabel('Age in years')
#
# # plot 5
# ax_arr[1, 1].scatter(df.Age, df.Fare, color='c', alpha=0.15)
# ax_arr[1, 1].set_title('Scatter plot : Age')
# ax_arr[1, 1].set_xlabel('Age')
# ax_arr[1, 1].set_ylabel('Fare')
#
# # to hide any plot to not execute
# ax_arr[1, 2].axis('off')
#
# # To eliminate over_lapping
# plt.tight_layout()
#
# plt.show()
