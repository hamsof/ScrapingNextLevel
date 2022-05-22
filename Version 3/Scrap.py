# my try of scraping


import requests
from bs4 import BeautifulSoup

url = 'https://hamsof.github.io/simple-book-show/'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

my_tables = soup.find_all('table')

## now getting specific data

# print(mytables[0])

### collecting data

for table in my_tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        for col in cols:
            data = col.text.strip()
            #print(data)   
            #  
for table in my_tables:
    i=0
    rows = table.find_all('tr')
    for index_1,row in enumerate(rows):
        cols = row.find_all('td')
        print(f"{cols[i].text}")
    i+=1
