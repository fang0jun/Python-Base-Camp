import pygame

from plane_sprite import *


# font = pygame.font.Font(None,70)

    #主程序第一步：c封装主程序类
class Game(object):  #主游戏类继承object机位
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
        #1，创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size) #--开发时最好用常量来代替固定的值  size使矩形获得元组
        # my_score = font.render(str(count), False, (255, 255, 255))
        # self.screen.blit(my_score, (10, 30))
        #2，创建游戏时钟
        self.clock = pygame.time.Clock()
        #3，调用私有方法，创建精灵与精灵组
        self.__create_sprite()
        #4，设置定时器事件（初始化中设置）-创造敌机-1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT,500)
        pygame.time.set_timer(FIRE_BULLET,500)


    def __create_sprite(self):   #调用私有方法
        #创建精灵
        bg1 = Background("./image/background.png",6)
        bg2 = Background("./image/background.png",6)
        bg2.rect.y = -bg2.rect.height
        #将英雄单独定义成一个游戏系统的属性 才能在其他方法中直接使用英雄这个对象
        self.hero = Hero()

        #创建精灵组
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)


        #创建精灵和精灵组
        # bg1 = Background()
        # bg2 = Background(True)
        # self.bg_group = pygame.sprite.Group(bg1,bg2)



    def start_game(self):
        print("游戏开始")
        while True:
            #1，设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #2，事件监听
            self.__event_handler()
            #3，碰撞检测
            self.__check_collide()
            #4，更新/绘制精灵组
            self.__update_sprites()
            #5，更新显示
            pygame.display.update()
            pass
    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退游
            if event.type == pygame.QUIT:
                # pygame.quit()
                # exit()
                Game.__gameover()  # 用类名的方式调用静态方法！
            elif event.type == CREATE_ENEMY_EVENT:   #监听定时器事件是否发生（定时响起）
                #创建敌机精灵
                enemy =Enemy()
                #将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == FIRE_BULLET:
                self.hero.fire()
            #键盘监听法
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右")
        #使用键盘提供的方法(键盘模块法)获取键盘按键 --- 返回一个按键元组
        key_pressed = pygame.key.get_pressed()
        #判断元组中对应的按键索引值 1
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -4
        else:
            self.hero.speed = 0



    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        # list = pygame.sprite.spritecollide(self.enemy, self.hero.bullet_group, False)

        enemys_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,False)   #返回 所有敌机精灵列表
        if len(enemys_list) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self): #--括号中有（self）是动态的方法
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __gameover():   #--gameover未使用对象属性，位属性，故所以是静态方法
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':  #为了当前主程序可以被当作模块导入
    #主程序第二步：创建游戏对象
    game = Game()
    #主程序第三步：启动游戏
    game.start_game()