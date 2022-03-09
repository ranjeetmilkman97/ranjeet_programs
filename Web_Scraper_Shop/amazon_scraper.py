from bs4 import BeautifulSoup as soup
import csv
import requests

my_url="https://www.amazon.in/s?k=samsung+mobiles&rh=n%3A1389401031&crid=30A5J1QWDVYM6&sprefix=samsung+mobil%2Caps%2C599&ref=nb_sb_noss_2"

source = requests.get(my_url).text

page_soup = soup(source, "lxml")

item_name = page_soup.findAll("span", { "class": "a-size-medium a-color-base a-text-normal"})
item_price = page_soup.findAll("span", { "class": "a-offscreen"})

with open ('amazon_scrape.csv', 'w') as f:
    headers = ['Name', 'Pricing']
    
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

    for (item,price) in zip(item_name,item_price):        
        csv_writer.writerow([item.text,price.text])    
   

       





