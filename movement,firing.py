import pygame
from random import randint
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)
running = True
cap = pygame.display.set_caption("Dino power")
icon = pygame.image.load("dinosaur.png")
pygame.display.set_icon(icon)
spaceship = pygame.image.load("ship.png")
shipx = 350
shipy = 490
ship_move_DU= 0
ship_move_RL= 0

enemy = []
enemyx = []
enemyy = []
enemy_move_x =[] 
enemy_move_y =[]
number_of_enemies =6
for i in range(number_of_enemies):
    enemy.append(pygame.image.load("aircraft.png"))
    enemyx.append(randint(0,736))
    enemyy.append(randint(0,200))
    enemy_move_x.append(4)
    enemy_move_y.append(40)
space = pygame.image.load("space.png")
guns = pygame.image.load("bullet (1).png")
gunsx = 0
gunsy = 0
guns_move_x = 0
guns_move_y = 12
bullet_state = "ready"
def player(x,y):
    screen.blit(spaceship, (x,y))
def aircraft(x,y,i):
    screen.blit(enemy[i], (x,y))
def bg():
    screen.blit(space,(0,0))
def bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(guns,(x+16,y+10))
def iscollision(enemyy,enemyx,gunsx,gunsy):
    distance = math.sqrt((math.pow(enemyx-gunsx,2))+(math.pow(enemyy-gunsy,2)))
    if distance < 27:
        return True
    else:
        return False
    
score_value=0
font = pygame.font.Font('varsity_regular.ttf',32)
texty=10
textx=10
over_font=pygame.font.Font('varsity_regular.ttf',64)
def show_score(x,y):
    score = font.render("Score : "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over = over_font.render(" GAME OVER ",True,(255,255,255))
    screen.blit(over,(200,250))
while running:
    screen.fill((0,0,0))
    bg()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship_move_RL += 5
            if event.key == pygame.K_LEFT:
                ship_move_RL -= 5
            if event.key == pygame.K_DOWN:
                ship_move_DU += 5
            if event.key == pygame.K_UP:
                ship_move_DU -= 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    gunsx = shipx
                    bullet(gunsx, gunsy)
                    shot = pygame.mixer.Sound("shoot.mp3")
                    shot.play()

                
        if event.type == pygame.KEYUP:
            ship_move_DU=0
            ship_move_RL=0
        if event.type == pygame.QUIT:
            running = False
    shipx+=ship_move_RL    
    shipy+=ship_move_DU 
    if shipx <=0:
        shipx = 0
    if shipx >=736:
        shipx = 736
    if shipy <=0:
        shipy = 0
    if shipy >=530:
        shipy = 530
        
    for i in range(number_of_enemies):
        if enemyy[i]>490:
            for j in range(number_of_enemies):
                enemyy[j]=2000
            game_over_text()
            break
        enemyx[i] += enemy_move_x[i]   
        if enemyx[i] <=0:
            enemy_move_x[i] = 4
            enemyy[i] += enemy_move_y[i]
        elif enemyx[i] >=736:
            enemy_move_x[i] = -4
            enemyy[i] += enemy_move_y[i]
        collision = iscollision(enemyy[i],enemyx[i],gunsx,gunsy)
        if collision:
            explosion = pygame.mixer.Sound("explosive.mp3")
            explosion.play()
            gunsy = shipy
            gunsx = shipx
            bullet_state = "ready"
            score_value+=1
            enemyx[i] = randint(0,736)
            enemyy[i] = randint(0,200)    
        aircraft(enemyx[i],enemyy[i],i) 
        
    if gunsy<=0:
        gunsy = shipy
        gunsx = shipx
        bullet_state="ready"

    if bullet_state is "fire":
        bullet(gunsx,gunsy)
        gunsy -= guns_move_y
    player(shipx,shipy)
    show_score(textx,texty)
    pygame.display.update()
