import csv

import requests
from bs4 import BeautifulSoup

url = "https://www.cisce.org/locate-search.aspx?country=2&state=5&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=&search=locate"
# url = "http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx"

page = requests.get(url)
page_text = page.text

outfile = open("table_data.csv", "w", newline='')
writer = csv.writer(outfile)

tree = BeautifulSoup(page_text, "lxml")
table_tag = tree.select("table")[0]
tab_data = [[item.text for item in row_data.select("td")]
            for row_data in table_tag.select("tr")]

for data in tab_data:
    writer.writerow(data)

outfile.close()
