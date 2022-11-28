import csv

import requests
from bs4 import BeautifulSoup


url = 'https://booth.pm/ja/search/VRChat?in_stock=false&new_arrival=true'
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser",from_encoding='utf-8')

topic = soup.find(class_="u-mt-400") 

with open('booth_data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    for element in topic.find_all("li"): 
         imageURL = element.find("a")
         image = imageURL.get("data-original")
         imurl = imageURL.get("href")

         source2 = element.find(class_="item-card__title")
         title = source2.find("a")

         price = element.find(class_="price")

         print(title.text)
         print(price.text)
         print(image)
         print(imurl)
         print()

         row = [title.text, price.text, imurl, image]
         writer.writerow(row)