
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



#Selenium
from selenium import webdriver

url = 'https://www.exist.com'
driver = webdriver.Chrome()
driver.get(url)

search_box = driver.find_element_by_name('search')
search_box.send_keys('Python')
search_box.submit()