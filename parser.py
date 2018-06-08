import urllib.request
import copy
from bs4 import BeautifulSoup

url = 'http://www.pinoyden.com.ph/index.php?topic=391263.0'
response = urllib.request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

authors = soup.find_all("div",{"class":"poster"})
posts = soup.find_all("div",{"class":"post"})
# print(len(authors))


