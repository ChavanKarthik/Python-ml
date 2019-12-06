import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBClassifier

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
# print(X.info())
Y = training_df.iloc[:, -1:]
# print(Y.info())

# 0.2 test_size means 20% of training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

# Evaluating model performance with different models
# Results = pd.DataFrame({'Model': [], 'ROC Score': []})
#
# # Decision Tree Classifier
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
#
# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_pred, y_test)
# roc_auc = auc(false_positive_rate, true_positive_rate)
#
# res = pd.DataFrame({'Model': ['DecisionTreeClassifier'],
#                     'ROC Score': roc_auc})
# Results = Results.append(res)
#
#
# # Random Forest Classifier
# model = RandomForestClassifier(n_estimators=2500, max_depth=4)
# model.fit(X_train, y_train.values.ravel())
# y_pred = model.predict(X_test)
#
# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_pred, y_test)
# roc_auc = auc(false_positive_rate, true_positive_rate)
#
# res = pd.DataFrame({'Model': ['RandomForestClassifier'],
#                     'ROC Score': roc_auc})
#
# Results = Results.append(res)
#
#
# # KNeighbors Classifier
# model = KNeighborsClassifier()
# model.fit(X_train, y_train.values.ravel())
# y_pred = model.predict(X_test)
#
# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_pred, y_test)
# roc_auc = auc(false_positive_rate, true_positive_rate)
#
# res = pd.DataFrame({'Model': ['KNeighborsClassifier'],
#                     'ROC Score': roc_auc})
# Results = Results.append(res)
#
#
# # SVM
# model = SVC(gamma='scale')
# model.fit(X_train, y_train.values.ravel())
# y_pred = model.predict(X_test)
#
# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_pred, y_test)
# roc_auc = auc(false_positive_rate, true_positive_rate)
#
# res = pd.DataFrame({'Model': ['SVM'],
#                     'ROC Score': roc_auc})
# Results = Results.append(res)
#
#
# # Logistic Regression
# model = LogisticRegression(solver='lbfgs')
# model.fit(X_train, y_train.values.ravel())
# y_pred = model.predict(X_test)
#
# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_pred, y_test)
# roc_auc = auc(false_positive_rate, true_positive_rate)
#
# res = pd.DataFrame({'Model': ['LogisticRegression'],
#                     'ROC Score': roc_auc})
# Results = Results.append(res)


# xgboost classifier
model = XGBClassifier(learning_rate=0.001, n_estimators=2500, max_depth=4, min_child_weight=0, gamma=0,
                      subsample=0.7, colsample_bytree=0.7, scale_pos_weight=1, seed=27, reg_alpha=0.00006)
# model.fit(X_train, y_train.values.ravel())
# y_pred = model.predict(X_test)

# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_pred, y_test)
# roc_auc = auc(false_positive_rate, true_positive_rate)
#
# res = pd.DataFrame({'Model': ['XGBClassifier'], 'ROC Score': roc_auc})
# Results = Results.append(res)

# print(Results)
#                     Model  ROC Score
#  DecisionTreeClassifier   0.813933
#  RandomForestClassifier        NaN
#    KNeighborsClassifier   0.695748
#                     SVC        NaN
#      LogisticRegression   0.680807
#            XGBClassifier   0.828770
# XGBClassifier simply outperforms this use-case

model.fit(X, Y.values.ravel())
y_predictions = model.predict(test_data_df).astype(int)
np.savetxt('/home/beehyv/Downloads/python/Coupon_redemption_prediction/submission01.csv', y_predictions, delimiter=',')

submission_data = pd.read_csv('/home/beehyv/Downloads/python/Coupon_redemption_prediction/submission01.csv',
                              low_memory=False)
submission_data['id'] = test_data_ids
# print(submission_data.describe())
submission_data['redemption_status'] = submission_data.iloc[:, 0:1]
# print(submission_data.describe())
submission_data = submission_data[['id', 'redemption_status']]
# print(submission_data.describe())
# print(submission_data.info())
# print(submission_data.columns.values)
submission_data.to_csv("submission1.csv", index=False)

# submission_data = pd.DataFrame({'id': test_data_ids, 'redemption_status': y_predictions})
# "Shape of passed values is {0}, indices imply {1}".format(passed, implied)
# ValueError: Shape of passed values is (1, 2), indices imply (50226, 2)
# submission_data = pd.concat([test_data_ids, y_predictions], axis=1)
# submission_data.to_csv("submission01.csv", index=False)
