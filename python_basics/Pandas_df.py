# importing the necessary packages
import os

import pandas as pd
import pandas_profiling

os.chdir("/home/beehyv/Downloads/python/python_basics")


def main():
    # my code for profiling
    df = pd.read_csv('/home/beehyv/Downloads/python/titanic/data/raw/test.csv')
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file("titanic_data_profile.html")


if __name__ == "__main__":
    main()

# pandas_profiling.ProfileReport(df)
# print(df.profile_report())

data = pd.read_csv("sample_csv1.csv")  # Get data in a object
# print(data) # To print whole data
# print(data.head(2)) # To return top n (5 by default) rows of a data frame
# print(data.columns.tolist())  # To return all column names
# print(data.loc[[1], ['P_ID', 'P_Name']])  # To return specific columns and rows 1,3
# data2 = pd.read_excel('sample_excel.xlsx')
# print(data2.loc[[1], ['id', ' block_id']])
