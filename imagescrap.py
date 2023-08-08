
'''from bs4 import BeautifulSoup as bfs
import requests 
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

sourceweb = requests.get('https://www.freeimages.com/search/dog',headers = headers).text
soup = bfs(sourceweb,'lxml')

images = []
images_links = soup.select('img[src^="https://www.freeimages.com/photo/dog"]')
print(images_links)
for i in range (len(images)):
    images.append(images_links[i]['src'])

for i in range (len(images)):
    name = f"D:\dogpic"+str(i)".png"
    urllib.request.urlretrive(images[i,name])'''
from bs4 import BeautifulSoup as bfs
import requests
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

sourceweb = requests.get('https://www.freeimages.com/search/dog', headers=headers).text
soup = bfs(sourceweb, 'lxml')

images_links = soup.select('img[src^="https://www.freeimages.com/photo"]')
images = []
for i in range(len(images_links)):
    images.append(images_links[i]['src'])

for i in range(len(images)):
    name = f"D:\\dogpic{i}.png"  # Use double backslashes to escape the backslash properly
    urllib.request.urlretrieve(images[i], name)
