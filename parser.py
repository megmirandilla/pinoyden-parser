import urllib.request
import copy
import json
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

for i in range(len(posts)):
	if i==0:
		data['user_id'] = users[i]
		data['message'] = posts[i]
	quote['user_id'] = users[i]
	quote['message'] = posts[i]
	quote_list.append(copy.deepcopy(quote))

data['quotes'] = copy.deepcopy(quote_list)

with open('data.json','w') as fp:
	json.dump(data, fp)