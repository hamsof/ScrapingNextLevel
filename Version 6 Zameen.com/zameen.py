from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('C:\Program Files\chromedriver.exe') #path where driver is located on your local disk
driver = webdriver.Chrome(service=s)

url  = 'https://www.zameen.com'
driver.get(url)

time.sleep(2)

##### zameen.com main page filters 

### Actually these filters are not dropdown menues these are actualy button so first we will click
### Button then from list we click our desired button
### for example click on city button will appear cities we will enter lahore keys then lahore button
### will be visible then we will click lahore

click_city = driver.find_element(By.XPATH,'//*[@aria-label="City filter"]') # selecting by the attribute aria-label
click_city.click() 
chose_city = driver.find_element(By.XPATH,'//*[@aria-label="Lahore"]')
chose_city.click()
find_button = driver.find_element(By.XPATH,'//*[@aria-label="Find button"]')
find_button.click()

#### next page asal filters 

chose_perpose = driver.find_element(By.XPATH,'//*[@id="large-search-form"]/div/div/div[1]/div[1]/div/div[1]')
chose_perpose.click()
find_buy = driver.find_element(By.XPATH,'//*[@aria-label="Buy"]') # change aria label to Rent fot rent perpose


##########3 price

chose_price = driver.find_element(By.XPATH,'//*[@aria-label="Price filter"]')
chose_price.click()

chose_min_price = driver.find_element(By.XPATH,'//*[@id="large-search-form"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/input') # was not accessible by attribute
chose_min_price.send_keys(5000000) # min price 50 lakh

chose_max_price = driver.find_element(By.XPATH,'//*[@id="large-search-form"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input')
chose_max_price.send_keys(10000000) # max price 1 crore
chose_price.click()

#### marla button
find_length = driver.find_element(By.XPATH,'//*[@aria-label="Area filter"]')
find_length.click()
### min marla
chose_min_length = driver.find_element(By.XPATH,'//*[@id="large-search-form"]/div/div/div[1]/div[5]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/input')
chose_min_length.send_keys(5) # 5 marla
#### max marla 
chose_max_length = driver.find_element(By.XPATH,'//*[@id="large-search-form"]/div/div/div[1]/div[5]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input')
chose_max_length.send_keys(20) # 10 marla 
find_length.click()


driver.refresh() #sometimes it does not show actual results by reload it will !
time.sleep(5) 

prices = list()
addressess= list()
bedses = list()
bathses = list()
areas = list()
pics = list()


### getting house information from article tag and info i am getting by using selenium not BS4

def homes():
    try:
        Elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'article'))) # wait until the articles loaded
        articles = driver.find_elements(By.TAG_NAME,'article')
    except:
        return    
    count=0
    for i in articles:
        if(count == 2 or count==5): # These are not in our interest articles actualy are ads
            count+=1
            continue
        try:
            price = i.find_element(By.XPATH,'.//span[@aria-label="Price"]').text ####Dot is very important if we skip this it will not find this element inside of that particuler article
        except:
            price = "No info given"
        try:    
            address = i.find_element(By.XPATH,'.//*[@aria-label="Title"]').text
        except:
            address = "No info given"
        try:        
            beds = i.find_element(By.XPATH,'.//*[@aria-label="Beds"]').text
        except:
            beds = "No info given"
        try:        
            baths = i.find_element(By.XPATH,'.//*[@aria-label="Baths"]').text
        except:
            baths = "No info given"    
        #area = i.find_element(By.XPATH,'//*[@id="body-wrapper"]/main/div[3]/div[2]/div[4]/div[1]/ul/li[35]/article/div[3]/div[2]/div[2]/div[2]/div/span[3]/span/div/div/div[1]/span')
        try:        
            area = i.find_element(By.XPATH,'.//*[@aria-label="Area"]').text
        except:
            area = "No info given"
        try:    
            WebDriverWait(i, 10).until(EC.presence_of_element_located((By.XPATH, './/*[@aria-label="Listing photo"]')))
            pic = i.find_element(By.XPATH,'.//*[@aria-label="Listing photo"]').get_attribute('data-src')    
            if (pic == None):
                pic = i.find_element(By.XPATH,'.//*[@aria-label="Listing photo"]').get_attribute('src')
                if(pic == None): 
                    pic = "No pic"        
        except:
            pic = "No info given"    
        print(price, " " ,address, " " ,beds, " ",baths, " ", area, " ",pic)
        prices.append(price)
        addressess.append(address)
        bedses.append(beds)
        bathses.append(baths)
        areas.append(area)
        pics.append(pic)
        count+=1



### actual loop 

#it took me 5 hours to find this logic 
while(True):
    try:
        homes()
        myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@title="Next"]'))) # waiting until next button appears
        next_button = driver.find_element(By.XPATH,'//a[@title="Next"]')
        driver.execute_script("arguments[0].scrollIntoView();", next_button) #if we want to click then we have to go that element
        driver.execute_script("scrollBy(0,-200);") # next button after apearing goes below navbar this was a big issue so i have to scrol up some pixels and then click
        next_button.click()
    except:
        break


fd = open('zameen.csv', 'wt')
csv_writer = csv.writer(fd)
csv_writer.writerow(['Price', 'Area', 'Address' , 'Beds' ,'Bath', 'Pic' ])


for i in range(len(prices)):
    csv_writer.writerow([prices[i], areas[i] ,addressess[i], bedses[i], bathses[i], pics[i]])

fd.close()