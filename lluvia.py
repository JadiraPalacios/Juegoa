import pygame, sys
import random
pygame.init()

black = (0,0,0)
celeste = (0,200,255)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_list = []
for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    coor_list.append([x, y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    for coord in coor_list:
        pygame.draw.circle(screen, celeste, coord, 2)
        coord[1] += 1
        if coord[1] > 500:
            coord[1] = 0

    pygame.display.flip()
    clock.tick(30)