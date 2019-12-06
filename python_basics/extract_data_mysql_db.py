# import library of mysql
import pymysql

# connect to database
connection = pymysql.connect(host='localhost', user='root', password='password', database='titanic_data')

# create a cursor
cursor = connection.cursor()

# query to create table
create_table = """CREATE TABLE `Students_report1` (
  `roll_number` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `maths` int(11) DEFAULT NULL,
  `physics` int(11) DEFAULT NULL,
  `chemistry` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `average` int(11) DEFAULT NULL,
  `grade` varchar(45) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`roll_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1"""

# executing create table
# cursor.execute(create_table)

load_data = "INSERT INTO titanic_data.Students_report1 (`roll_number`, `name`, `maths`, `physics`, `chemistry`, `total`, `average`, `grade`, `rank`) VALUES ('1', 'sai', '75', '85', '95', '255', '85', 'A', '3');"

# inserting data
# cursor.execute(load_data)

query = "select * from titanic_data.Students_report1;"

# run the query
cursor.execute(query)

# retrieve data from cursor
for i in cursor:
    print(i)

print(cursor)

# closing connection
connection.close()
