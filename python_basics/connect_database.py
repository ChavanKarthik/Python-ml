import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='password', database='motech_data_services')

mycursor = mydb.cursor()  # we can run quires by creating a cursor

mycursor.execute("select * from wash_states limit 1;")  # To pass quires to run

for i in mycursor:
    print('data in wash_states table', i)
