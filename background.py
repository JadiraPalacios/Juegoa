import pygame


screen=pygame.display.set_mode([806,715])
clock=pygame.time.Clock()
pygame.mouse.set_visible(0)

done=False

background=pygame.image.load("awaer.png").convert()
player=pygame.image.load("awa.png").convert()
player.set_colorkey([0,0,0])
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    mouse_pos=pygame.mouse.get_pos()
    x=mouse_pos[0]
    y=mouse_pos[1]


    screen.blit(background,[0,0])
    screen.blit(player,[x,y])
    pygame.display.flip()
    clock.tick(60)