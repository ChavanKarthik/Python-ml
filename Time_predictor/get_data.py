import mysql.connector
import pandas as pd
from mysql.connector import Error
from sklearn import tree

try:
    mydb = mysql.connector.connect(host='localhost',
                                   user="root",
                                   passwd="beehyv123",
                                   database="titanic_data")
    select_query = ("SELECT DAYNAME(modificationDate) AS 'Day', HOUR(call_start_time) AS 'Calling_time', case when (("
                    "percentage_listened)/100)>=0.7 then 'Yes' else 'No' end  AS 'preferable_time', "
                    "(percentage_listened) / 100 AS '%_listened' FROM titanic_data.beneficiary_call_measure;")
    my_cursor = mydb.cursor()

    my_cursor.execute(select_query)

    records = my_cursor.fetchall()

    data = [x for x in records]
    # print(data)

    df = pd.DataFrame(data, columns=['Day', 'Calling_time', 'preferable_time', '%_listened'])
    print(df.head())

    clf = tree.DecisionTreeClassifier()

    # features which impact %_listened
    X = df[['subscription_type', 'Calling_time', 'preferable_time']]
    # print(X)

    # output of individual records
    Y = df['%_listened']
    # print(Y)

    clf = clf.fit(X, Y)

    prediction = clf.predict([[1, 11, 1]])
    print(prediction)

    my_cursor.close()
except Error as e:
    print("Error while connecting to MySQL", e)
