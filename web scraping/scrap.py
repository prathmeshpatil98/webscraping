# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen
# import logging

# flip_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
# urlclient = urlopen(flip_url)
# flip_page = urlclient.read()
# # flip_page.decode('utf-8')
# flip_html = bs(flip_page ,'html.parser')
# # flip_html.encode('utf-8')

# # flip_html.findA
# flip__webpage = flip_html.findAll("div",{"class" : "_1AtVbE col-12-12"})
# for i in flip__webpage :
#     print(i)

import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flip_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
urlclient = urlopen(flip_url)
flip_page = urlclient.read().decode('utf-8')  # Specify the character encoding as 'utf-8'
flip_html = bs(flip_page, 'html.parser')

flip__webpage = flip_html.findAll("div", {"class": "_1AtVbE col-12-12"})
for i in flip__webpage:
    print(i)



