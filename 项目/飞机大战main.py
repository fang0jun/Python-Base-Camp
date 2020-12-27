import pygame

from 飞机大战精灵组自编版 import *

class Game():
    def __init__(self):

        #创建游戏屏幕
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        #创建游戏时钟
        self.clock = pygame.time.Clock()

        #调用私有方法，创建精灵和精灵组
        self.__create_sprite()

        #创建定时器（以用作创造随机事件）
        pygame.time.set_timer(CREATE_ENEMY_EVENT,500)
        pygame.time.set_timer(BULLET_FIRE,500)

    def __create_sprite(self):
        background1 = Background("./image/background.png",6)
        background2 = Background("./image/background.png",6)
        background2.rect.y = -background2.rect.height

        #将hero对象 单独 定义成一个游戏系统的属性，以便之后子弹类精灵调用在系统中的hero对象中
        self.hero = Hero()


        #精灵组是一种属性
        self.background_group = pygame.sprite.Group(background1,background2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)





#=======================================================================================================================
#=======================================================================================================================




    #私有方法只有在对象方法中自身调用后才能被使用---共有方法里的私有是 存着为了自己调用
    def start_game(self):
        while True:
        #设置刷新频率
            self.clock.tick(FRAME_PER_SEC) #最好用变量储存

            #监听事件
            self.__event_handler()

            #检测碰撞
            self.__check_collide()

            #调用精灵和精灵组
            self.__update_sprite()

            #更新屏幕
            pygame.display.update()
            pass

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


    def __event_handler(self):
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 self.__game_over()
             #创建多个随机精灵是，要在循环里创建精灵对象（提前得设置一个定时器）
             elif event.type == CREATE_ENEMY_EVENT:
                 enemy = Enemy()
                 self.enemy_group.add(enemy)
             elif event.type == BULLET_FIRE:
                 self.hero.fire()



    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero_group,self.hero.bullet_hero_group,True,True)
        collide_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,False)
        if len(collide_list) > 0:
            self.hero.kill()
            self.__game_over()


    def __update_sprite(self):
        self.background_group.update()
        self.background_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_hero_group.update()
        self.hero.bullet_hero_group.draw(self.screen)



#=======================================================================================================================
#=======================================================================================================================



        #碰撞检测
if __name__ == '__main__':
    game = Game()
    game.start_game()