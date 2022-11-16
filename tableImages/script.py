from bs4 import BeautifulSoup
import os

imagePath = 'tableImages/'

def findImageInList(name):
	for image in os.listdir(imagePath):
		if name+'.jpg' == image:
			return image
	return None

with open('table.html', 'r', encoding='utf-8') as f:
	content = f.read()
	soup = BeautifulSoup(content, 'html')
	table = soup.table
	trs = table.find_all('tr')
	skip = True
	for i in range(0,len(trs)):
		if skip:
			skip = False
			continue
		tds = trs[i].find_all('td')
		name = tds[1].text
		if len(tds) <= 5:
			continue
		temp = tds[5].find_all('img')
		if len(temp) == 0:
			continue
		img = temp[0]
		imageName = findImageInList(name)
		if imageName == None:
			continue
		img['src'] = imagePath+imageName

with open('table1.html','w', encoding='utf-8') as wr:
	wr.write(str(table))

