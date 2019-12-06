import mysql.connector
import pandas as pd
from mysql.connector import Error
from sklearn import svm

# connect to database
try:
    mydb = mysql.connector.connect(host='localhost',
                                   user="root",
                                   passwd="beehyv123",
                                   database="titanic_data")

    select_query = ("SELECT DAYNAME(modificationDate) AS 'Day', "
                    "percentage_listened AS '%_listened', "
                    "HOUR(call_start_time) AS 'Calling_time' "
                    "FROM titanic_data.beneficiary_call_measure "
                    "where percentage_listened > 60;")

    my_cursor = mydb.cursor()
    my_cursor.execute(select_query)
    records = my_cursor.fetchall()
    my_cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)

data = [x for x in records]
# print(data)

df = pd.DataFrame(data, columns=['Day', '%_listened', 'Calling_time'])

''' binning or bucketing with labels'''
bins = [10, 12, 14, 16, 18]
labels = ['11-12', '13-14', '15-16', '17-18']
df['binned'] = pd.cut(df['Calling_time'], bins, labels=labels)
# df.drop(['Calling_time'], axis=1)

df = df[['Day', '%_listened', 'binned']]
# print(df[['Day', '%_listened', 'binned']])
# split data into x and y variables
y_tr = df.iloc[:, 2]
x_tr = (df.iloc[:, 0:2])

# convert categorical data to dummy variables for mathematical analysis
x_tr = pd.get_dummies(x_tr)
# print(x_tr.info())

# Train model
SVM = svm.SVC(decision_function_shape="ovo", gamma='auto').fit(x_tr, y_tr)
print(SVM.predict(x_tr[:1]))
