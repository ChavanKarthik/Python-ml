import os

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

file_train_data = os.getcwd() + '/cleaned_data/train.csv'
file_test_data = os.getcwd() + '/cleaned_data/test.csv'

train_df = pd.read_csv(file_train_data, low_memory=False)
test_df = pd.read_csv(file_test_data, low_memory=False)

# replace all empty spaces with nan
train_df = train_df.replace('', np.nan, regex=True)
test_df = test_df.replace('', np.nan, regex=True)
# print(train_df.info()) # 78369 records
# print(test_df.info())  # 50226 records

# fill null values of train_df with mode of individual column values
age_range_mode_df = train_df.mode()['age_range'][0]
is_married_mode_df = train_df.mode()['is_married'][0]
rented_mode_df = train_df.mode()['rented'][0]
family_size_mode_df = train_df.mode()['family_size'][0]
income_bracket_categorized_mode_df = train_df.mode()['income_bracket_categorized'][0]

# replacing the null values
train_df['age_range'] = train_df.age_range.replace(np.NaN, age_range_mode_df)
train_df['is_married'] = train_df.is_married.replace(np.NaN, is_married_mode_df)
train_df['rented'] = train_df.rented.replace(np.NaN, rented_mode_df)
train_df['family_size'] = train_df.family_size.replace(np.NaN, family_size_mode_df)
train_df['income_bracket_categorized'] = train_df.income_bracket_categorized.replace(np.NaN,
                                                                                     income_bracket_categorized_mode_df)

# fill null values of test_df
percent_redeemed_on_coupin_id_mode = test_df.mode()['percent_redeemed_on_coupin_id'][0]
percent_redeemed_on_customer_id_mode = test_df.mode()['percent_redeemed_on_customer_id'][0]
age_range_mode = test_df.mode()['age_range'][0]
is_married_mode = test_df.mode()['is_married'][0]
rented_mode = test_df.mode()['rented'][0]
family_size_mode = test_df.mode()['family_size'][0]
income_bracket_categorized_mode = test_df.mode()['income_bracket_categorized'][0]

# replacing the null values
test_df['percent_redeemed_on_coupin_id'] = test_df.percent_redeemed_on_coupin_id.replace(np.NaN,
                                                                                         percent_redeemed_on_coupin_id_mode)
test_df['percent_redeemed_on_customer_id'] = test_df.percent_redeemed_on_customer_id.replace(np.NaN,
                                                                                             percent_redeemed_on_customer_id_mode)
test_df['age_range'] = test_df.age_range.replace(np.NaN, age_range_mode)
test_df['is_married'] = test_df.is_married.replace(np.NaN, is_married_mode)
test_df['rented'] = test_df.rented.replace(np.NaN, rented_mode)
test_df['family_size'] = test_df.family_size.replace(np.NaN, family_size_mode)
test_df['income_bracket_categorized'] = test_df.income_bracket_categorized.replace(np.NaN,
                                                                                   income_bracket_categorized_mode)
# print(train_df.info())
# print(test_df.info())

# separate test data first column (id) column and save it and remove it
test_data_ids = test_df.iloc[:, 0:1]
del test_df['id']
# print(test_data_ids.info())
# print(test_df.columns.values == train_df.columns.values)

# concat test and train data in one df for feature engineering
df = pd.concat([train_df, test_df], axis=0, ignore_index=True, sort=False)

df['percent_redeemed_on_coupin_id'] = df.percent_redeemed_on_coupin_id.astype(int)
df['percent_redeemed_on_customer_id'] = df.percent_redeemed_on_customer_id.astype(int)
df['avg_transaction'] = df.avg_transaction.astype(int)
df['is_married'] = df.is_married.astype(int)
df['rented'] = df.rented.astype(int)
# print(df.info())
# print(df.columns.values)

df = pd.get_dummies(df, prefix=['age_range', 'family_size', 'income_bracket_categorized'],
                    columns=['age_range', 'family_size', 'income_bracket_categorized'])
# print(df.info())
# column_titles = df.columns.values

column_titles = ['percent_redeemed_on_coupin_id', 'percent_redeemed_on_customer_id', 'avg_transaction',
                 'frequency_of_visit', 'age_on_service', 'is_married', 'rented', 'age_range_18-25', 'age_range_26-35',
                 'age_range_36-45', 'age_range_46-55', 'age_range_56-70', 'age_range_70+', 'family_size_1',
                 'family_size_2', 'family_size_3', 'family_size_4', 'family_size_5+',
                 'income_bracket_categorized_eight',
                 'income_bracket_categorized_eleven', 'income_bracket_categorized_five',
                 'income_bracket_categorized_four',
                 'income_bracket_categorized_nine', 'income_bracket_categorized_one',
                 'income_bracket_categorized_seven',
                 'income_bracket_categorized_six', 'income_bracket_categorized_ten', 'income_bracket_categorized_three',
                 'income_bracket_categorized_twelve', 'income_bracket_categorized_two', 'redemption_status']

df = df.reindex(columns=column_titles)
# print(df.info())

# separate training data from training
training_df = df[df['redemption_status'] != 123]
# print(training_df.info())


# separate testing data from training
test_data_df = df[df['redemption_status'] == 123]
del test_data_df['redemption_status']
# print(test_data_df.info())

X = training_df.iloc[:, :-1]
print(X.info())
Y = training_df.iloc[:, -1:]
# Y = Y.ravel()
print(Y.info())

# smt = SMOTE(random_state=42, ratio=1.0)
# X_re_sampled, Y_re_sampled = smt.fit_sample(X, Y)
#
# Decision Tree Classifier
model = DecisionTreeClassifier(max_depth=4)
model.fit(X, Y)

y_predictions = model.predict(test_data_df).astype(int)
np.savetxt('/home/beehyv/Downloads/python/Coupon_redemption_prediction/submission02.csv', y_predictions, delimiter=',')

submission_data = pd.read_csv('/home/beehyv/Downloads/python/Coupon_redemption_prediction/submission02.csv',
                              low_memory=False)
submission_data['id'] = test_data_ids
# print(submission_data.describe())
submission_data['redemption_status'] = submission_data.iloc[:, 0:1]
# print(submission_data.describe())
submission_data = submission_data[['id', 'redemption_status']]
# print(submission_data.describe())
# print(submission_data.info())
# print(submission_data.columns.values)
submission_data.to_csv("submission2.csv", index=False)
