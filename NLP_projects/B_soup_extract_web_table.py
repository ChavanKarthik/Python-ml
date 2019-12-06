import csv

import requests
from bs4 import BeautifulSoup

url = "https://www.cisce.org/locate-search.aspx?country=2&state=5&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=&search=locate"
page = requests.get(url)
page_text = page.text

soup = BeautifulSoup(page_text, "lxml")
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th", "td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("table_data.csv", "w", newline='')
writer = csv.writer(outfile)

for item in list_of_rows:
    print(' '.join(item))
