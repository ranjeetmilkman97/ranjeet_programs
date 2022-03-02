from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

my_url="https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


item_name = page_soup.findAll("div", { "class": "_4rR01T"})
item_price = page_soup.findAll("div",{ "class": "_30jeq3 _1_WHN1"})


with open ('flip_scrape.csv', 'w') as f:
    headers = ['Name', 'Pricing']
    
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

    for (item,price) in zip(item_name,item_price):        
        csv_writer.writerow([item.text,price.text])    
   

       





