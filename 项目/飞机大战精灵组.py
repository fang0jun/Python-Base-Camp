import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
BULLET_FIRE = 1
#创建定时器
CREATE_ENEMY_EVENT = pygame.USEREVENT

#游戏精灵父类
class Basic(pygame.sprite.Sprite):#包.块.类（精灵类）
    """精灵组"""

    def __init__(self,image,speed=1):
    #因为是继承自pygame的精灵子类(非object)故需要主动调用父类的初始化
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

#子类-屏幕
class Background(Basic):
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

#子类-敌机
class Enemy(Basic):
    def __init__(self):
        super().__init__("./image/enemy_2.png")
        self.speed = random.randint(3,5)
        self.rect.bottom = 0             #bottom = y - height(图像)
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

    def __del__(self):
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
        #设置与子弹精灵碰撞后的动画

class Hero(Basic):
    #自定义基本属性

    def __init__(self):
        super().__init__("./image/hero.png" , 0)
        self.rect.x = 180
        self.rect.y = 400
        self.bullet_hero_group = pygame.sprite.Group()
    def fire(self):
        bullet = Bullet_hero()
        bullet.rect.bottom = self.rect.bottom - 20
        bullet.rect.centerx = self.rect.centerx
        self.bullet_hero_group.add(bullet)


    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= SCREEN_RECT.left:
            self.rect.x = SCREEN_RECT.left
        elif self.rect.x >= SCREEN_RECT.right:
            self.rect.x = SCREEN_RECT.right

class Bullet_hero(Basic):
    def __init__(self):
        super().__init__("./image/bullet.png",-6)
    def update(self):
        super().update()
        if self.rect.y <= 0:
            self.kill()















