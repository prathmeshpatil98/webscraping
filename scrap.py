'''import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flip_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
urlclient = urlopen(flip_url)
flip_page = urlclient.read()
flip_page.decode('utf-8')
flip_html = bs(flip_page ,'html.parser')
encoded_content = flip_html.prettify().encode('utf-8')
print(encoded_content)

flip__webpage = flip_html.findAll("div",{"class" : "_1AtVbE col-12-12"})
for i in flip__webpage :
    print(i)'''

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
for i in flip__webpage:
    print(i)






