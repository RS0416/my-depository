import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colors using pygame.Color

# Background colors

BLUE = pygame.Color('blue')

LIGHTBLUE = pygame.Color('lightblue')

DARKBLUE = pygame.Color('darkblue')

# Sprite colors

YELLOW = pygame.Color('yellow')

MAGENTA = pygame.Color('magenta')

ORANGE = pygame.Color('orange')

WHITE = pygame.Color('white')

screen_width, screen_height = 500, 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('color changing sprite')

class SPRITE(pygame.sprite.Sprite):
    def __init__ (self, color, height, width):
        super().__init__()
        self.img=pygame.Surface([width, height])
        self.img.fill(color)
        self.rect=self.img.get_rect()
        self.velocity=[random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundaryhit = False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]= -self.velocity[0]
            boundaryhit= True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[0]= -self.velocity[0]
            boundaryhit= True
        if boundaryhit== True:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def changecolor(self):
        self.img.fill(random.choice([YELLOW, BLUE, ORANGE, WHITE]))

def change_background_color():
   global bg_color
   bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

all_sprite_list=pygame.sprite.Group()
sp1=SPRITE(BLUE,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,380)

screen = pygame.display.set_mode((500, 400))

# Set the window title

pygame.display.set_caption("Colorful Bounce")

# Set the initial background color

bg_color = BLUE

# Apply the background color

screen.fill(bg_color)

# Game loop control flag

exit = False

# Create a clock object to control frame rate

clock = pygame.time.Clock()

# Main game loop

while not exit:

# Event handling loop

   for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit = True
        
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()

# If the background color change event is triggered, change the background color

        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:

            change_background_color()
   all_sprite_list.update()
   screen.fill(bg_color)
   all_sprite_list.draw(screen)
   pygame.display.flip()
   clock.tick(240)

pygame.quit()