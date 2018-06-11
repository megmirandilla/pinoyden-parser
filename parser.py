import urllib.request
import copy
from bs4 import BeautifulSoup

data = {'user_id':'', 'message':'', 'quotes':''}
quote = {'user_id':'', 'message':''}
quote_list = []

url = 'http://www.pinoyden.com.ph/index.php?topic=343063.0'
response = urllib.request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

users_block = soup.find_all("div",{"class":"poster"})
post_block = soup.find_all("div",{"class":"post"})
# print(len(authors))

posts = []
for block in post_block:
	posts.append(block.text)

users = []
for block in users_block:
	users.append(block.find("div",{"class":"bigtext"}).find("a").text) 

# print(users)
