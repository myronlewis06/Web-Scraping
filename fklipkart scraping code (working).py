from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests

df = pd.DataFrame({'Review Rating' : [''] , 'Short Description' : [''] , 'Review' : ['']})         
path= "D:\VOC\scraping\chromedriver_win32\chromedriver.exe"
for i in range(1,10):
    url= 'https://www.flipkart.com/apple-iphone-14-pro-max-space-black-128-gb/product-reviews/itm9aed88fe43457?pid=MOBGHWFHCNVGGMZF&lid=LSTMOBGHWFHCNVGGMZFEEIZN3&marketplace=FLIPKART&page='+str(i)
    print(url)
    requests.get(url)   #To check if the webpage can be scraped

    driver =webdriver.Chrome(path)

    driver.get(url)
    time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    all_reviews= soup.find_all('div', class_='col _2wzgFH K0kLPL')
    

                
    for details in all_reviews:
        
        try:
                                                            
            review_rating= details.find('div', class_='_3LWZlK _1BLPMq').text
            short_description = details.find('p', class_='_2-N8zT').text
            full_review = details.find('div', class_='t-ZTKy').text
            df = df.append({'Review Rating':review_rating , 'Short Description':short_description , 'Review':full_review}, ignore_index = True)
            time.sleep(1)
            
        except:
            pass
              
df.to_csv("D:/VOC/scraping/project/flipkart_data.csv")