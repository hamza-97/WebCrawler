from bs4 import BeautifulSoup

import requests


lister = []
number = 0

def newfunc(funcurl):
	global number	
	r  = requests.get(funcurl)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	counter = 0;
	newurl = funcurl
	check = r

	for link in soup.find_all('a'):
		if (link.get('href')):
			if (link.get('href') not in lister):
				filename = "file" + str(number)
				if (url in link.get('href')):
					lister.append(link.get('href'))
					newr  = requests.get(link.get('href'))

					newsoup = BeautifulSoup(newr.content,"html.parser")
					with open(filename +".html",'w') as file:
						file.write(newr.content)
					number = number + 1
					print link.get('href')
					newfunc(link.get('href'))

				elif ("http" not in link.get('href') and "mailto" not in link.get('href') and "//" not in link.get('href') and "www" not in link.get('href') and ":" not in link.get('href')):
					newurl = url + link.get('href')
					lister.append(link.get('href'))
					newr  = requests.get(funcurl)
					with open(filename +".html",'w') as file:
						file.write(newr.content)
					number = number + 1
					print url + link.get('href')

					newfunc(url + link.get('href'))
				else:
					continue			
	return


url = "https://www.syedfaaizhussain.com/"
r  = requests.get(url)
verynewsoup = BeautifulSoup(r.content,"html.parser")
with open("file.html",'w') as file:
	file.write(r.content)
name = "filer"
newfunc(url)
lenghter = len(lister) + 1

print lenghter
