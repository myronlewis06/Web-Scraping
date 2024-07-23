import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7"

page = requests.get(url)
page  # response 200

soup =BeautifulSoup(page.text, "lxml")

postings = soup.find_all('div', class_="media soft push-none rule")

df=pd.DataFrame({'Links':[''],'Car Name' : [''], 'Price' : [''], 'Car Colour' : ['']})

while True:

    for post in postings:
        
        try:
           
            
           link = post.find('a',class_='media__img media__img--thumb').get('href')
           link_full = "https://www.carpages.ca" + link
           name = post.find('h4', class_='hN').text.strip()
           price = post.find('strong', class_="delta").text.strip()
           colour =post.find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
           df=df.append({'Links':link_full,'Car Name' : name, 'Price' : price, 'Car Colour' : colour}, ignore_index=True)
           
        except:
            pass
        
        
    
    next_page =soup.find('a',{'title' :'Next Page'}).get('href')
    next_page_full="https://www.carpages.ca" + next_page

    url =next_page_full
    page=requests.get(url)
    soup =BeautifulSoup(page.text, "lxml")
           
         
df.to_csv('D:/VOC/scraping/Cardata.csv')          