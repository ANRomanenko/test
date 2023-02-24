from bs4 import BeautifulSoup
import requests

url = 'https://rozetka.com.ua/nabori-po-uhodu-za-litsom/c4657328/'
response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")
lists = soup.find_all('div', class_='goods-tile__inner')
print(lists)
