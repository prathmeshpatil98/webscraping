from bs4 import BeautifulSoup as bfs
import requests
import urllib.request
import os

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def download_images(base_url, keyword, num_images):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    search_url = f"{base_url}/search/{keyword}"
    sourceweb = requests.get(search_url, headers=headers).text
    soup = bfs(sourceweb, 'lxml')

    images_links = soup.select('img[src^="https://www.freeimages.com/photo/"]')
    images = []
    for i in range(min(num_images, len(images_links))):
        images.append(images_links[i]['src'])

    create_directory(keyword)
    for i in range(len(images)):
        name = f"{keyword}/catpic_{i}.png"
        urllib.request.urlretrieve(images[i], name)

if __name__ == "__main__":
    base_url = 'https://www.freeimages.com'
    keyword = 'cat'  # You can change this keyword to any other topic you want to search for images
    num_images = 5  # Number of images to download, change it as needed

    download_images(base_url, keyword, num_images)
