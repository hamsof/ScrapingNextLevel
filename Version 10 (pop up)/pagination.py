from cmath import log
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

titles = []
prices = []
availability=[]
reviews=[]
links=[]
star_rates =[]

def books():

    time.sleep(2)

    books = driver.find_elements(By.CLASS_NAME, 'col-sm-4')
    books_count = len(books)
    for i in range(1,books_count+1):
        title = driver.find_element(By.XPATH,'//*[@id="container"]/div[' +str(i)+ ']/p[1]').text
        titles.append(title)
        price = driver.find_element(By.XPATH,'//*[@id="container"]/div[' +str(i)+ ']/div/p[1]').text
        prices.append(price)
        avail = driver.find_element(By.XPATH,'//*[@id="container"]/div[' +str(i)+ ']/div/p[2]').text
        availability.append(avail)
        review = driver.find_element(By.XPATH,'//*[@id="container"]/div[' +str(i)+ ']/div/p[3]').text
        reviews.append(review)
        link = driver.find_element(By.XPATH,'//*[@id="container"]/div[' +str(i)+ ']/p[1]/a').get_attribute('href')
        links.append(link)
        star_rate = driver.find_element(By.XPATH,'//*[@id="container"]/div[' +str(i)+ ']/div/div').get_attribute('data-rate-star')
        star_rate = round(float(star_rate),2) # fixing our rating to only 2 floatng points
        star_rates.append(star_rate)
    

    
    
s = Service('C:\Program Files\chromedriver.exe') 
driver = Chrome(service=s)

    
# Need to add the logic for iterating through all the pages

### The logic is not to get the links and then got to to that link one by one
### We will be using the some good way. In my sense is to click to the next button until it disappear
### I have done same thing in Github scraping as well
## Lets do it in same fashion

url  = 'https://hamsof.github.io/simple-book-show/Version%2010%20(pop%20up)/?page_1#'

driver.get(url)
driver.maximize_window()


#### Lets close the pop up
# it will take 3 seconds then pop up appears
time.sleep(5)

driver.switch_to.frame(driver.find_element(By.ID,'frame'))

clos_button  = driver.find_element(By.XPATH,'//*[@id="staticBackdrop"]/div/div/div[1]/button')
clos_button.click()

driver.switch_to.default_content()


while(True):
        books()    
        page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.page-item'))) ## this is what wait looks like and this is important otherwise this code dont even But github worked without wait as i loaded all the data very fast
        try:    
            driver.find_element(By.XPATH,'//*[@id="page_8"]')
            driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH,'//*[@id="page_8"]'))
            try:
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR,'.page-item.disabled') ## finding the disbale class which disable the last page if we get this then break otherwise exception will be throwed
                break
            except:
                driver.find_element(By.XPATH,'//*[@id="page_8"]').click()  ## as exception throwed now should to the next button i mean a tag of next page      
        except:
            break


# Writing in the file
data = {'Title/Author':titles, 'Price':prices, 'Availability':availability, 
        'Reviews':reviews, 'Links':links, 'StarRating': star_rates}
df = pd.DataFrame(data, columns=['Title/Author', 'Price', 'Availability', 'Reviews', 'Links', 'StarRating'])
df.to_csv('books_pagination.csv', index=False)
df = pd.read_csv('books_pagination.csv')
df