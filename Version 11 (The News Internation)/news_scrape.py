from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

s = Service('C:\Program Files\chromedriver.exe')
myoptions = Options()
driver = Chrome(service=s, options=myoptions) 
driver.maximize_window()



driver.get('https://www.thenews.com.pk/today')  
time.sleep(2)


urls = []


try:
    s =  WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"China"))) 
    search_keywords = driver.find_elements(By.PARTIAL_LINK_TEXT,"China")
    for i in search_keywords:
        print(i.text)
        urls.append(i.get_attribute("href"))
except:
    print("I did not find it ")       


print(urls)

original_window = driver.current_window_handle

news_artiles  = []
authors = []
headings = []



for i in urls:
    
    driver.switch_to.new_window('tab')
    driver.get(i)
    
    try:
        heading  =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".detail-heading h1")))    
        author = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".category-source")))
        artile = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".story-detail")))
        
        print(heading.text,author.text,artile.text)
        
        news_artiles.append(artile.text)
        authors.append(author.text)
        headings.append(heading.text)
    
    except:
        pass    

    driver.switch_to.window(original_window)




fd = open('news_china.csv', 'wt')
csv_writer = csv.writer(fd)
csv_writer.writerow(['Heading', 'Author', 'Article' ])


for i in range(len(headings)):
    csv_writer.writerow([headings[i], authors[i] ,news_artiles[i]])

fd.close()