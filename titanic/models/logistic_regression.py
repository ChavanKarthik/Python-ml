# import all needful libraries
import os

import pandas as pd

# import processed data
processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
train_file_path = os.path.join(processed_data_path, 'train.csv')
test_file_path = os.path.join(processed_data_path, 'test.csv')

train_df = pd.read_csv(train_file_path, index_col='PassengerId')
test_df = pd.read_csv(test_file_path, index_col='PassengerId')

# print(train_df.info())
# print(test_df.info())

# Data Preparation
X = train_df.loc[:, 'Age':].as_matrix().astype('float')
y = train_df['Survived'].ravel()

# print(X.shape, y.shape)

from sklearn.model_selection import train_test_split

# Train and test data split from training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

from sklearn.dummy import DummyClassifier

# create model
model_dummy = DummyClassifier(strategy='most_frequent', random_state=0)

# train model
model_dummy.fit(X_train, y_train)

# print(f'Accuracy for baseline model : {model_dummy.score(X_test, y_test)}')

# performance metrics

# print(f'Accuracy for baseline model : {accuracy_score(y_test, model_dummy.predict(X_test) )}')
# print(f'Accuracy for baseline model : {confusion_matrix(y_test, model_dummy.predict(X_test) )}')
# print(f'Accuracy for baseline model : {precision_score(y_test, model_dummy.predict(X_test) )}')
# print(f'Accuracy for baseline model : {recall_score(y_test, model_dummy.predict(X_test) )}')

# import logistic regression from sklearn
from sklearn.linear_model import LogisticRegression

# create model
model_lr1 = LogisticRegression(C=3.0, penalty='l2')

# train model
model_lr1.fit(X_train, y_train)

prediction = model_lr1.predict(test_df)

prediction = pd.DataFrame(prediction, columns=[['Survived']]).to_csv('prediction.csv')

# evaluate model
# print(f'score for logistic regression : {model_lr1.score(X_test, y_test)}')

# Hyper-parameter optimization
from sklearn.model_selection import GridSearchCV

parameters = {'C': [1.0, 2.0, 3.0, 4.0, 5.0, 10.0], 'penalty': ['l1', 'l2']}
clf = GridSearchCV(model_lr1, param_grid=parameters, cv=5)

clf.fit(X_train, y_train)
# print(clf.best_params_)

# def get_submission_file(clf, filename):
#     submission_file_data_path = os.path.join(os.path.pardir, 'data', 'submission')
#     write_file_path = os.path.join(submission_file_data_path, 'train.csv')


# Feature Normalization
from sklearn.preprocessing import MinMaxScaler

scalar = MinMaxScaler()
X_train_scaled = scalar.fit_transform(X_train)

# check minimum and maximum values
# print(X_train_scaled[:, 0].min(), X_train_scaled[:, 0].max())

X_test_scaled = scalar.fit_transform(X_test)

# create new model with standardised data

model_lr2 = LogisticRegression()
parameters = {'C': [1.0, 2.0, 3.0, 4.0, 5.0, 10.0], 'penalty': ['l1', 'l2']}
clf = GridSearchCV(model_lr1, param_grid=parameters, cv=3)

clf.fit(X_train, y_train)
# print(clf.best_score_)
# predictions2 = clf.predict(test_df)
