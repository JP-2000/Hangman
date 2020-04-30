from movieslists import emvlist, hmvlist
import pygame 
from pygame import mixer
import random
from pygame  import *
import string
import cv2 
import numpy as np 
# initializing pygame
pygame.init()

# clock
clock = pygame.time.Clock()

# setting screen 
screen = pygame.display.set_mode((800,600))

#music and  sounds
mixer.music.load('bg_music.mp3')
mixer.music.play(-1)
pygame.mixer.set_num_channels(8)
mouse_pressed_sound = mixer.Sound('mouse_pressed.wav')
sound_sound = mixer.Sound('sound_sound.wav')
channel_1 = pygame.mixer.Channel(5)

                    #frame_1
f_1_hangman_sound = mixer.Sound('hover.wav')
hover_counter_1f_1_hover_sound_1 = mixer.Sound('hover.wav')
f_1_hover_sound_1 = mixer.Sound('hover.wav')
f_1_hover_sound_2 = mixer.Sound('hover.wav')

                    #frame_2
f_2_hover_sound_1 = mixer.Sound('hover.wav')
f_2_hover_sound_2 = mixer.Sound('hover.wav')
mouse_pressed_sound = mixer.Sound('mouse_pressed.wav')

                    #frame_3
correct_key_sound = mixer.Sound('correct_key.wav')
wrong_key_sound = mixer.Sound('wrong_key.wav')
coffin_dance_loop_sound = mixer.Sound('coffin_dance.wav')

# title and icon for screen
pygame.display.set_caption('Hangman movies editn')
icon=pygame.image.load('hangman_icon.png')
pygame.display.set_icon(icon)

sound = 'on'
game_loop = True
while game_loop:

    #backgroud image 
    bg = ['mornin.png', 'sunny.png', 'eve.png', 'night.jpg']
    bg_blur = ['mornin_blur.jpg', 'sunny_blur.jpg', 'eve_blur.jpg', 'night_blur.jpg']
    n = random.randint(0, 3)
    background_img = pygame.image.load(bg[n])
    frame_4_bg_img = pygame.image.load(bg_blur[n])

    ############################################ BUTTONS ################################################### 

    # button images
    button_3_img = pygame.image.load('1_button_3.png')
    button_2_img = pygame.image.load('1_button_2.png')
    button_1_img = pygame.image.load('1_button_1.png')
    button_4_img = pygame.image.load('1_button_4.png')
    sound_button_1_img = pygame.image.load('sound_button_1.png')
    sound_button_2_img = pygame.image.load('sound_button_2.png')

    # button text fonts
    b_font_1 = pygame.font.Font('Squiborn DEMO.ttf', 30)
    b_font_2 = pygame.font.Font('Squiborn DEMO.ttf', 35)
    b_font_3 = pygame.font.Font('Squiborn DEMO.ttf', 50)

    ############################################ frame_1 ##################################################

    # hangman name
    hangman_font = pygame.font.Font('Bombtrack Demo.ttf', 150)
    hangman_x = 0
    hangman_y = 0 
    hangman_y_change = 10
    hangman_x_change = 100

    def frame_1(mouse_pressed, hangman_font, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img, f_1_hangman_sound, f_1_hover_sound_1, f_1_hover_sound_2, mouse_pressed_sound, sound_sound):

        #global variables
        global hangman_count, frame, sound, hangman_x, hangman_y, hangman_x_change, hangman_y_change, held, f_1_hover_counter_1, f_1_hover_counter_2  

        # Hangman_Display
        hangman_y += hangman_y_change
        if hangman_y <= 120 and hangman_count == 0:
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
        elif hangman_y <= 120 and hangman_count == 1:
            f_1_hangman_sound.play()
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (0+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
        elif hangman_y <= 120 and hangman_count == 2:
            f_1_hangman_sound.play()
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (0+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (100+40, 125))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
        elif hangman_y <= 120 and hangman_count == 3:
            f_1_hangman_sound.play()
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (0+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (100+40, 120))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (200+40, 120))
            hangman_font_text = hangman_font.render("G", True, color)
            screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
        elif hangman_y <= 120 and hangman_count == 4:
            f_1_hangman_sound.play()
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (0+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (100+40, 120))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (200+40, 120))
            hangman_font_text = hangman_font.render("G", True, color)
            screen.blit(hangman_font_text, (300+40, 120))
            hangman_font_text = hangman_font.render("M", True, color)
            screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
        elif hangman_y <= 120 and hangman_count == 5:
            f_1_hangman_sound.play()
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (0+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (100+40, 120))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (200+40, 120))
            hangman_font_text = hangman_font.render("G", True, color)
            screen.blit(hangman_font_text, (300+40, 120))
            hangman_font_text = hangman_font.render("M", True, color)
            screen.blit(hangman_font_text, (400+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (hangman_x+45, hangman_y))
        elif hangman_y <= 120 and hangman_count == 6:
            f_1_hangman_sound.play()
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (0+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (100+40, 120))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (200+40, 120))
            hangman_font_text = hangman_font.render("G", True, color)
            screen.blit(hangman_font_text, (300+40, 120))
            hangman_font_text = hangman_font.render("M", True, color)
            screen.blit(hangman_font_text, (400+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (500+45, 120))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (hangman_x+40, hangman_y)) 
        else:
            hangman_y = 0
            hangman_x += hangman_x_change
            hangman_count = hangman_count + 1
        if hangman_count >= 7:
            hangman_font_text = hangman_font.render("H", True, color)
            screen.blit(hangman_font_text, (0+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (100+40, 120))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (200+40, 120))
            hangman_font_text = hangman_font.render("G", True, color)
            screen.blit(hangman_font_text, (300+40, 120))
            hangman_font_text = hangman_font.render("M", True, color)
            screen.blit(hangman_font_text, (400+40, 120))
            hangman_font_text = hangman_font.render("A", True, color)
            screen.blit(hangman_font_text, (500+45, 120))
            hangman_font_text = hangman_font.render("N", True, color)
            screen.blit(hangman_font_text, (600+40, 120))    

        #PLAY_GAME
        if (280 + 250 > mouse[0] > 280) and (331 < mouse[1] < 391):
            if sound == 'on' and f_1_hover_counter_1 == 1:
                f_1_hover_sound_1.play()
                f_1_hover_counter_1 = 2
            screen.blit(button_2_img, (265, 140))
            play_button_font_2 = b_font_2.render("PlAY GAME", True, (100, 100, 100))
            screen.blit(play_button_font_2, (340, 345))
            if (mouse_pressed[0] == 1):
                if  held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                    pygame.time.delay(500)
                    frame = 2
                held = True
            else:
                held = False
        else:
            f_1_hover_sound_1.stop()
            f_1_hover_counter_1 = 1
            screen.blit(button_3_img, (280, 150))
            play_button_font_1 = b_font_1.render("PLAY GAME", True, (224, 224, 224))
            screen.blit(play_button_font_1, (352, 347))
        
        #QUIT_GAME
        if (280 + 250 > mouse[0] > 280) and (492 > mouse[1] > 425) :
            if sound == 'on' and f_1_hover_counter_2 == 1:
                f_1_hover_sound_2.play()
                f_1_hover_counter_2 = 2

            screen.blit(button_4_img, (283, 250))
            quit_button_font_2 = b_font_2.render("QUIT GAME", True, (100, 100, 100))
            screen.blit(quit_button_font_2, (348, 440))
            if (mouse_pressed[0] == 1):
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                    pygame.quit()
                    quit()
                held = True
            else:
                held = False
        else:
            f_1_hover_sound_2.stop()
            f_1_hover_counter_2 = 1
            screen.blit(button_1_img, (281, 250))
            quit_button_font_1 = b_font_1.render("QUIT GAME", True, (224, 224, 224))
            screen.blit(quit_button_font_1, (352, 444))

        #SOUND
        if sound == "on":
            screen.blit(sound_button_1_img, (700, 500))
        else:
            screen.blit(sound_button_2_img, (700, 500)) 
        if (764 > mouse[0] > 700) and  (564 > mouse[1] > 500):
            if sound == "on":
                screen.blit(pygame.transform.scale(sound_button_1_img, (80, 80)), (693, 495))
            else:
                screen.blit(pygame.transform.scale(sound_button_2_img, (80, 80)), (693, 495))
            if mouse_pressed[0] == 1:
                sound_sound.play()
                if held == False:
                    if sound == 'on':
                        sound = 'off'
                    else:
                       sound = 'on' 
                held = True
            else:
                held = False 

    ######################################################## frame_2 #################################################################
    def frame_2(mouse_pressed, b_font_3, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img, f_2_hover_sound_1, f_2_hover_sound_2, mouse_pressed_sound, sound_sound):
        
        #GLOBAL_VARIABLES
        global sound, frame, held, lang , f_2_hover_counter_1, f_2_hover_counter_2
        
        #CHOOSE_TEXT
        choose_font = b_font_3.render("CHOOSE :", True, (0, 0, 0))
        screen.blit(choose_font, (330, 150))
    
        #ENGLISH
        if (280 + 250 > mouse[0] > 280) and (231 < mouse[1] < 291):
            if f_2_hover_counter_1 == 1 and sound == 'on':
                f_2_hover_sound_1.play()
                f_2_hover_counter_1 = 2
            screen.blit(button_2_img, (265, 40))
            english_button_font_2 = b_font_2.render("English", True, (100, 100, 100))
            screen.blit(english_button_font_2, (356, 242))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                    pygame.time.delay(500)
                    frame = 3
                    lang = 2
                held = True
            else:
                held = False  
        else:
            f_2_hover_sound_1.stop()
            f_2_hover_counter_1 = 1
            screen.blit(button_3_img, (280, 50))
            english_button_font_1 = b_font_1.render("English", True, (224, 224, 224))
            screen.blit(english_button_font_1, (363, 246))

        #HINDI
        if (280 + 250 > mouse[0] > 280) and (392 > mouse[1] > 325) :
            if f_2_hover_counter_2 == 1 and sound == 'on':
                f_2_hover_sound_2.play()
                f_2_hover_counter_2 = 2
            screen.blit(button_4_img, (283, 150))
            hindi_button_font_2 = b_font_2.render("HINDI", True, (100, 100, 100))
            screen.blit(hindi_button_font_2, (369, 340))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                    pygame.time.delay(500)
                    frame = 3
                    lang = 1
                held = True
            else:
                held = False  
        else:
            f_2_hover_sound_2.stop()
            f_2_hover_counter_2 = 1
            screen.blit(button_1_img, (281, 150))
            hindi_button_font_1 = b_font_1.render("HINDI", True, (224, 224, 224))
            screen.blit(hindi_button_font_1, (376, 344))

        #SOUND
        if sound == "on":
            screen.blit(sound_button_1_img, (700, 500))
        else:
            screen.blit(sound_button_2_img, (700, 500)) 

        if (764 > mouse[0] > 700) and  (564 > mouse[1] > 500):
            if sound == "on":
                screen.blit(pygame.transform.scale(sound_button_1_img, (80, 80)), (693, 495))
            else:
                screen.blit(pygame.transform.scale(sound_button_2_img, (80, 80)), (693, 495))

            if mouse_pressed[0] == 1:
                sound_sound.play()
                if held == False:
                    if sound == 'on':
                        sound = 'off'
                    else:
                       sound = 'on' 
                held = True
            else:
                held = False 

    ######################################################## Frame_3 #############################################################
    #FONTS
    font_1_3 = pygame.font.Font('Choco Bear.otf', 50) 
    font_2_3 = pygame.font.Font('Choco Bear.otf', 30)
    font_3_3 = pygame.font.Font('JMH Typewriter.ttf', 40)
    
    #IMAGES 
    menu_1_img = pygame.image.load('menu_1.png')
    menu_2_img = pygame.image.load('menu_2.png')
    heart_alive_img = pygame.image.load('heart_alive.png')
    heart_ded_img = pygame.image.load('heart_ded.png')

    #MOVIE_SELECTION
    x = random.randrange(0, 100)
    e_movie = emvlist[random.randint(x, 100)]  
    h_movie = hmvlist[random.randint(x, 100)]  

    #txtboxes:
    t_x_list = []
    t_x_list.clear()
    t_y_list = []
    t_y_list.clear()
    t_x = 60
    t_y = 145 
    t_x_change = 40
    t_y_change = 100
    t_w = 35
    t_h = 50

    #hearts 
    hearts_x_list = []
    hearts_x_list.clear()
    h_x = 5
    h_x_change = 35
    for i in range(0, 9):
        hearts_x_list.append(h_x)
        h_x += h_x_change 

    def frame_3(lang, font_1_3, font_2_3, font_3_3, menu_1_img, menu_2_img, heart_alive_img, heart_ded_img, e_movie, h_movie, t_x, t_y, t_x_change, t_y_change, t_w, t_h, h_x,h_x_change, mouse_pressed, mouse, correct_key_sound, wrong_key_sound, coffin_dance_loop_sound, mouse_pressed_sound, sound_sound):
        
        #GLOBAL_VARIABLES
        global t_x_list, t_y_list, hearts_x_list, hearts_counter, line_set, letters_index_no_list, frame, held, ans_index_list, ans, ans_lower, sound, game_status, coffin_dance_loop_sound_counter
        
        #GUESS_MOVIE_TXT
        font_1_3_text = font_1_3.render("GUESS THE MOVIE : ", True, color)
        screen.blit(font_1_3_text, (50, 50))    

        #INSTRUCTIONS
        font_2_3_space = font_2_3.render("' / ' - SPACE", True, color)
        screen.blit(font_2_3_space, (50, 460)) 
        font_2_3_vowel = font_2_3.render("' ' ' - VOWEL", True, color)
        screen.blit(font_2_3_vowel, (50 + 200, 460)) 
        font_2_3_number = font_2_3.render("' ^ ' - NUMBER", True, color)
        screen.blit(font_2_3_number, (50 + 400, 460))

        #DISPLAY_QUESTION
        if lang == 1:
            ans = h_movie
        else:
            ans = e_movie
        ans2 = 'X'
        ans_lower = ans.lower()
        
        if len(ans) <= 12:
            no_of_letters = 2
        elif len(ans) <= 17:
            no_of_letters = 3
        else:
            no_of_letters = 4

        for i in range(0, no_of_letters):
            if (len(letters_index_no_list) == no_of_letters):
                break
            letter_index_no = random.randint(1, (len(ans)-1))
            
            while ((ans[letter_index_no].isalpha() != True) and (ans[letter_index_no].isnumeric() != True )) or (letter_index_no in letters_index_no_list):
                letter_index_no = random.randint(1, (len(ans)-1))
            letters_index_no_list.append(letter_index_no)

        for i in range(0, len(letters_index_no_list)):
            ans_index_list.append(letters_index_no_list[i])

        for i in range(0, len(ans)):
            if i in letters_index_no_list:
                ans2 += ans[i]
            else:
                ans2 += ' '
        
        if len(ans) > 17:
            line_set = 1

        if line_set == 0:
            t_x = 400 - 17.5
            t_y = 245
            for i in range(0, len(ans)): 
                if len(t_x_list) == len(ans):
                    break                              
                if i == int(len(ans)/2):
                    for j  in range (i, -1, -1):
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x -= t_x_change
                    t_x = 400 - 17.5 + t_x_change
                    for j in range  (i+1, len(ans)):
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x += t_x_change                    
                    break
                else:
                    continue

            mid = int(len(ans) / 2)
            for i in range(0, mid + 1):
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color)
                screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color)
                        screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color)
                    screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], -1)
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color)
                    screen.blit(font_1_3_character, ((t_x_list[mid - i] + 12), (t_y_list[mid - i] - 8)))
            for i in range(mid + 1, len(ans)):
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color)
                        screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

            for i in ans_index_list:
                if i >= 0 and i <= mid:
                    font_1_3_character = font_3_3.render(ans[i], True, color)
                    screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
                else:
                    font_1_3_character = font_3_3.render(ans[i], True, color)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))

        if line_set == 1:
            j = 0
            t_x = 60
            t_y = 145
            while True:
                count_space = 0
                if len(t_x_list) == len(ans):
                    break
                for j in range(j, len(ans)):                    
                    if ans[j] == ' ':
                        count_space += 1
                    if t_x > 700 and count_space != 0:
                        if ans[j] == ' ':
                            t_x_list.append(t_x)
                            t_y_list.append(t_y)
                            j = j+1 
                            break  
                        j = j - 1
                        while ans[j] != " ":
                            t_x_list.pop(j)
                            t_y_list.pop(j)
                            j = j - 1
                        j = j + 1
                        t_y += t_y_change
                        t_x = 60
                        break                       
                    elif t_x > 700 and count_space == 0:  
                        t_x = 60
                        t_y += t_y_change
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x += t_x_change
                    else:                           
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x += t_x_change

            for i in range (0, len(ans)):
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color)
                        screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
                    font_1_3_character = font_1_3.render('/', True, color)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

            for i in ans_index_list:
                font_1_3_character = font_3_3.render(ans[i], True, color)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))

        #MENU_DISPLAY
        if (746 < mouse[0] < 778) and (28 < mouse[1] < 60):
            screen.blit(pygame.transform.scale(menu_2_img, (38, 38)), (742, 25))
            if mouse_pressed[0] == 1:
                if sound == 'on':
                    mouse_pressed_sound.play()
                if held == False:
                    frame = 4 
                held = True
            else:
                held = False  
        else:
            screen.blit(pygame.transform.scale(menu_1_img, (32, 32)), (746, 28))

        #HEARTS
        for i in range(0, 9):
            screen.blit(heart_ded_img, (hearts_x_list[i], 5))

        for i in range(hearts_counter, 9):
            screen.blit(heart_alive_img, (hearts_x_list[i], 5)) 

        #GAME_STATUS
        check_game_status_count = 0
        for i in range(0, len(ans)):
            if ans[i] == ' ':
                check_game_status_count += 1
                continue
            if ans[i] == ':' or  ans[i] == "'" or ans[i] == ',' or ans[i] == '-' or ans[i] == '!' or ans[i] == '.' or ans[i] == '(' or ans[i] == ')':
                check_game_status_count += 1
                continue
            if i in ans_index_list:
                check_game_status_count += 1

        if (hearts_counter <= 9) and (len(ans) == check_game_status_count):
            game_status = "win"            
        if hearts_counter > 8:
            game_status = "lose"
        
        if game_status == "win":
            frame = 6
        if game_status == "lose":
            frame = 5            

    ####################################################################### Frame_4 #########################################################################################

    #IMAGES
    home_img = pygame.image.load('home.png')
    play_img = pygame.image.load('play.png')
    quit_img = pygame.image.load('quit.png')

    #FONTS
    pause_font = pygame.font.Font('Bombtrack Demo.ttf', 100)

    def frame_4(home_img, play_img, quit_img, pause_font,mouse_pressed, mouse, sound_button_1_img, sound_button_2_img, frame_4_bg_img, color, mouse_pressed_sound, sound_sound):
        
        #GLOBAL_VARIABLES
        global frame, held, sound, game_loop, game_loop_2
        
        #PAUSE_TXT        
        screen.blit(frame_4_bg_img, (0, 0))
        pause_txt = pause_font.render('PAUSE', True, color)
        screen.blit(pause_txt, (265, 150))
        
        #MENU_OPTIONS
        screen.blit(home_img, (220 + 8, 300))
        screen.blit(play_img, (320 + 8, 300))
        screen.blit(pygame.transform.scale(quit_img, (55, 55)), (420 + 8, 300))
        screen.blit(sound_button_1_img, (520 + 8, 300))        
        if sound == "on":
            screen.blit(sound_button_1_img, (520 + 8, 300))
        else:
            screen.blit(sound_button_2_img, (520 + 8, 300)) 
        if (220 < mouse[0] < 220 + 64) and (300 < mouse[1] < 300 + 64):
            screen.blit(pygame.transform.scale(home_img, (85, 85)), (217, 292))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                        pygame.time.delay(500)
                    game_loop_2 = False                     
                held = True
            else:
                held = False 
        if (320 < mouse[0] < 320 + 64) and (300 < mouse[1] < 300 + 64):
            screen.blit(pygame.transform.scale(play_img, (85, 85)), (317, 292))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                        pygame.time.delay(500)
                    frame = 3                     
                held = True
            else:
                held = False 
        if (420 < mouse[0] < 420 + 64) and (300 < mouse[1] < 300 + 64):
            screen.blit(quit_img, (423, 298))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                        pygame.time.delay(500)
                    game_loop_2 = False
                    game_loop = False                     
                held = True
            else:
                held = False 
        if (520 < mouse[0] < 520 + 64) and (300 < mouse[1] < 300 + 64):                
            if sound == "on":
                screen.blit(pygame.transform.scale(sound_button_1_img, (85, 85)), (517, 292))
            else:
                screen.blit(pygame.transform.scale(sound_button_2_img, (85, 85)), (517, 292))
            if mouse_pressed[0] == 1:
                if held == False:
                    sound_sound.play()
                    if sound == "on":
                        sound = "off"
                    else:
                        sound = "on"
                held = True
            else:
                held = False 

    ############################################################ frame_5 ##################################################################################

    #IMAGES
    nibba_img = pygame.image.load('nibba.png')
    frame_5_bg_img = pygame.image.load('space.jpg')

    #FONTS
    ded_font = pygame.font.Font('go3v2.ttf', 80)
    f_5_button_font = pygame.font.Font('go3v2.ttf', 30)
    ans_font = pygame.font.Font('JMH Typewriter.ttf', 20)

    #VARIABLES
    n_y = -500
    n_y_change = 8
    d_y = 600

    def frame_5(ans, sound_button_1_img, sound_button_2_img, nibba_img, frame_5_bg_img, ded_font, f_5_button_font, n_y_change, mouse, mouse_pressed,button_1_img, button_3_img, mouse_pressed_sound):
        
        #GLOBAL_VARIABLES
        global frame, held, game_loop, game_loop_2, sound, n_y, d_y
        
        #AKSAY
        screen.blit(frame_5_bg_img, (0,0))
        if n_y <= 30:
            n_y += n_y_change
        screen.blit(nibba_img, (200, n_y))
        if d_y >= 380:
            d_y -= 8
        
        #YOU_DED_TXT
        ded_txt = ded_font.render('YOU DED', True, (150, 150, 150))
        screen.blit(ded_txt, (245, d_y))

        #ANSWER
        ans_txt = ans_font.render("[Ans: " + ans + "]", True, (180, 180, 180))
        screen.blit(ans_txt, (10, d_y + 197))

        #BUTTONS
        screen.blit(button_1_img, (80, 330))
        screen.blit(button_1_img, (470, 330))

        play_again_txt = f_5_button_font.render('PLAY AGAIN', True, (224, 224, 224))
        screen.blit(play_again_txt, (125, 518))

        quit_game_txt = f_5_button_font.render('QUIT GAME', True, (224, 224, 224))
        screen.blit(quit_game_txt, (523, 518))

        if (90 < mouse[0] < 90 + 250 ) and (510 < mouse[1] < 510 + 64):
            screen.blit(button_3_img, (80, 325))
            screen.blit(play_again_txt, (125, 515))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                        pygame.time.delay(500) 
                    game_loop_2 = False                     
                held = True
            else:
                held = False 

        if (480 < mouse[0] < 480 +250) and (510 < mouse[1] < 510 + 64):
            screen.blit(button_3_img, (470, 325))
            screen.blit(quit_game_txt, (523, 515))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                        pygame.time.delay(500) 
                    game_loop_2 = False    
                    game_loop = False                 
                held = True
            else:
                held = False 

        #SOUND
        if sound == "on":
            screen.blit(sound_button_1_img, (720, 20))
        else:
            screen.blit(sound_button_2_img, (720, 20)) 

        if (764 > mouse[0] > 700) and  (17 + 64 > mouse[1] > 17):
            if sound == "on":
                screen.blit(pygame.transform.scale(sound_button_1_img, (80, 80)), (713, 15))
            else:
                screen.blit(pygame.transform.scale(sound_button_2_img, (80, 80)), (713, 15))

            if mouse_pressed[0] == 1:
                sound_sound.play()
                if held == False:
                    if sound == 'on':
                        sound = 'off'
                    else:
                       sound = 'on' 
                held = True
            else:
                held = False 

    ########################################################### frame_6 ###################################################################################

    #IMAGES
    ok_img = pygame.image.load('ok.png')
    party_img = pygame.image.load('party.png')
    party_2_img = pygame.image.load('party_2.png')
    circle_1_img = pygame.image.load('circle_1.png')
    circle_2_img = pygame.image.load('circle_2.png')
    rocket_img = pygame.image.load('rocket.png')
    confetti_img = pygame.image.load('confetti.png')

    shift_y = 600

    def frame_6(sound_button_1_img, sound_button_2_img, ok_img, party_img, party_2_img, circle_1_img, circle_2_img, rocket_img, confetti_img, frame_4_bg_img, ded_font, button_3_img, button_1_img, f_5_button_font,mouse, mouse_pressed, mouse_pressed_sound):

        #GLOBAL_VARIABLES
        global frame, held, sound, game_loop, game_loop_2, shift_y

        screen.blit(frame_4_bg_img, (0, 0))
        
        if shift_y > 0:
            shift_y -= 50 

        #PARTY_HATS
        screen.blit(party_img, (135, 300 + shift_y ))
        screen.blit(party_2_img, (545, 300  + shift_y))
        
        #CIRCLES
        screen.blit(circle_2_img, (50 + 205 - 12.5, 100 - 12.5 - 30 + shift_y))
        screen.blit(circle_1_img, (50 + 205 + 2, 100 + 2 - 30 + shift_y))
        
        #HAND_OK
        screen.blit(ok_img, (288, 15 + shift_y))
        
        #YOU_WIN_TXT
        win_txt_2 = ded_font.render('YOU WIN !', True, (0, 0, 0))
        screen.blit(win_txt_2, (245, 380 + shift_y))
        win_txt = ded_font.render('YOU WIN !', True, (255, 214, 51))
        screen.blit(win_txt, (247, 380 + shift_y))
        
        #RIBBONS
        screen.blit(rocket_img, (-100, 370 + shift_y))
        screen.blit(rocket_img, (645, 370 + shift_y))
        screen.blit(confetti_img, (-110, 0 + shift_y))
        screen.blit(confetti_img, (660, 0 + shift_y))

        #BUTTONS
        screen.blit(button_1_img, (80, 330 + shift_y))
        screen.blit(button_1_img, (470, 330 + shift_y))

        play_again_txt = f_5_button_font.render('PLAY AGAIN', True, (224, 224, 224))
        screen.blit(play_again_txt, (125, 518 + shift_y))

        quit_game_txt = f_5_button_font.render('QUIT GAME', True, (224, 224, 224))
        screen.blit(quit_game_txt, (523, 518 + shift_y))

        if (90 < mouse[0] < 90 + 250 ) and (510 < mouse[1] < 510 + 64):
            screen.blit(button_3_img, (80, 325 + shift_y))
            screen.blit(play_again_txt, (125, 515 + shift_y))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                        pygame.time.delay(500) 
                    game_loop_2 = False                     
                held = True
            else:
                held = False 

        if (480 < mouse[0] < 480 +250) and (510 < mouse[1] < 510 + 64):
            screen.blit(button_3_img, (470, 325 + shift_y))
            screen.blit(quit_game_txt, (523, 515 + shift_y))
            if mouse_pressed[0] == 1:
                if held == False:
                    if sound == 'on':
                        mouse_pressed_sound.play()
                        pygame.time.delay(500) 
                    game_loop_2 = False    
                    game_loop = False                 
                held = True
            else:
                held = False 

        #SOUND
        if sound == "on":
            screen.blit(sound_button_1_img, (720, 20 + shift_y))
        else:
            screen.blit(sound_button_2_img, (720, 20 + shift_y)) 

        if (764 > mouse[0] > 700) and  (17 + 64 > mouse[1] > 17):
            if sound == "on":
                screen.blit(pygame.transform.scale(sound_button_1_img, (80, 80)), (713, 15 + shift_y))
            else:
                screen.blit(pygame.transform.scale(sound_button_2_img, (80, 80)), (713, 15 + shift_y))

            if mouse_pressed[0] == 1:
                sound_sound.play()
                if held == False:
                    if sound == 'on':
                        sound = 'off'
                    else:
                       sound = 'on' 
                held = True
            else:
                held = False 

    ############################################ Counters ####################################################

    frame = 1
    hangman_count = 0
    held  = False

    if n == 0 or n == 1 or n == 2:
        color = (0, 0, 0)
    else:
        color = (224, 224, 224)

    if n == 0 or n == 1 :
        color_2 = (0, 80, 130)
    elif n == 2 :
        color_2 = (9, 81, 105)
    else:
        color_2 = (5, 155,154)

    line_set = 0
    letters_index_no_list = []
    letters_index_no_list.clear()
    hearts_counter = 0
    ans_index_list = []
    ans_index_list.clear()
    game_status = "wubalubadubdub"

    f_1_hover_counter_1 = 1
    f_1_hover_counter_2 = 1
    f_2_hover_counter_1 = 1
    f_2_hover_counter_2 = 1

    ###################################################### MAIN_GAME_LOOP ####################################################################3

    game_loop_2 = True
    while game_loop_2:
        
        clock.tick(60)

        screen.fill((0, 0, 0))
        
        screen.blit(background_img, (0, 0))

        mouse = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if sound == 'off':
            mixer.music.set_volume(0)
        else:
            mixer.music.set_volume(0.5)

        if frame == 1:  
            frame_1(mouse_pressed, hangman_font, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img, f_1_hangman_sound, f_1_hover_sound_1, f_1_hover_sound_2, mouse_pressed_sound, sound_sound)    
            
        if frame == 2:
            frame_2(mouse_pressed, b_font_3, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img, f_2_hover_sound_1, f_2_hover_sound_2, mouse_pressed_sound,  sound_sound)
        
        if frame == 3:
            frame_3(lang, font_1_3, font_2_3, font_3_3, menu_1_img, menu_2_img, heart_alive_img, heart_ded_img, e_movie, h_movie, t_x, t_y, t_x_change, t_y_change, t_w, t_h, h_x,h_x_change, mouse_pressed, mouse, correct_key_sound, wrong_key_sound, coffin_dance_loop_sound, mouse_pressed_sound, sound_sound)        
        
        if frame == 4:
            frame_4(home_img, play_img, quit_img, pause_font,mouse_pressed, mouse, sound_button_1_img, sound_button_2_img, frame_4_bg_img, color, mouse_pressed_sound, sound_sound)

        if frame == 5:
            frame_5(ans, sound_button_1_img, sound_button_2_img, nibba_img, frame_5_bg_img, ded_font, f_5_button_font, n_y_change, mouse, mouse_pressed,button_1_img, button_3_img, mouse_pressed_sound)

        if frame == 6:
            frame_6(sound_button_1_img, sound_button_2_img, ok_img, party_img, party_2_img, circle_1_img, circle_2_img, rocket_img, confetti_img, frame_4_bg_img, ded_font, button_3_img, button_1_img, f_5_button_font,mouse, mouse_pressed, mouse_pressed_sound)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop_2 = False
                game_loop = False
            if event.type == pygame.KEYDOWN:
                if frame == 3:
                    character = chr(event.key)
                    if (64 < ord(character) < 91) or (96 < ord(character) < 123) or (character.isnumeric() == True):
                        if character in ans_lower:
                            if sound == 'on':
                                correct_key_sound.play()
                            for i in range(0, len(ans_lower)):
                                if character == ans_lower[i]:
                                    ans_index_list.append(i)
                        else:
                            if sound == 'on':
                                wrong_key_sound.play()
                            hearts_counter += 1
        pygame.display.update()

    