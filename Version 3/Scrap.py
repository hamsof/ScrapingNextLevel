import requests
from bs4 import BeautifulSoup

url = 'https://hamsof.github.io/simple-book-show/'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

my_tables = soup.find_all('table') 

prices = list()
book_names = list()
stock_info = list()
prices = list()
reviews = list()


for table in my_tables:
    rows = table.find_all('tr')
    for index_1,row in enumerate(rows):
        cols = row.find_all('td')
        for col in cols:
            data = col.text.strip()
            #print(index_1,' ' ,data)
            #index_1 row 1 contains imgs
            if(index_1==1):#names
                book_names.append(data)
            elif(index_1==2):#price
                prices.append(data)
            elif(index_1==3):#in stock
                stock_info.append(data)    
            #elif(index_1==4):#reviews that will be fetched by their data-rating
            #elif(index_1==5):#add to cart not required


data  = soup.find_all('p',{'class':'review'})
for review in data:
    reviews.append(review['data-rating'])


print("\nWelcome to Scrapper system\n")
for i in range (9):
    print("BOOK : " , i+1)
    print("        ",book_names[i])
    print("        ",prices[i])
    print("        ",stock_info[i])
    print("        ",reviews[i])

