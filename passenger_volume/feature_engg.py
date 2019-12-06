import os

import pandas as pd
import reverse_geocoder

train_data_file_path = os.getcwd() + '/DataSet/Train.csv'
test_data_file_path = os.getcwd() + '/DataSet/Test.csv'

train_df = pd.read_csv(train_data_file_path, low_memory=False)
test_df = pd.read_csv(test_data_file_path, low_memory=False)
train_df = train_df.iloc[0]

new = reverse_geocoder.search((train_df.latitude_source, train_df.longitude_source))
# Loading formatted geocode file...
# train_df['address'] = train_df.apply(lambda row: reverse_geocoder.search(row['latitude_source'], row['longitude_source']))
train_df['country'] = train_df.apply(lambda row: reverse_geocoder.search((row['latitude'], row['longitude'])))

print(train_df['country'])
