# 导入系统文件库
import pygame
import random
from pygame.locals import *
from random import randint

# 定义一些窗体参数及加载字体文件
SCREEN_WIDTH = 900  # 窗体宽度
SCREEN_HEIGHT = 600  # 窗体宽度
LOW_SPEED = 4  # 字体移动最低速度
HIGH_SPEED = 10  # 字体移动最快速度
FONT_COLOR = (00, 150, 00)  # 字体颜色
FONT_SIZE = 5  # 字体尺寸
FONT_NOM = 20  # 显示字体数量  从0开始
FONT_NAME = "calibrii.ttf"  # 注意字体的文件名必须与真实文件完全相同（注意ttf的大小写），且文件名不能是中文
FREQUENCE = 10  # 时间频度
times = 0  # 初始化时间


# 定义随机参数
def randomspeed():
    return randint(LOW_SPEED, HIGH_SPEED)


def randomposition():
    return randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)


def randomoname():
    return randint(0, 100000)


def randomvalue():
    return randint(0, 100)  # this is your own display number range


# class of sprite
class Word(pygame.sprite.Sprite):
    def __init__(self, bornposition):
        pygame.sprite.Sprite.__init__(self)
        self.value = randomvalue()
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.image = self.font.render(str(self.value), True, FONT_COLOR)
        self.speed = randomspeed()
        self.rect = self.image.get_rect()
        self.rect.topleft = bornposition

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# init the available modules
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ViatorSun CodeRain")
clock = pygame.time.Clock()
group = pygame.sprite.Group()
group_count = int(SCREEN_WIDTH / FONT_NOM)

# mainloop
while True:
    time = clock.tick(FREQUENCE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    for i in range(0, group_count):
        group.add(Word((i * FONT_NOM, -FONT_NOM)))

    group.update()
    group.draw(screen)
    pygame.display.update()

