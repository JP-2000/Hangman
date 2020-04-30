for k in range(0, len(ans)):
    if ans[j].isalpha() == True:
        if t_x > 750:
            t_y += t_y_change
            t_x = 50
        screen.draw.rect(screen, color, [t_x, t_y, t_w, t_h], 3)
    elif ans[j].isnumeric() == True: 
        if t_x > 750:
            t_y += t_y_change
            t_x = 50
        screen.draw.rect(screen, color, [t_x, t_y, t_w, t_h], 3)
        font_1_3_num_sym = font_1_3.render('^', True, color_2)
        screen.blit(font_1_3_num_sym, ((t_x + 8), (t_y + 43 )))
    elif ans[j] == " ":
        if t_x > 750:
            t_y += t_y_change
            t_x = 50
        screen.draw.rect(screen, color, [t_x, t_y, t_w, t_h], -1)
    else:
        if t_x > 750:
            t_y += t_y_change
            t_x = 50
        font_1_3_character = font_3_3.render('A', True, color_2)
        screen.blit(font_1_3_character, ((400 - 17.5 + 5), (170 - 25 + 5)))









for i in range(0, len(ans)):
                if len(ans) % 2 != 0:  #checks odd no of letters 
                    if i == (len(ans) / 2):  # checks middle character 
                        for j in range(i, -1):
                            if t_x < 50:
                                line_set = 1 
                            else:                            
                                t_x -= t_x_change
                        for j in range(i, len(ans)):
                            print("ncalncl")
                        break
                    
                else:
                    if i == (len(ans) / 2):
                        for j in range(i-1, -1):
                            print('dbddadkcb')
                        for j in range(i+1, len(ans)):
                            print('kskksbd')
                            break

        





        #pygame.draw.rect(screen, (100, 100, 100), [50 , 120, 700, 300], 3)
        pygame.draw.rect(screen, (100, 100, 100), [(400 - 17.5), (270 - 25), 35, 50], 3)
        #pygame.draw.rect(screen, (100, 100, 100), [(400 - 17.5 + 35 +5 ), (270 - 25), 35, 50], -1)
        #pygame.draw.rect(screen, (100, 100, 100), [(400 - 17.5), (170 - 25), 35, 50], 3)
        #pygame.draw.rect(screen, (100, 100, 100), [(400 - 17.5), (370 - 25), 35, 50], 3)
        #font_1_3_num_sym = font_1_3.render('^', True, color_2)
        #screen.blit(font_1_3_num_sym, ((400 - 17.5 + 8), (170 - 25 + 43 )))
        font_1_3_character = font_3_3.render("A", True, color_2)
        screen.blit(font_1_3_character, ((400 - 17.5 + 3), (270 - 25 + 3)))
















        ########### Display various fonts for frame 3 #################

        font_1_3_text = font_1_3.render("GUESS THE MOVIE : ", True, color_2)
        screen.blit(font_1_3_text, (50, 50))    

        font_2_3_space = font_2_3.render("' / ' - SPACE", True, color_2)
        screen.blit(font_2_3_space, (50, 460)) 
        font_2_3_vowel = font_2_3.render("' ' ' - VOWEL", True, color_2)
        screen.blit(font_2_3_vowel, (50 + 200, 460)) 
        font_2_3_number = font_2_3.render("' ^ ' - NUMBER", True, color_2)
        screen.blit(font_2_3_number, (50 + 400, 460))

        
        ########### Display Question #############
        ans = h_movie
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
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color_2)
                        screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], -1)
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[mid - i] + 12), (t_y_list[mid - i] - 8)))
            for i in range(mid + 1, len(ans)):
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color_2)
                        screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

            for i in ans_index_list:
                if i >= 0 and i <= mid:
                    font_1_3_character = font_3_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
                else:
                    font_1_3_character = font_3_3.render(ans[i], True, color_2)
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
                    elif t_x > 700 and count_space == 0:   #without space condition
                        t_x = 60
                        t_y += t_y_change
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x += t_x_change
                    else:                               #normal condition
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x += t_x_change

            for i in range (0, len(ans)):
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color_2)
                        screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
                    font_1_3_character = font_1_3.render('/', True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

            for i in ans_index_list:
                font_1_3_character = font_3_3.render(ans[i], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))


        ######## Display Menu ############

        if (746 < mouse[0] < 778) and (28 < mouse[1] < 60):
            screen.blit(pygame.transform.scale(menu_2_img, (38, 38)), (742, 25))
        else:
            screen.blit(pygame.transform.scale(menu_1_img, (32, 32)), (746, 28))


        ######### Display hearts#########

        for i in range(0, 9):
            screen.blit(heart_ded_img, (hearts_x_list[i], 5))

        for i in range(hearts_counter, 9):
            screen.blit(heart_alive_img, (hearts_x_list[i], 5))







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            print(chr(event.key))
            character = chr(event.key)
            if character in ans_lower:
                for i in range(0, len(ans_lower)):
                    if character == ans_lower[i]:
                        ans_index_list.append(i)
            else:
                hearts_counter += 1

   
    pygame.display.update()




    #####################################################################################################################################################
from movieslists import emvlist, hmvlist
import pygame 
from pygame import mixer
import random
from pygame  import *
import string

# initializing pygame
pygame.init()
# clock
clock = pygame.time.Clock()

# setting screen 
screen = pygame.display.set_mode((800,600))


# title and icon for screen
pygame.display.set_caption('Hangman movies editn')
icon=pygame.image.load('hangman_icon.png')
pygame.display.set_icon(icon)

#backgroud image 
bg = ['mornin.png', 'sunny.png', 'eve.png', 'night.jpg']
n = random.randint(0, 3)
background_img = pygame.image.load(bg[n])




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



############################################ Counters ####################################################


frame = 3
hangman_count = 0
sound = 'on '
held  = False
if n == 0 or n == 1 or n == 2:
    color = (0, 0, 0)
else:
    color = (224, 224, 224)
if n == 0 or n == 1 or n == 2:
    color_2 = (0, 0, 0)
else:
    color_2 = (224, 224, 224)

line_set = 0
count_space = 0
letters_index_no_list = [] 
hearts_counter = 0
ans_index_list = []

############################################ frame_1 ##################################################

# hangman name
hangman_font = pygame.font.Font('Bombtrack Demo.ttf', 150)
hangman_x = 0
hangman_y = 0 
hangman_y_change = 10
hangman_x_change = 100

def frame_1(mouse_pressed, hangman_font, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img):
    global hangman_count, frame, sound, hangman_x, hangman_y, hangman_x_change, hangman_y_change, held  

    hangman_y += hangman_y_change
    if hangman_y <= 120 and hangman_count == 0:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 1:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (0+40, 120))
        hangman_font_text = hangman_font.render("A", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 2:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (0+40, 120))
        hangman_font_text = hangman_font.render("A", True, color)
        screen.blit(hangman_font_text, (100+40, 125))
        hangman_font_text = hangman_font.render("N", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 3:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (0+40, 120))
        hangman_font_text = hangman_font.render("A", True, color)
        screen.blit(hangman_font_text, (100+40, 120))
        hangman_font_text = hangman_font.render("N", True, color)
        screen.blit(hangman_font_text, (200+40, 120))
        hangman_font_text = hangman_font.render("G", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 4:
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

    if (280 + 250 > mouse[0] > 280) and (331 < mouse[1] < 391):
        screen.blit(button_2_img, (265, 140))
        play_button_font_2 = b_font_2.render("PlAY GAME", True, (100, 100, 100))
        screen.blit(play_button_font_2, (340, 345))
        if (mouse_pressed[0] == 1):
            if  held == False:
                frame = 2
            held = True
        else:
            held = False
    else:
        screen.blit(button_3_img, (280, 150))
        play_button_font_1 = b_font_1.render("PLAY GAME", True, (224, 224, 224))
        screen.blit(play_button_font_1, (352, 347))
    
    if (280 + 250 > mouse[0] > 280) and (492 > mouse[1] > 425) :
        screen.blit(button_4_img, (283, 250))
        quit_button_font_2 = b_font_2.render("QUIT GAME", True, (100, 100, 100))
        screen.blit(quit_button_font_2, (348, 440))
        if (mouse_pressed[0] == 1):
            if held == False:
                pygame.quit()
                quit()
            held = True
        else:
            held = False
    else:
        screen.blit(button_1_img, (281, 250))
        quit_button_font_1 = b_font_1.render("QUIT GAME", True, (224, 224, 224))
        screen.blit(quit_button_font_1, (352, 444))

    if sound == "on":
        screen.blit(sound_button_1_img, (700, 500))
    else:
        screen.blit(sound_button_2_img, (700, 500)) 

    if (764 > mouse[0] > 700) and  (564 > mouse[1] > 500):
        if mouse_pressed[0] == 1:
            if held == False:
                if sound == 'on':
                    sound = 'off'
                else:
                   sound = 'on' 
                print('True')
            held = True
        else:
            held = False 

######################################################## frame_2 #################################################################
def frame_2(mouse_pressed, b_font_3, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img):
    global sound, frame, held
    
    
    choose_font = b_font_3.render("CHOOSE :", True, (0, 0, 0))
    screen.blit(choose_font, (330, 150))
        
    if (280 + 250 > mouse[0] > 280) and (231 < mouse[1] < 291):
        screen.blit(button_2_img, (265, 40))
        english_button_font_2 = b_font_2.render("English", True, (100, 100, 100))
        screen.blit(english_button_font_2, (356, 242))
        if mouse_pressed[0] == 1:
            if held == False:
                frame=3
            held = True
        else:
            held = False  
    else:
        screen.blit(button_3_img, (280, 50))
        english_button_font_1 = b_font_1.render("English", True, (224, 224, 224))
        screen.blit(english_button_font_1, (363, 246))

    if (280 + 250 > mouse[0] > 280) and (392 > mouse[1] > 325) :
        screen.blit(button_4_img, (283, 150))
        hindi_button_font_2 = b_font_2.render("HINDI", True, (100, 100, 100))
        screen.blit(hindi_button_font_2, (369, 340))
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            if held == False:
                frame=3
            held = True
        else:
            held = False  
    else:
        screen.blit(button_1_img, (281, 150))
        hindi_button_font_1 = b_font_1.render("HINDI", True, (224, 224, 224))
        screen.blit(hindi_button_font_1, (376, 344))


    if sound == "on":
        screen.blit(sound_button_1_img, (700, 500))
    else:
        screen.blit(sound_button_2_img, (700, 500)) 

    if (764 > mouse[0] > 700) and  (564 > mouse[1] > 500):
        if mouse_pressed[0] == 1:
            if held == False:
                if sound == 'on':
                    sound = 'off'
                else:
                    sound = 'on' 
            
            held = True
        else:
            held = False 

######################################################## Frame_3 #############################################################
font_1_3 = pygame.font.Font('Choco Bear.otf', 50) 
font_2_3 = pygame.font.Font('Choco Bear.otf', 30)
font_3_3 = pygame.font.Font('JMH Typewriter.ttf', 40)
 


menu_1_img = pygame.image.load('menu_1.png')
menu_2_img = pygame.image.load('menu_2.png')
heart_alive_img = pygame.image.load('heart_alive.png')
heart_ded_img = pygame.image.load('heart_ded.png')

e_movie = emvlist[random.randint(0, 100)]  
h_movie = hmvlist[random.randint(0, 100)]  


#txtboxes:
t_x_list = []
t_y_list = []
t_x = 60
t_y = 145 
t_x_change = 40
t_y_change = 100
t_w = 35
t_h = 50

#hearts 
hearts_x_list = []
h_x = 5
h_x_change = 35

for i in range(0, 9):
    hearts_x_list.append(h_x)
    h_x += h_x_change 



###################################################### MAIN_GAME_LOOP ####################################################################3
game_loop = True
while game_loop:
    
    clock.tick(60)

    screen.fill((0, 0, 0))
    
    screen.blit(background_img, (0, 0))

    mouse = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    if frame == 1:  
        frame_1(mouse_pressed, hangman_font, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img)    
        
    if frame == 2:
        frame_2(mouse_pressed, b_font_3, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img)
    
    if frame == 3:
        
        ########### Display various fonts for frame 3 #################

        font_1_3_text = font_1_3.render("GUESS THE MOVIE : ", True, color_2)
        screen.blit(font_1_3_text, (50, 50))    

        font_2_3_space = font_2_3.render("' / ' - SPACE", True, color_2)
        screen.blit(font_2_3_space, (50, 460)) 
        font_2_3_vowel = font_2_3.render("' ' ' - VOWEL", True, color_2)
        screen.blit(font_2_3_vowel, (50 + 200, 460)) 
        font_2_3_number = font_2_3.render("' ^ ' - NUMBER", True, color_2)
        screen.blit(font_2_3_number, (50 + 400, 460))

        
        ########### Display Question #############
        ans = h_movie
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
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color_2)
                        screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], -1)
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[mid - i] + 12), (t_y_list[mid - i] - 8)))
            for i in range(mid + 1, len(ans)):
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color_2)
                        screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

            for i in ans_index_list:
                if i >= 0 and i <= mid:
                    font_1_3_character = font_3_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
                else:
                    font_1_3_character = font_3_3.render(ans[i], True, color_2)
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
                    elif t_x > 700 and count_space == 0:   #without space condition
                        t_x = 60
                        t_y += t_y_change
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x += t_x_change
                    else:                               #normal condition
                        t_x_list.append(t_x)
                        t_y_list.append(t_y)
                        t_x += t_x_change

            for i in range (0, len(ans)):
                font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
                if ans[i].isalpha() == True:
                    if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                        font_1_3_num_sym = font_1_3.render("'", True, color_2)
                        screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                    else:
                        pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                elif ans[i].isnumeric() == True: 
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render('^', True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
                elif ans[i] == " ":
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
                    font_1_3_character = font_1_3.render('/', True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))
                else:
                    font_1_3_character = font_1_3.render(ans[i], True, color_2)
                    screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

            for i in ans_index_list:
                font_1_3_character = font_3_3.render(ans[i], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))


        ######## Display Menu ############

        if (746 < mouse[0] < 778) and (28 < mouse[1] < 60):
            screen.blit(pygame.transform.scale(menu_2_img, (38, 38)), (742, 25))
        else:
            screen.blit(pygame.transform.scale(menu_1_img, (32, 32)), (746, 28))


        ######### Display hearts#########

        for i in range(0, 9):
            screen.blit(heart_ded_img, (hearts_x_list[i], 5))

        for i in range(hearts_counter, 9):
            screen.blit(heart_alive_img, (hearts_x_list[i], 5))







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            print(chr(event.key))
            character = chr(event.key)
            if character in ans_lower:
                for i in range(0, len(ans_lower)):
                    if character == ans_lower[i]:
                        ans_index_list.append(i)
            else:
                hearts_counter += 1

   
    pygame.display.update()


    

#########################################################################################################################################################################################
from movieslists import emvlist, hmvlist
import pygame 
from pygame import mixer
import random
from pygame  import *
import string

# initializing pygame
pygame.init()
# clock
clock = pygame.time.Clock()

# setting screen 
screen = pygame.display.set_mode((800,600))


# title and icon for screen
pygame.display.set_caption('Hangman movies editn')
icon=pygame.image.load('hangman_icon.png')
pygame.display.set_icon(icon)

#backgroud image 
bg = ['mornin.png', 'sunny.png', 'eve.png', 'night.jpg']
n = random.randint(0, 3)
background_img = pygame.image.load(bg[n])



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



############################################ Counters ####################################################


frame = 3
hangman_count = 0
sound = 'on '
held  = False
if n == 0 or n == 1 or n == 2:
    color = (0, 0, 0)
else:
    color = (224, 224, 224)
if n == 0 or n == 1 or n == 2:
    color_2 = (0, 0, 0)
else:
    color_2 = (224, 224, 224)

line_set = 0
letters_index_no_list = [] 
hearts_counter = 0
ans_index_list = []

############################################ frame_1 ##################################################

# hangman name
hangman_font = pygame.font.Font('Bombtrack Demo.ttf', 150)
hangman_x = 0
hangman_y = 0 
hangman_y_change = 10
hangman_x_change = 100

def frame_1(mouse_pressed, hangman_font, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img):
    global hangman_count, frame, sound, hangman_x, hangman_y, hangman_x_change, hangman_y_change, held  

    hangman_y += hangman_y_change
    if hangman_y <= 120 and hangman_count == 0:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 1:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (0+40, 120))
        hangman_font_text = hangman_font.render("A", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 2:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (0+40, 120))
        hangman_font_text = hangman_font.render("A", True, color)
        screen.blit(hangman_font_text, (100+40, 125))
        hangman_font_text = hangman_font.render("N", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 3:
        hangman_font_text = hangman_font.render("H", True, color)
        screen.blit(hangman_font_text, (0+40, 120))
        hangman_font_text = hangman_font.render("A", True, color)
        screen.blit(hangman_font_text, (100+40, 120))
        hangman_font_text = hangman_font.render("N", True, color)
        screen.blit(hangman_font_text, (200+40, 120))
        hangman_font_text = hangman_font.render("G", True, color)
        screen.blit(hangman_font_text, (hangman_x+40, hangman_y))
    elif hangman_y <= 120 and hangman_count == 4:
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

    if (280 + 250 > mouse[0] > 280) and (331 < mouse[1] < 391):
        screen.blit(button_2_img, (265, 140))
        play_button_font_2 = b_font_2.render("PlAY GAME", True, (100, 100, 100))
        screen.blit(play_button_font_2, (340, 345))
        if (mouse_pressed[0] == 1):
            if  held == False:
                frame = 2
            held = True
        else:
            held = False
    else:
        screen.blit(button_3_img, (280, 150))
        play_button_font_1 = b_font_1.render("PLAY GAME", True, (224, 224, 224))
        screen.blit(play_button_font_1, (352, 347))
    
    if (280 + 250 > mouse[0] > 280) and (492 > mouse[1] > 425) :
        screen.blit(button_4_img, (283, 250))
        quit_button_font_2 = b_font_2.render("QUIT GAME", True, (100, 100, 100))
        screen.blit(quit_button_font_2, (348, 440))
        if (mouse_pressed[0] == 1):
            if held == False:
                pygame.quit()
                quit()
            held = True
        else:
            held = False
    else:
        screen.blit(button_1_img, (281, 250))
        quit_button_font_1 = b_font_1.render("QUIT GAME", True, (224, 224, 224))
        screen.blit(quit_button_font_1, (352, 444))

    if sound == "on":
        screen.blit(sound_button_1_img, (700, 500))
    else:
        screen.blit(sound_button_2_img, (700, 500)) 

    if (764 > mouse[0] > 700) and  (564 > mouse[1] > 500):
        if mouse_pressed[0] == 1:
            if held == False:
                if sound == 'on':
                    sound = 'off'
                else:
                   sound = 'on' 
                print('True')
            held = True
        else:
            held = False 

######################################################## frame_2 #################################################################
def frame_2(mouse_pressed, b_font_3, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img):
    global sound, frame, held
    
    
    choose_font = b_font_3.render("CHOOSE :", True, (0, 0, 0))
    screen.blit(choose_font, (330, 150))
        
    if (280 + 250 > mouse[0] > 280) and (231 < mouse[1] < 291):
        screen.blit(button_2_img, (265, 40))
        english_button_font_2 = b_font_2.render("English", True, (100, 100, 100))
        screen.blit(english_button_font_2, (356, 242))
        if mouse_pressed[0] == 1:
            if held == False:
                frame=3
            held = True
        else:
            held = False  
    else:
        screen.blit(button_3_img, (280, 50))
        english_button_font_1 = b_font_1.render("English", True, (224, 224, 224))
        screen.blit(english_button_font_1, (363, 246))

    if (280 + 250 > mouse[0] > 280) and (392 > mouse[1] > 325) :
        screen.blit(button_4_img, (283, 150))
        hindi_button_font_2 = b_font_2.render("HINDI", True, (100, 100, 100))
        screen.blit(hindi_button_font_2, (369, 340))
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            if held == False:
                frame=3
            held = True
        else:
            held = False  
    else:
        screen.blit(button_1_img, (281, 150))
        hindi_button_font_1 = b_font_1.render("HINDI", True, (224, 224, 224))
        screen.blit(hindi_button_font_1, (376, 344))


    if sound == "on":
        screen.blit(sound_button_1_img, (700, 500))
    else:
        screen.blit(sound_button_2_img, (700, 500)) 

    if (764 > mouse[0] > 700) and  (564 > mouse[1] > 500):
        if mouse_pressed[0] == 1:
            if held == False:
                if sound == 'on':
                    sound = 'off'
                else:
                    sound = 'on' 
            
            held = True
        else:
            held = False 

######################################################## Frame_3 #############################################################
font_1_3 = pygame.font.Font('Choco Bear.otf', 50) 
font_2_3 = pygame.font.Font('Choco Bear.otf', 30)
font_3_3 = pygame.font.Font('JMH Typewriter.ttf', 40)
 


menu_1_img = pygame.image.load('menu_1.png')
menu_2_img = pygame.image.load('menu_2.png')
heart_alive_img = pygame.image.load('heart_alive.png')
heart_ded_img = pygame.image.load('heart_ded.png')

e_movie = emvlist[random.randint(0, 100)]  
h_movie = hmvlist[random.randint(0, 100)]  


#txtboxes:
t_x_list = []
t_y_list = []
t_x = 60
t_y = 145 
t_x_change = 40
t_y_change = 100
t_w = 35
t_h = 50

#hearts 
hearts_x_list = []
h_x = 5
h_x_change = 35

for i in range(0, 9):
    hearts_x_list.append(h_x)
    h_x += h_x_change 


def frame_3(font_1_3, font_2_3, font_3_3, menu_1_img, menu_2_img, heart_alive_img, heart_ded_img, e_movie, h_movie, t_x, t_y, t_x_change, t_y_change, t_w, t_h, h_x,h_x_change, mouse_pressed ):
    ######################## global variables ###################3
    global t_x_list, t_y_list, hearts_x_list, hearts_counter, line_set, letters_index_no_list, frame, held, ans_index_list, ans_lower


    ########### Display various fonts for frame 3 #################

    font_1_3_text = font_1_3.render("GUESS THE MOVIE : ", True, color_2)
    screen.blit(font_1_3_text, (50, 50))    

    font_2_3_space = font_2_3.render("' / ' - SPACE", True, color_2)
    screen.blit(font_2_3_space, (50, 460)) 
    font_2_3_vowel = font_2_3.render("' ' ' - VOWEL", True, color_2)
    screen.blit(font_2_3_vowel, (50 + 200, 460)) 
    font_2_3_number = font_2_3.render("' ^ ' - NUMBER", True, color_2)
    screen.blit(font_2_3_number, (50 + 400, 460))

    
    ########### Display Question #############
    ans = h_movie
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
            font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
            screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
            if ans[i].isalpha() == True:
                if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                    pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render("'", True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 45 )))
                else:
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
            elif ans[i].isnumeric() == True: 
                pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], 3)
                font_1_3_num_sym = font_1_3.render('^', True, color_2)
                screen.blit(font_1_3_num_sym, ((t_x_list[mid - i] + 8), (t_y_list[mid - i] + 43 )))
            elif ans[i] == " ":
                pygame.draw.rect(screen, color, [t_x_list[mid - i], t_y_list[mid - i], t_w, t_h], -1)
            else:
                font_1_3_character = font_1_3.render(ans[i], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[mid - i] + 12), (t_y_list[mid - i] - 8)))
        for i in range(mid + 1, len(ans)):
            font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
            screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
            if ans[i].isalpha() == True:
                if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render("'", True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                else:
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
            elif ans[i].isnumeric() == True: 
                pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                font_1_3_num_sym = font_1_3.render('^', True, color_2)
                screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
            elif ans[i] == " ":
                pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
            else:
                font_1_3_character = font_1_3.render(ans[i], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

        for i in ans_index_list:
            if i >= 0 and i <= mid:
                font_1_3_character = font_3_3.render(ans[i], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[mid - i] + 3), (t_y_list[mid - i] + 3)))
            else:
                font_1_3_character = font_3_3.render(ans[i], True, color_2)
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
                elif t_x > 700 and count_space == 0:   #without space condition
                    t_x = 60
                    t_y += t_y_change
                    t_x_list.append(t_x)
                    t_y_list.append(t_y)
                    t_x += t_x_change
                else:                               #normal condition
                    t_x_list.append(t_x)
                    t_y_list.append(t_y)
                    t_x += t_x_change

        for i in range (0, len(ans)):
            font_1_3_character = font_3_3.render(ans2[i + 1], True, color_2)
            screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))
            if ans[i].isalpha() == True:
                if ans[i] == 'a' or ans[i] == 'e' or ans[i] == 'i' or ans[i] == 'o' or ans[i] == 'u' or ans[i] == 'A' or ans[i] == 'E' or ans[i] == 'I' or ans[i] == 'O' or ans[i] == 'U':
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                    font_1_3_num_sym = font_1_3.render("'", True, color_2)
                    screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 45 )))
                else:
                    pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
            elif ans[i].isnumeric() == True: 
                pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], 3)
                font_1_3_num_sym = font_1_3.render('^', True, color_2)
                screen.blit(font_1_3_num_sym, ((t_x_list[i] + 8), (t_y_list[i] + 43 )))
            elif ans[i] == " ":
                pygame.draw.rect(screen, color, [t_x_list[i], t_y_list[i], t_w, t_h], -1)
                font_1_3_character = font_1_3.render('/', True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))
            else:
                font_1_3_character = font_1_3.render(ans[i], True, color_2)
                screen.blit(font_1_3_character, ((t_x_list[i] + 12), (t_y_list[i] - 8)))

        for i in ans_index_list:
            font_1_3_character = font_3_3.render(ans[i], True, color_2)
            screen.blit(font_1_3_character, ((t_x_list[i] + 3), (t_y_list[i] + 3)))


    ######## Display Menu ############

    if (746 < mouse[0] < 778) and (28 < mouse[1] < 60):
        screen.blit(pygame.transform.scale(menu_2_img, (38, 38)), (742, 25))
    else:
        screen.blit(pygame.transform.scale(menu_1_img, (32, 32)), (746, 28))


    ######### Display hearts#########

    for i in range(0, 9):
        screen.blit(heart_ded_img, (hearts_x_list[i], 5))

    for i in range(hearts_counter, 9):
        screen.blit(heart_alive_img, (hearts_x_list[i], 5))





###################################################### MAIN_GAME_LOOP ####################################################################3
game_loop = True
while game_loop:
    
    clock.tick(60)

    screen.fill((0, 0, 0))
    
    screen.blit(background_img, (0, 0))

    mouse = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    if frame == 1:  
        frame_1(mouse_pressed, hangman_font, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img)    
        
    if frame == 2:
        frame_2(mouse_pressed, b_font_3, mouse, button_1_img, button_2_img, button_3_img, button_4_img, b_font_1, b_font_2, sound_button_1_img, sound_button_2_img)
    
    if frame == 3:
        frame_3(font_1_3, font_2_3, font_3_3, menu_1_img, menu_2_img, heart_alive_img, heart_ded_img, e_movie, h_movie, t_x, t_y, t_x_change, t_y_change, t_w, t_h, h_x,h_x_change, mouse_pressed )        
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            print(chr(event.key))
            character = chr(event.key)
            if character in ans_lower:
                for i in range(0, len(ans_lower)):
                    if character == ans_lower[i]:
                        ans_index_list.append(i)
            else:
                hearts_counter += 1

   
    pygame.display.update()


    

############################################################################################################################################################################################


import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys

camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([1280,720])

try:
    while True:
        ret, frame = camera.read()
        
        screen.fill([0,0,0])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                sys.exit(0)
except (KeyboardInterrupt, SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()


##############################################################################################################################################333
import csv
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


list2000=[]
list2001=[]
list2002=[]
list2003=[]

list500=[]


def year2000():
    
    url='https://en.wikipedia.org/wiki/2000_in_film'

    uclient = ureq(url)
    urlre=uclient.read()
    uclient.close()
    
    ps=soup(urlre,"html.parser")

    mcontainer=ps.find('div',{'class':'mw-parser-output'})
    containers=mcontainer.findAll('ul')
    con=[]
    for i in range(39,58):
        con.append(containers[i])
    contain=con[0]
    for contain in con:
        x=contain.findAll('li')
        y=x[0]
        for y in x:
            list2000.append(y.i.a.text)
    
    
def year2001():
    
    url='https://en.wikipedia.org/wiki/2001_in_film'

    uclient = ureq(url)
    urlre=uclient.read()
    uclient.close()
    
    ps=soup(urlre,"html.parser")

    mcontainer=ps.find('div',{'class':'mw-parser-output'})
    containers=mcontainer.findAll('ul')
    con=[]
    for i in range(39,63):
        con.append(containers[i])
    contain=con[0]
    for contain in con:
        x=contain.findAll('li')
        y=x[0]
        for y in x:
            list2001.append(y.i.a.text)
    

def year2002():
    
    url='https://en.wikipedia.org/wiki/2002_in_film'

    uclient = ureq(url)
    urlre=uclient.read()
    uclient.close()
    
    ps=soup(urlre,"html.parser")

    mcontainer=ps.find('div',{'class':'mw-parser-output'})
    containers=mcontainer.findAll('ul')
    con=[]
    for i in range(37,59):
        con.append(containers[i])
    contain=con[0]
    for contain in con:
        x=contain.findAll('li')
        y=x[0]
        for y in x:
            list2002.append(y.i.a.text)
    


def year2003():
    
    url='https://en.wikipedia.org/wiki/2003_in_film'

    uclient = ureq(url)
    urlre=uclient.read()
    uclient.close()
    
    ps=soup(urlre,"html.parser")

    mcontainer=ps.find('div',{'class':'mw-parser-output'})
    containers=mcontainer.findAll('ul')
    con=[]
    for i in range(39,63):
        con.append(containers[i])
    contain=con[0]
    count1=0

    for contain in con:
        x=contain.findAll('li')
        count1=count1+1
        count2=0
        y=x[0]
        for y in x:
            if (count2==3 and count1==6) or (count1==8 and count2==10):
                list2003.append(y.i.text)
            else:   
                list2003.append(y.i.a.text)
            count2=count2+1

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
year2000();
year2001();
year2002();
year2003();

print(list2000)
print(list2001)
print(list2002)
print(list2003)

print(len(list2000))
print(len(list2001))
print(len(list2002))
print(len(list2003))

top100();
top200();
top300();
top400()
top500();

with open('e_list.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(list500)


print(list100);
print(list300);
print(list500);

print(len(list100));
print(len(list300));
print(len(list500));