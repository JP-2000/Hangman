import csv
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup



list500=[]


def top100():
	url='https://www.imdb.com/list/ls062911411/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)


def top200():
	url='https://www.imdb.com/list/ls062911411/?sort=moviemeter,asc&st_dt=&mode=detail&page=2'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)


def top300():
	url='https://www.imdb.com/list/ls062911411/?sort=moviemeter,asc&st_dt=&mode=detail&page=3'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)
		
def top400():
	url='https://www.imdb.com/list/ls062911411/?sort=moviemeter,asc&st_dt=&mode=detail&page=4'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)
		
		

def top500():
	url='https://www.imdb.com/list/ls062911411/?sort=moviemeter,asc&st_dt=&mode=detail&page=5'

	uclient = ureq(url)
	urlre=uclient.read()
	uclient.close()
	
	ps=soup(urlre,"html.parser")

	containers=ps.findAll('div',{'class':'lister-item-content'})
	container=containers[0]
	for container in containers:
		list500.append(container.h3.a.text)






print("Hola")

top100();
top200();
top300();
top400()
top500();

with open('e_list.csv','w',newline='') as f:
	w=csv.writer(f)
	w.writerow(list500)


