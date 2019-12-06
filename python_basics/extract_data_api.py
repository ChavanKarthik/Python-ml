# requests module is used for rest API handling
import time

import requests

# store url with &api_key
url = 'https://api.data.gov/ed/collegescorecard/v1/schools?school.name=boston%20college&api_key=wBNhUTE5YykkCrmM9pvW4HnhUKzH8hK2gFBfcz70'

# save response in result
response1 = requests.get(url)

# to wait for response
time.sleep(3)

# to get headers
print(response1.headers)

# to get response in Json format
print(response1.json())

# to get response in text format
print(response1.text)

# to get status_code
print(response1.status_code)
