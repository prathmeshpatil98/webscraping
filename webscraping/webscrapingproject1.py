import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    text = paragraph.get_text().strip()
    print(text)
