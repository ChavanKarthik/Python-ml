# import all needful libraries
import os

import pandas as pd

# import processed data
processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
train_file_path = os.path.join(processed_data_path, 'train.csv')
test_file_path = os.path.join(processed_data_path, 'test.csv')

train_df = pd.read_csv(train_file_path, index_col='PassengerId')
test_df = pd.read_csv(test_file_path, index_col='PassengerId')

# Data Preparation
X = train_df.loc[:, 'Age':].as_matrix().astype('float')
y = train_df['Survived'].ravel()

from sklearn.model_selection import train_test_split

# Train and test data split from training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.neighbors import KNeighborsClassifier

k_neighbor = KNeighborsClassifier()
k_neighbor.fit(X_train, y_train)
# Predictions_rfc = k_neighbor.predict(X_test)
# print(k_neighbor.score(X_train, y_train))
Predictions_rfc = k_neighbor.predict(test_df)
pd.DataFrame(Predictions_rfc, columns=[['Survived']]).to_csv('predictions_knnc.csv')
