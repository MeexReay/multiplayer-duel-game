import pygame
pygame.init()

win = pygame.display.set_mode((600,400))
pygame.display.set_caption("Multiplayer Duel Game")

clock = pygame.time.Clock()
 
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)
pygame.quit()