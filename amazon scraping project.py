from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests


path= "D:\VOC\scraping\chromedriver_win32\chromedriver.exe"
url= 'https://www.amazon.in/'

driver =webdriver.Chrome(path)

driver.get(url)

box = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
box.send_keys('oneplus 11r')
box.send_keys(Keys.ENTER)

time.sleep(3)

link = driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a')
link.click()

time.sleep(3)

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]
driver.switch_to.window(chld)

last_height = driver.execute_script('return document.body.scrollHeight')


driver.execute_script('window.scrollTo(0,15000)')


see_all_reviews = driver.find_element(By.XPATH,'//*[@id="reviews-medley-footer"]/div[2]/a')
see_all_reviews.click()






df = pd.DataFrame({'Review Rating' : [''] , 'Short Description' : [''], 'Date' : [''], 'Review' : ['']})

while True:
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    all_reviews = soup.find_all('div', class_='a-section celwidget')     
        
    for details in all_reviews:
            
        try:
                                
                        
                            
            review_rating =details.find('a', class_='a-link-normal').text[0:3]
            short_description = details.find('a', class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').text
            initial_date =details.find('span' , class_='a-size-base a-color-secondary review-date').text.split()[-3:]     
            date=initial_date[0] + " " + initial_date[1] + " " + initial_date[2]
            full_review = details.find('div', class_='a-row a-spacing-small review-data').text
            df = df.append({'Review Rating':review_rating , 'Short Description':short_description , 'Date':date , 'Review':full_review}, ignore_index = True)
            last_height1 = driver.execute_script('return document.body.scrollHeight')
            driver.execute_script('window.scrollTo(0,6500)')
            time.sleep(3)
          
            
        except:
            pass
        
        try:
            button = soup.find_element(By.XPATH,'//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
            button.click()
            
           
        except:
            break
                 
        #next_page =soup.find_element(By.XPATH,'//*[@id="cm_cr-pagination_bar"]/ul/li[2]')
       # next_page.click()
        #time.sleep(3)
       
   
              
    
   # df.to_csv("D:\VOC\scraping\project\my_data.csv")
#reviewpage_height = driver.execute_script('return document.body.scrollHeight')

#print(reviewpage_height)
