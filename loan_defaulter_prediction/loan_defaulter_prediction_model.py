import os

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier

train_data_file_path = os.getcwd() + '/train.csv'
test_data_file_path = os.getcwd() + '/test.csv'

train_df = pd.read_csv(train_data_file_path)
test_df = pd.read_csv(test_data_file_path)

# add dummy feature to make it similar to training data
test_df['m13'] = 'test_data'

# concat test and train data in one df for feature engg
df = pd.concat([train_df, test_df], axis=0, ignore_index=True, sort=False)

# print(train_df['borrower_credit_score'].sum())
# print(train_df['borrower_credit_score'].mean())

# take average of credit score when two borrowers
df['borrower_credit_score'] = np.where((df['number_of_borrowers'] > 1), (
        df['co-borrower_credit_score'] + df['borrower_credit_score']) / 2,
                                       df['borrower_credit_score'])

# Remove the users whose credit score is null
df = df[(df.borrower_credit_score != 0)]

# Change the date format as origination date format
df['first_payment_date'] = pd.to_datetime(df['first_payment_date'], errors='coerce')
df['origination_date'] = pd.to_datetime(df['origination_date'], errors='coerce')

# remove extra spaces in column names
df.columns = df.columns.str.strip()
# print(df.columns)

# set the date format of both the columns into one format
# df['first_payment_date'] = df.first_payment_date.str.cat('01/', )

df2 = df['first_payment_date']
df3 = df['origination_date']
# find gap between origination date and first payment
df['Months_Gap'] = round((df2 - df3) / np.timedelta64(1, 'M'), 0)
# print(df.info())
df['Months_Gap'] = df['Months_Gap'].astype(int)
df['interest_rate'] = df['interest_rate'].astype(int)
# print(df.info())

# feature engg by insurance_type, insurance-%
df['Insured_by_user'] = np.where((df['insurance_percent'] > 0) & (df['insurance_type'] == 0), 1, 0)
df['Insured_by_bank'] = np.where((df['insurance_percent'] > 0) & (df['insurance_type'] == 1), 1, 0)
df['Is_Insured'] = np.where((df['insurance_percent'] == 0), 1, 0)

# put loan_to_value into bins
bins = [0, 20, 40, 60, 80, 100]
labels = ['very_less', 'less', 'medium', 'high', 'very_high']
df['loan_to_value_binned'] = pd.cut(df['loan_to_value'], bins, labels=labels)

# put loan_to_value into bins debt_to_income_ratio
bins1 = [0, 15, 31, 47, 65]
labels1 = ['less', 'medium', 'high', 'very_high']
df['debt_to_income_ratio_binned'] = pd.cut(df['debt_to_income_ratio'], bins1, labels=labels1)

# put loan_to_value into bins loan_term
bins2 = [0, 119, 179, 239, 359, 360]
labels2 = ['very_less', 'less', 'medium', 'high', 'very_high']
df['loan_term_binned'] = pd.cut(df['loan_term'], bins2, labels=labels2)

# put loan_to_value into bins loan_term
bins3 = [10000, 60000, 90000, 160000, 210000, 410000, 610000, 1300000]
labels3 = ['very_very_less', 'very_less', 'less', 'medium', 'high', 'very_high', 'very_very_high']
df['unpaid_principal_bal_binned'] = pd.cut(df['unpaid_principal_bal'], bins3, labels=labels3)

# put borrower_credit_score into bins loan_term
bins4 = [0, 619, 639, 669, 699, 729, 759, 779, 799, 842]
labels4 = ['very_very_less', 'very_less', 'less', 'below_avg', 'avg', 'above_avg', 'high', 'very_high',
           'very_very_high']
df['borrower_credit_score_binned'] = pd.cut(df['borrower_credit_score'], bins4, labels=labels4)

# remove unnecessary columns
df = df[['source', 'financial_institution', 'interest_rate',
         'unpaid_principal_bal_binned', 'loan_term_binned', 'Months_Gap',
         'loan_to_value_binned', 'debt_to_income_ratio_binned',
         'borrower_credit_score_binned', 'loan_purpose',
         'Insured_by_user', 'Insured_by_bank', 'Is_Insured',
         'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7',
         'm8', 'm9', 'm10', 'm11', 'm12', 'm13']]

# Reduce the df size to reduce time in processing in every iteration
# df = df[0:1000]

# train data
training_df = df.loc[df.m13 != 'test_data']

# separate test data and remove 'm13'(prediction column) after feature engg from df
columns = [column for column in df.columns if column != 'm13']
test_data_df = df.loc[df.m13 == 'test_data', columns]
test_data_df = pd.get_dummies(test_data_df)
# print(test_data_df.info())
# print(training_df.columns.values)

# separate x1, x2, ..xn columns with y1(m13)
X = (training_df.iloc[:, 0:25])

# Y = Y.astype(np.float64)
# get m13 the last column
Y = (training_df.iloc[:, 25:])
# Y = Y.astype(int)
Y = np.array(Y).astype(int)
# print(Y['m13'].value_counts())
# print(Y.describe())

X = pd.get_dummies(X)
# print(X.info())

# print('Mean of m13 before re-sampling : ', (Y.mean()))
smt = SMOTE(random_state=42, ratio=1.0)
X_re_sampled, Y_re_sampled = smt.fit_sample(X, Y)

# check whether re-sampling is done
# print('Mean of m13 after re-sampling : ', (Y_re_sampled.mean()))

# 0.2 test_size means 20%
# X_train, X_test, y_train, y_test = train_test_split(X_re_sampled, Y_re_sampled, test_size=0.2, random_state=2)

# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)
# print(np.bincount(y_train))

# # Train Logistic Regression model
# LR = LogisticRegression(random_state=0, solver='lbfgs', max_iter=500).fit(X_train, y_train)
# y_predictions = LR.predict(X_test)
# # print(round(LR.score(X_test, y_test), 4))
# print(f1_score(y_test, y_predictions, average=None))
#
# # Train SVM model
# SVM = svm.SVC(decision_function_shape="ovo", gamma='auto').fit(X_train, y_train)
# # Predict the result
# y_predictions = SVM.predict(X_test)
# # print(round(SVM.score(X_test, y_test), 4))
# print(f1_score(y_test, y_predictions, average=None))

# Train random forest model
RF = RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0).fit(X_re_sampled, Y_re_sampled)

y_predictions = RF.predict(test_data_df)
np.savetxt("predictions.csv", y_predictions, delimiter=",")

# y_predictions = y_predictions.astype('int')
# print(round(RF.score(X_test, y_test), 4))
# print(f1_score(y_test, y_predictions, average=None))
# print(y_predictions.reshape(-1, 1))
