import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
import sys

sys.stdout.reconfigure(encoding='utf-8')


flip_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
urlclient = urlopen(flip_url)
flip_page = urlclient.read()
flip_page = flip_page.decode('utf-8')  # Decode and store the content in flip_page
flip_html = bs(flip_page ,'html.parser')

flip__webpage = flip_html.findAll("div", {"class": "_1AtVbE col-12-12"})
find_len = (len(flip__webpage))
del flip__webpage[0:2]
del flip__webpage[-3:]
box = flip__webpage[len(flip__webpage)-1]

product_link = "https://www.flipkart.com" +flip__webpage[3].div.div.div.a['href']
#print(product_link)
product_req = requests.get(product_link)
flipproduct_html = (bs(product_req.text,'html.parser'))
productreview_boxes = flipproduct_html.find_all("div",{"class": "_16PBlm"})
#len(productreview_boxes)
#print(productreview_boxes[0].)
del(productreview_boxes[-1])

allReviews =[]
for i in productreview_boxes:
    print("reviewer name :-")
    print(i.div.div.find('p', {"class": "_2sc7ZR _2V5EHH"}).text)
    print("reviewer rating:-")
    print(i.div.div.div.div.text)
    print("reviewer comment:-")
    print(i.div.div.div.p.text)
    print("reviewer description:-")
    print(i.div.div.find_all('div', {"class": ""}))
    print("=================================")
    review = {
        "name" : i.div.div.find('p',{"class":"_2sc7ZR _2V5EHH"}).text,
        "rating" : i.div.div.div.div.text, 
        "comment" : i.div.div.div.p.text,
        "description" : i.div.div.find_all('div', {"class":""})
    }
    allReviews.append(review)
print(allReviews)



