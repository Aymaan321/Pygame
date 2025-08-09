import pygame
pygame.init()

screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

green = (0, 175, 0)
# Draw solid circle
pygame.draw.circle(screen, green, (300, 300), 50)

# Draw outlined circle
pygame.draw.circle(screen, green, (100, 100), 50, 3)

pygame.display.update()

a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
    pygame.display.flip()

pygame.quit()
