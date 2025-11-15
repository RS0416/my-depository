import pygame
pygame.init()
screen= pygame.display.set_mode((500,500))
done= False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen, (0,255,0), (200,200),50)
    pygame.draw.circle(screen, (255,0,255), (200,300),60,3)
    pygame.display.flip()