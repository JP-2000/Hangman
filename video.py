# importing libraries 
from PIL import Image
import pygame
import cv2 
import numpy as np 
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Bolo Tara RaRa')
bg_sound = mixer.Sound('coffin_dance.wav')


   
# Create a VideoCapture object and read from input file 

cap = cv2.VideoCapture('coffindance.mkv') 
bg_img = pygame.image.load('sunny.png')

bg_sound_count = 1
running = True
while running:
# Check if camera opened successfully 
	if (cap.isOpened()== False):  
 		print("Error opening video  file") 
   
# Read until video is completed
	# Capture frame-by-frame 
	ret, frame = cap.read() 
	if ret == True:
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		frame = np.rot90(frame)
		frame = pygame.surfarray.make_surface(frame)

		# Display the resulting frame 
		screen.blit(frame, (0, 100))
		if bg_sound_count == 1:
			bg_sound.play()
			bg_sound_count = 2
		pygame.time.delay(26)
		#pygame.time.delay(10)
	else:
		bg_sound.stop()
		cap.release()
		cap = cv2.VideoCapture('coffindance.mkv')

		
	# Break the loop 
	
	   
	# When everything done, release  
	# the video capture object 
	
	   
	# Closes all the frames

	for event in pygame.event.get():  #gets all the events in the screen 
		
		if event.type == pygame.QUIT:   #close button is also an event and whn it is clicked its type changes to pygame.QUIT
			running=False

	pygame.display.update()
