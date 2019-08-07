from bs4 import BeautifulSoup
import requests

url = "https://www.python.org/"

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    resultado = (link.get('href').split())
    print(resultado)
