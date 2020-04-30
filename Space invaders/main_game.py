import random
import pygame
import math
from pygame import mixer
import numpy as np 

#initialize the pygame
pygame.init()

#create screen
screen=pygame.display.set_mode((800,600))

#backgorund
background_img = pygame.image.load('background.jpg')

#backgorund music
mixer.music.load('backgroundmusic.mp3')
mixer.music.play(-1)

#title and icon
pygame.display.set_caption('Bolo Tara RaRa')
icon=pygame.image.load('icon.ico')
pygame.display.set_icon(icon)

#score
score_val = 0
font = pygame.font.Font('computo-monospace.otf', 20)
score_x = 10
score_y = 10

def show_score(x, y):
	score = font.render("Score : " + str(score_val), True, (224, 224, 224))
	screen.blit(score, (x, y))

#gaem over text

gover_font = pygame.font.Font('computo-monospace.otf', 50)
gover_img = pygame.image.load('gameover.jpg')
gover_img_x = 0
gover_img_y = 600
gover_img_y_change = 10

def game_over():
	gover = gover_font.render(" " "YOU DIED"" ", True, (224, 224, 224))
	screen.blit(gover, (200, 500))

#player
player_img=pygame.image.load('player.png')
player_x=380
player_y=520
player_x_change=0

def player(x,y):
	screen.blit(player_img, (x,y))


#enemy
enemy_1_img = []
enemy_2_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
count = []
noe = 10
for i in range(0, noe):
	enemy_1_img.append(pygame.image.load('alien_1.png'))
	enemy_2_img.append(pygame.image.load('alien_2.png'))
	enemy_x.append(random.randint(0, 736))
	enemy_y.append(random.randint(50, 250))
	enemy_x_change.append(3)
	enemy_y_change.append(40)
	count.append(0)
def enemy_1(x, y, i):
	screen.blit(enemy_1_img[i], (x,y))

def enemy_2(x, y, i):
	screen.blit(enemy_2_img[i], (x,y))



#bullet
bullet_img=pygame.image.load('bullet.png')
bullet_x=0
bullet_y=520
bullet_x_change=0
bullet_y_change=10
bullet_state = "ready"

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire" 
	screen.blit(bullet_img, (x+16,y))

def iscollison(bullet_x, bullet_y, enemy_x, enemy_y):
	x = bullet_x - enemy_x
	y = bullet_y - enemy_y
	distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
	
	if distance < 27:
		return True
	else:
		return False

count_img = 0
count_player = 0 

#game loop
running=True
while running:
	screen.fill((0,0,0)) # backgroundcolor

	#background image
	screen.blit(background_img, (0,0))
	
	if count_img == 2:
		if gover_img_y == 0:
			gover_img_y_change = 0
		gover_img_x = 0
		gover_img_y -= gover_img_y_change
		screen.blit(gover_img, (gover_img_x,gover_img_y))
	if gover_img_y == 0:
		game_over()

	
	#showscore
	show_score(score_x, score_y)

	for event in pygame.event.get():  #gets all the events in the screen 
		
		if event.type == pygame.QUIT:   #close button is also an event and whn it is clicked its type changes to pygame.QUIT
			running=False
		
		if event.type == pygame.KEYDOWN: #checks if a keystoke is pressed
			if event.key == pygame.K_LEFT : #checks the key
				player_x_change = -3
			if event.key == pygame.K_RIGHT:
				player_x_change = 3
			if event.key == pygame.K_SPACE and bullet_state == "ready":
				fire_sound = mixer.Sound('fire.wav')
				fire_sound.play()
				fire_bullet(player_x, bullet_y)
				bullet_x=player_x


		if event.type == pygame.KEYUP: #checks if a keystoke is released
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : #checks the key
				player_x_change = 0

	
	#player movement
	player_x += player_x_change  
	
	if player_x <= 0:
		player_x = 0
	elif player_x >= 736:
		player_x = 736

	#enemy movement
	for i in range(0, noe):
		
		#GameOver
		if enemy_y[i] > 470:
			for j in range(0,noe):
				enemy_y[j]= 1000
			count_img=2
			count_player = 1


		enemy_x[i] += enemy_x_change[i]

		if enemy_x[i] <= 0:
			enemy_x_change[i] = 3
			enemy_y[i] += enemy_y_change[i]
			count[i]=1
		
		elif enemy_x[i] >=736:
			enemy_x_change[i] = -3	
			enemy_y[i] += enemy_y_change[i]
			count[i]=2

		if count[i] == 0:	
			enemy_2(enemy_x[i], enemy_y[i], i)
		elif count[i] == 1:
			enemy_2(enemy_x[i], enemy_y[i], i)
		elif count[i] == 2:
			enemy_1(enemy_x[i], enemy_y[i], i)	

		collison=iscollison(bullet_x, bullet_y, enemy_x[i], enemy_y[i])	

		if collison:
			collison_sound = mixer.Sound('collison.wav')
			collison_sound.play()
			bullet_y = 520
			bullet_state = "ready"
			score_val += 10
			enemy_x[i] = random.randint(0, 736)
			enemy_y[i] = 50

		
	
	#bullet movement
	if bullet_y <= 0:
		bullet_state = "ready"
		bullet_y=520
	if bullet_state is "fire":
		bullet_y -= bullet_y_change
		fire_bullet(bullet_x, bullet_y)
		
	if count_player == 0:	
		player(player_x, player_y)

		
	pygame.display.update() #u need to update the screen everytime  