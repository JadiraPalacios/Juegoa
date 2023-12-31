import pygame
import random

WHITE=(255,255,255)
BLACK=(0,0,0)

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("meteoros.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("awa.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()

pygame.init()

screen=pygame.display.set_mode([900,800])
clock=pygame.time.Clock()
done=False
score=0

meteor_list=pygame.sprite.Group()
all_sprite_list=pygame.sprite.Group()

for i in range(20):
    meteor=Meteor()
    meteor.rect.x=random.randrange(900)
    meteor.rect.y=random.randrange(800)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player=Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    mouse_pos=pygame.mouse.get_pos()
    player.rect.x=mouse_pos[0]
    player.rect.y=mouse_pos[1]

    meteor_hit_list=pygame.sprite.spritecollide(player,meteor_list,True)

    for meteor in meteor_hit_list:
        
        score +=10
        print(score)
    screen.fill(BLACK)
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
