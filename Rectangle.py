# Draw a rectangle
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
a = False
while not a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = True
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
    