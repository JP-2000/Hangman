import csv
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

list500=[]


def top1_100():
	url='https://www.imdb.com/list/ls063540474/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)


def top1_158():
	url='https://www.imdb.com/list/ls063540474/?sort=moviemeter,asc&st_dt=&mode=detail&page=2'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)


def top2_100():
	url='https://www.imdb.com/list/ls063208123/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)
		
def top2_200():
	url='https://www.imdb.com/list/ls063208123/?sort=moviemeter,asc&st_dt=&mode=detail&page=2'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)
		
		

def top2_300():
	url='https://www.imdb.com/list/ls063208123/?sort=moviemeter,asc&st_dt=&mode=detail&page=3'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)

def top2_400():
	url='https://www.imdb.com/list/ls063208123/?sort=moviemeter,asc&st_dt=&mode=detail&page=4'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)

def top2_500():
	url='https://www.imdb.com/list/ls063208123/?sort=moviemeter,asc&st_dt=&mode=detail&page=5'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)


print('hola')
top1_100()
top1_158()
top2_100()
top2_200()
top2_300()
top2_400()
top2_500()

list500=list(dict.fromkeys(list500))

with open('h_list.csv','w',newline='') as f:
	w=csv.writer(f)
	w.writerow(list500)
