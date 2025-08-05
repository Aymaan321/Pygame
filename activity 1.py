# write a python program to create an empty pygame window
import pygame

# initialize required modules
pygame.init()

# setup window geometry
screen = pygame.display.set_mode((600, 500))

# create a loop to run till the game is quit by the user
a = False
while not a:
    # clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # make the changes visible
    pygame.display.flip()
