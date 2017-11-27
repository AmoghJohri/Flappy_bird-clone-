import flappy
import pygame
import random
import pygame.mixer
import sys
from random import randint
from pygame.locals import *
import time

#Colors
yellow = (0,255,255)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
maroon = (131,3,0)
gold = (255,215,0)
purple = (102,0,102)

FPS = 30

pygame.init()

#game-icon
icon = pygame.image.load('flappy.jpeg')
pygame.display.set_icon(icon)

#Sound_clips
hit_sound = pygame.mixer.Sound('sound/hit.wav')
die_sound = pygame.mixer.Sound('sound/die.wav')
wing_sound = pygame.mixer.Sound('sound/wing.wav')
point_sound = pygame.mixer.Sound('sound/point.wav')
theme = pygame.mixer.Sound('sound/theme.wav')


pygame.init()


#Display
size = 500,700
screen = pygame.display.set_mode(size) 
gameDisplay = pygame.display.set_mode((500,700))
pygame.display.set_caption("Flappy Bird")


#Highscore_file
global Highscore_all
with open('highscore.txt','r') as f:
  Highscore_all = int(f.read(100))
global HighScore
HighScore = 0

global i
i=0


theme.play()	#Theme_song


#Main game loop begins here.

def gameloop():

  #Randomizing bird images.
  n = randint(1,3)
  if(n==1):
    ballIMG = pygame.image.load('bird_images/bluebird-midflap.png')
    fallIMG = pygame.image.load('bird_images/bluebird-fall.png')
  elif(n==2):
    ballIMG = pygame.image.load('bird_images/redbird-midflap.png')
    fallIMG = pygame.image.load('bird_images/redbird-fall.png')
  else:
    ballIMG = pygame.image.load('bird_images/yellowbird-midflap.png')
    fallIMG = pygame.image.load('bird_images/yellowbird-fall.png')
  
  #Randomizing background images.
  bg = randint(1,3)
  if(bg == 1):
    background = pygame.image.load('bg_images/static_background.png')
  elif(bg == 2):
    background = pygame.image.load('bg_images/Day.png')
  else:
    background = pygame.image.load('bg_images/Night.png')
  
  #Randomizing pipe images.
  ob = randint(1,2)
  if(ob == 1):
      loc1 = pygame.image.load('pipe_images/upperpipe-red.png')
      loc2 = pygame.image.load('pipe_images/lowerpipe-red.png')
  else:
      loc1 = pygame.image.load('pipe_images/upperpipe-green.png')
      loc2 = pygame.image.load('pipe_images/lowerpipe-green.png')


  clock = pygame.time.Clock()
  global counter	#Counter for choosing mid-flap or fall-bird image.
  counter = 0
  global HighScore
  

  #Bird definition.
  def bird(x,y):
    if counter == 0:
      gameDisplay.blit(ballIMG,(x,y))
    else:
      gameDisplay.blit(fallIMG,(x,y))

  
  #Gameover definition.
  def gameover():
    global Highscore_all
    global HighScore
    global counter
    Score(score)	#Displays score.
    counter += 1
    if counter == 1:
      pygame.mixer.pause()
      hit_sound.play()
      die_sound.play()
    play_again()
    font = pygame.font.SysFont(None,30)	
    font1 = pygame.font.SysFont(None,75)
    font2 = pygame.font.SysFont(None,40)
    text1 = font1.render("Game Over",True,red)

    #Highscore definition.
    if HighScore <= score:
      HighScore = score
    if Highscore_all <= HighScore:
      Highscore_all = HighScore
      with open('highscore.txt','w') as f:
        f.write(str(HighScore))

    text2 = font2.render("Score : " + str(score),True,maroon)
    text3 = font2.render("Highscore:" + " " + str(Highscore_all),True,gold)
    text4 = font.render("Press r to reset HighScore",True,white)
    screen.blit(text1, [120,220])
    screen.blit(text2, [205,290])
    screen.blit(text3, [180,320])
    screen.blit(text4, [130,420])
    

  #Pipe/Obstacle definition.
  def obstacle(xloc,yloc,xsize,ysize):    
    upper = pygame.transform.scale(loc1, (xsize,ysize))		#Scales pipe length to requirement.
    lower = pygame.transform.scale(loc2,(xsize, ysize + 700))
    screen.blit(upper, (xloc,yloc))
    screen.blit(lower, (xloc, yloc + ysize + space))

 
  #Score definition.
  def Score(score):
    global i
    font = pygame.font.SysFont(None,50)  
    font2 = pygame.font.SysFont(None,85)
    font3 = pygame.font.SysFont(None,35)  
    text = font.render("Score: " + str(score),True,gold)
    if i >= 1:
        screen.blit(text,[0,0])
    if i < 1:
	pygame.draw.rect(screen,white,[0, 90, 500, 250])
        pygame.draw.rect(screen,black,[10, 100, 480, 230])

        text2 = font2.render("FLAPPY BIRD !!!",True,green)
        text3 = font.render("Press p to play",True,yellow)
        text4 = font.render("Press ESCAPE to quit",True,yellow)
        text5 = font3.render("Press 'up arrow key' to move the bird",True,gold)
        screen.blit(text2,[25,100])
        screen.blit(text3,[120,200])
        screen.blit(text4,[60,240])
        screen.blit(text5,[40,300])


  #Play again definition.
  def play_again():
    font = pygame.font.SysFont(None,30)
    pygame.draw.rect(screen,white,[110, 210, 300, 250])
    pygame.draw.rect(screen,black,[120, 220, 280, 230])
    text1 = font.render("Press Enter to play again",True,yellow)
    text2 = font.render("Press Escape to quit",True,white)
    screen.blit(text1, [140,370])
    screen.blit(text2, [160,395])
    if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
             global score
             score = 0
             global HighScore
             HighScore = 0
             global Highscore_all
             Highscore_all = 0

    #Enter key restarts the game.
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
		pygame.mixer.unpause()
                gameloop()    


  #Game variable values.
  x = 200
  y = 350
  x_speed = 0
  y_speed = 6
  ground = 700
  xloc = 500
  yloc = 0
  xsize = 70
  ysize = randint(0,350)
  space  = 150
  obspeed = 3
  global score
  score = 0


  #Keys assigned for bird movement.
  done = False	      	
  while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -8    
		wing_sound.play()
		img = 1  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 6
		img = 2

    
    #Function calls.          
    screen.fill(white)
    screen.blit(background,(0,0))
    obstacle(xloc,yloc,xsize,ysize)
    bird(x,y)         
    Score(score)

    #Initial values of game variables.
    y += y_speed
    xloc -= obspeed


    #Crash tests.
    if (y>ground):	#For ground.
        gameover()
        y_speed = 10
        obspeed = 0
    if x+34> xloc and y-6 < ysize and x-25 < xsize+xloc:	#For lower pipe.
        gameover()
        y_speed = 10
        obspeed = 0
    if x+34> xloc and y+24 > ysize+space and x-25 < xsize+xloc:		#For upper pipe.
        gameover()
        y_speed = 10
        obspeed = 0

    #Pipe movement.    
    if xloc < -60:
        xloc = 500
        ysize = randint(0,350)		#Randomizing length of pipes.

    
    #Score increment.
    if x > xloc and x < xloc + 5:
        score = score + 1
        point_sound.play()
        

    pygame.display.flip()
    clock.tick(60)
    
    global i
    while i < 1:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                i = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()


gameloop()
pygame.quit()
quit()


