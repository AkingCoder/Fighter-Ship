import pygame
pygame.init


def player():
    screen.blit(spaceship, (shipx, shipy))


screen = pygame.display.set_mode((800, 600))
running = True
cap = pygame.display.set_caption("Dino power")
icon = pygame.image.load("dinosaur.png")
pygame.display.set_icon(icon)
spaceship = pygame.image.load("ship.png")
shipx = 350
shipy = 490
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    player()
    pygame.display.update()
