import sqlite3

import pandas as pd

conn = sqlite3.connect(database="titanic_data")
# host='localhost', user="root", passwd="password", database="titanic_data"

select_query = ("SELECT contentFile, (percentage_listened)/100, hour(call_start_time) "
                "FROM titanic_data.beneficiary_call_measure;")

df = pd.read_sql(select_query, conn)
