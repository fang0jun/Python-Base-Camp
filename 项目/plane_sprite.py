#创造游戏精灵子类

import random
import pygame
#定义屏幕大小 常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新的帧率
FRAME_PER_SEC= 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT  #专门为用户提供了一个常量（固定常量）
#创建子弹发射的定时器常量
FIRE_BULLET = pygame.USEREVENT +1

#计分



class Game(pygame.sprite.Sprite): #包.块.类(Sprite)
    """飞机大战游戏精灵"""

    #封装3个属性，既然要定义 对象的3个属性就要先实现初始化
    def __init__(self,image_name,speed=1):

        # 因为是继承自pygame的精灵子类(非object)故需要主动调用父类的初始化
        super().__init__()#可以调用父类的方法的对象
        #定义对象的属性
        self.image = pygame.image.load(image_name) #---因为不是路径故不用双括号
        self.rect =  self.image.get_rect()    #默认（0，0，原图长，原图宽）
        self.speed = speed
    def update(self):  #---重写了 父类的update方法，即所有精灵都调用的一个方法
        #在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(Game):  #继承父类,创建一个子类，以实现父类做不到的功能
    """游戏背景精灵"""
    def update(self):
        # 调用父类有用的方法    动态方法的调用使用super（）
        super().update()
        #判断背景是否移出屏幕，如果移出屏幕，则将图片设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
#设置背景滚动---方法二
# class Background(Game):
#     def __init__(self,is_alt =False):
#         #1，调用父类方法实现精灵的创建   有用参数（image/rect/speed）
#         super().__init__("./image/background.png")  #---super().调用一下初始化方法  并设置图片
#         #2，判断是否是交替图像，如果是，需要设置初始位置
#         if is_alt:
#             self.rect.y = -self.rect.height   #错误---self.rect.y = -self.rect.y


class Enemy(Game):
    """敌机精灵"""
    # 设置敌机精灵       1，初始化方法   2，重写update()方法
    def __init__(self):

        #1，初始化方法 --- 调用父类方法，顺便指定好敌机图片
        super().__init__("./image/enemy_1.png")

        # 并随机指定敌机水平位置和敌机速度
        self.speed = random.randint(3,5)
        self.rect.bottom = 0      #---bottom = y - height(图像)
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        #2,调用父类方法！保持垂直方向飞行
        super().update()

    # def __del__(self):
    #     count += 1

        # 判断敌机是否飞出屏幕，从精灵组中删除敌机（保证内存）
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    # def __del__(self): #检测是否被销毁
    #     print("敌机挂了")

class Hero(Game):
    """英雄精灵"""
    def __init__(self):
        super().__init__("./image/hero.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 100
        self.bullet_group = pygame.sprite.Group()    #!!!将子弹精灵组在Hero中初始化 在main主程序中调用
    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
    def fire(self):
        for i in (0,1,2):
            bullet = Hero_bullet()
            bullet.rect.bottom = self.rect.y -i*20
            bullet.rect.centerx = self.rect.centerx
            self.bullet_group.add(bullet)

class Hero_bullet(Game):
    def __init__(self):
        super().__init__("./image/bullet.png",-5)

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()
    # def __del__(self):
    #     print("0")