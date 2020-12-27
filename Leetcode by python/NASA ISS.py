import pygame, sys, math
from pygame.locals import *
pygame.init()


screen = pygame.display.set_mode((800, 600))
planet = pygame.image.load("lanqiu.jpg").convert_alpha()
width_1, height_1 = screen.get_size()
width_2, height_2 = screen.get_size()
ship = pygame.image.load("ship.png").convert_alpha()
ship = pygame.transform.smoothscale(ship, (width_2//5, height_2//5))


angle = 0.0
old_x = 0
old_y = 0


screen.fill((0, 0, 0))
pygame.display.set_caption("环球飞行")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        screen = pygame.display.set_mode((800, 600))
        # draw background
        screen.blit(planet, ((width_1 - 301)/2, (height_1 - 292)/2))

        # move the ship
        angle = (angle + 0.1) % 360
        radius = 230
        pos_x = math.cos(math.radians(angle)) * radius
        pos_y = math.sin(math.radians(angle)) * radius



        # rotate a degree
        delta_x = (pos_x - old_x)
        delta_y = (pos_x - old_y)

        rangled = math.degrees(math.atan2(delta_x, delta_y)) % 360

        scratch_ship = pygame.transform.rotate(ship, rangled)
        screen.blit(scratch_ship, (pos_x + 720 - width_1 // 2, pos_y + 550 - height_1 // 2))
        old_x = pos_x
        old_y = pos_y



        pygame.display.update()