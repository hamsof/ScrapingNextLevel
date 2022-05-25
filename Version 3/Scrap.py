import requests
from bs4 import BeautifulSoup

url = 'https://hamsof.github.io/simple-book-show/'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

my_tables = soup.find_all('table')
links = soup.find_all("")

## now getting specific data

# print(mytables[0])

### collecting data whole ####  

# for table in my_tables:
#     rows = table.find_all('tr')
#     for row in rows:
#         cols = row.find_all('td')
#         for col in cols:
#             data = col.text.strip()
#             #print(data)    




# in that way we can make a list of all the attrubutes

# prices = list()
# book_names = list()
# stock_info = list()
# phone_number = list()



# for table in my_tables:
#     rows = table.find_all('tr')
#     for index_1,row in enumerate(rows):
#         cols = row.find_all('td')
#         for index,col in enumerate(cols):
#             data = col.text.strip()
#             if(index_1==1):#names
#                 book_names.append(data)
#             elif(index_1==2):#stock
#                 stock_info.append(data)
#             elif(index_1==3):#price
#                 prices.append(data)    
#             elif(index_1==4):#phone number
#                 phone_number.append(data)   
#             #elif(index_1==5):#add to cart not required

# print("\nWelcome to Scrapper system\n")
# for i in range (9):
#     print("BOOK : " , i+1)
#     print("        ",book_names[i])
#     print("        ",prices[i])
#     print("        ",stock_info[i])
#     print("        ",phone_number[i])

