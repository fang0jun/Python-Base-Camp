"""

1,画出圆环和数字
2，使用多个小圆同时进行画园运动，组成长条作为针

"""
import pygame, sys, math, random
from datetime import datetime, date, time
from pygame.locals import *


# 基操
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("动态时钟")
screen.fill((111, 222, 222))

# 时间
today = datetime.today()
T = datetime.today().time()

# 某些参数
white = 255, 255, 255
orange = 220, 180, 0
yellow = 255, 255, 0
pink = 255, 100, 100
font = pygame.font.Font(None, 36)
pos_x = 300
pos_y = 250
radius = 250
angle = 360

# 绘制数字
def print_text(font, x, y, text, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def wrap_angle(angle):
    return angle % 360

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)
    pygame.draw.circle(screen, white, (pos_x, pos_y), 6, 0)

    for n in range(1, 13):
        x = int(math.cos(math.radians(30 * n - 90)) * (radius-20) - 10)
        y = int(math.sin(math.radians(30 * n - 90)) * (radius-20) - 10)
        print_text(font, pos_x + x, pos_y + y, str(n))

    # 绘制时针
    hours = datetime.today().hour % 12
    hours_x = int(math.cos(math.radians(30 * hours - 90)) * (radius - 80) - 10)
    hours_y = int(math.sin(math.radians(30 * hours - 90)) * (radius - 80) - 10)
    pygame.draw.line(screen, pink, (pos_x, pos_y), (pos_x + hours_x, pos_y + hours_y), 25)

    # 绘制分针
    min = datetime.today().minute
    min_angle = wrap_angle(min * 6 - 90)
    min_x = int(math.cos(math.radians(min_angle)) * (radius - 45))
    min_y = int(math.sin(math.radians(min_angle)) * (radius - 45))
    pygame.draw.line(screen, orange, (pos_x, pos_y), (pos_x + min_x, pos_y + min_y), 15)

    # 绘制秒针
    seconds = datetime.today().second
    angle = wrap_angle(seconds * 6 - 90)
    second_x = int(math.cos(math.radians(angle)) * (radius - 10))
    second_y = int(math.sin(math.radians(angle)) * (radius - 10))
    pygame.draw.line(screen, orange, (pos_x, pos_y), (pos_x + second_x, pos_y + second_y), 9)


    pygame.display.update()
