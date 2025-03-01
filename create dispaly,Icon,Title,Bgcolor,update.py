import pygame
pygame.init
screen = pygame.display.set_mode((800,600))
running = True
cap = pygame.display.set_caption("Dino power")
icon = pygame.image.load("dinosaur.png")
pygame.display.set_icon(icon)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,255,0))
    pygame.display.update()