import pygame
pygame.init()
screen_width, screen_height= 500, 500
display_surface= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("put a caption:")
background_img= pygame.transform.scale(pygame.image.load("C:\VS_CODES\py_games\bg.jpg").convert(),
(screen_width, screen_height))

def game_loop():
    clock= pygame.time.Clock()
    running= True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        display_surface.blit(background_img, (0,0))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

