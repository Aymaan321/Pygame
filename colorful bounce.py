import pygame
import random

pygame.init()

# Custom event ids for color change event
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
# Background Color
LIGHT_GREEN = pygame.Color('lightgreen')
DARK_RED = pygame.Color('darkred')
BLUE = pygame.Color('blue')

# Sprite Color
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
CYAN = pygame.Color('cyan')
BLACK = pygame.Color('black')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call to the parent class(Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    # Method to obtain sprite's position
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        # Check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        # Check for collision with top or bottom boundaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
            # If a boundary was hit, post events to change colors
        if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
                boundary_hit = False
    # Method to change sprite's color
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, CYAN, BLACK]))

def change_background_color():
    global bg_color
    bg_color = random.choice([LIGHT_GREEN, DARK_RED, BLUE])

sp1 = Sprite(BLACK, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")

bg_color = BLUE
screen.fill(bg_color)

clock = pygame.time.Clock()
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    # If the event sprite color change, change the sprite's color
    elif event.type == SPRITE_COLOR_CHANGE_EVENT:
      sp1.change_color()
    # If the event background color change, change the background color
    elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
      change_background_color()

  all_sprites_list.update()
  screen.fill(bg_color)
  all_sprites_list.draw(screen)

  pygame.display.flip()
  clock.tick(240)

pygame.quit()
