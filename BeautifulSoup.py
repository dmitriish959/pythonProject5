
from bs4 import BeautifulSoup
import requests

url = 'https://www.exist.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все заголовки "Колодки" на странице
headings = soup.find_all('h1')
for heading in headings:
    if heading.text == 'Колодки':
        print(heading.text)