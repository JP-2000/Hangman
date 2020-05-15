import os
import csv
import random


emvlist=[]
hmvlist=[]


with open("C:/Users/Jiten Patel/Desktop/hangman/movies/e_list.csv") as f:
	r=csv.reader(f)
	count=0
	for row in r:
		emvlist=row


with open("C:/Users/Jiten Patel/Desktop/hangman/movies/h_list.csv") as f: 
	r=csv.reader(f)
	count=0
	for row in r:
		hmvlist=row
print(len(emvlist))
print(len(hmvlist))

running = True
while running == True:
	
	running_2 = True 
	while running_2 == True:
		count = 0 
		if running_2 == True:
			for i in range (0, len(emvlist)):
				if len(emvlist[i]) > 51 :
					emvlist.pop(i)
					count += 1
					running_2 = False
					break 
				for  j in range(0, len(emvlist[i])):
					if ord(emvlist[i][j]) >= 128:
						emvlist.pop(i)
						count += 1 
						running_2 = False
						break

				if running_2 == False:
					break
		if running_2 == True:
			for i in range (0, len(hmvlist)):
				if len(hmvlist[i]) > 51 :
					hmvlist.pop(i)
					count += 1
					running_2 = False
					break 
				for  j in range(0, len(hmvlist[i])):
					if ord(hmvlist[i][j]) >= 128:
						hmvlist.pop(i)
						count += 1 
						running_2 = False
						break
				if running_2 == False:
					break
		if count == 0:
			running_2 = False
			running = False

for i in range (0, len(emvlist)):
	for  j in range(0, len(emvlist[i])):
		if ord(emvlist[i][j]) >= 128:
			print(emvlist[i][j], emvlist[i])

for i in range (0, len(hmvlist)):
	for  j in range(0, len(hmvlist[i])):
		if ord(hmvlist[i][j]) >= 128:
			print(hmvlist[i][j], hmvlist[i])


print(len(emvlist))
print(len(hmvlist))


