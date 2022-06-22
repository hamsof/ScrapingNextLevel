import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
s = Service('C:\Program Files\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url  = 'https://github.com/'
driver.get(url)

time.sleep(2)
users = list()
user_names = list()
full_names = list()
intros  = list()
total_users  = str()

def search():
    search_button = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
    search_button.send_keys("repos:>=400 location:pakistan",Keys.ENTER)
    time.sleep(5)
    total_users = driver.find_element(By.XPATH,'//*[@id="js-pjax-container"]/div/div[3]/div/div[1]/h3').text
    print(total_users)


def data():

    time.sleep(2)
    users =  driver.find_elements(By.CSS_SELECTOR,'.hx_hit-user')
    for data in users:
        try:
            name = data.find_element(By.CSS_SELECTOR,'.f4 .color-fg-muted').text
        except:
            name = "No name "
        try:      
            login = data.find_element(By.CSS_SELECTOR,'.f4 .mr-1').text
        except:
            login = "No user name"
        try:
            intro = data.find_element(By.TAG_NAME,'p').text
        except:
            intro = "No intro"

        print(name," ",login, " ",intro)    
        user_names.append(login)
        full_names.append(name)
        intros.append(intro)
                 

def main():
    search()
    while(True):
        data()
        try:
            driver.find_element(By.CSS_SELECTOR,'.paginate-container')
        except:
            break    
        try:    
            next_button=driver.find_element(By.CSS_SELECTOR,'.next_page')
            try:
                driver.find_element(By.CSS_SELECTOR,'.next_page.disabled') 
                break
            except:
                driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
        except:
            break
            


if __name__=="__main__":
    main()

    with open('main_page.csv', 'wt') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow(['Name  ', 'User Name   ', 'Intro'])
        for i in range(len(user_names)):
            csv_writer.writerow([full_names[i], user_names[i] ,intros[i]])

print("\n",total_users,"\n")
