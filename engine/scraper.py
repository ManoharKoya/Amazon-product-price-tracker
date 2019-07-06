import requests
from bs4 import BeautifulSoup
import winsound
import sys
import time

URL = sys.argv[1]

# URL = "https://www.amazon.in/gp/product/B07S3BD2W6?pf_rd_p=f2b20090-067d-415f-953d-b8dcecc9109f&pf_rd_r=GAYVDNG5S3NMB5D1DJSD"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

def convertPrice(txt):
   leng = len(txt)
   priceStr = ""
   for i in txt:
       if i!=',' :
           priceStr = priceStr + i
   price = float(priceStr)
   return price

priceDesire = 33000
soup = BeautifulSoup(page.content, 'html.parser')

ProductName = soup.find(id="productTitle").get_text().strip()
ProdValue = soup.find(id="priceblock_ourprice").get_text().strip()
price = convertPrice(ProdValue)

print("HelloMan")

if(priceDesire>=price):
        print("check website, you should be ready to buy")
        winsound.Beep(3000,1500)      
        
sys.stdout.flush()  
