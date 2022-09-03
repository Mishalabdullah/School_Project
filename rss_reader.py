from bs4 import BeautifulSoup
import requests


url = requests.get("https://lukesmith.xyz/index.xml")
soup = BeautifulSoup(url.content,'xml')
print(soup)
