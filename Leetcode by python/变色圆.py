"""

画圆的另一种方式，以大圆的边的坐标为圆心画出的众多小圆，来构成成大圆的边

"""

import pygame, sys, random, math
from pygame.locals import *
pygame.init()


screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("变色圆")
screen.fill((0, 111, 222))

angle = 360
color = 0, 0, 0
radius = 66
pos_x = 200
pos_y = 300


while True:
    for event in pygame.event.get():
        # !!!注意要使用大写QUIT！！！
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    angle += 1
    if angle >= 360:
        angle = 0
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    pos_x = math.cos(math.radians(angle)) * radius + 200
    pos_y = math.sin(math.radians(angle)) * radius + 250
    pos = (int(pos_x), int(pos_y))
    pygame.draw.circle(screen, color, pos, 10, 0)
    pygame.display.update()
