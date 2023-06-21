import pygame

pygame.init()

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()
