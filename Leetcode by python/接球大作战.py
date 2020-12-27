import random
import pygame

pygame.init()

#创建一个游戏屏幕(包括游戏介绍，游戏图标，窗口颜色)  ？idea？第二版改为背景图片
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("                                                                     448----接球大战")

#创建一个游戏时钟
clock = pygame.time.Clock()

#自定义棍球等等物品的初始化数据
window_color = (150,90,90)
ball_color = (200,200,0)
rect_color = (0,200,200)
number = 1
count = 0
score = 0
#字体对象font（字体，字号）
font = pygame.font.Font(None,70)
ball_x = random.randint(20,480)
ball_y = random.randint(20,180)

speed_x = 5
speed_y = 5


while True:
    #设置窗口颜色
    screen.fill(window_color)

    #设置游戏帧率
    clock.tick(60)

    #监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mouse_x,mouse_y = pygame.mouse.get_pos()

    # 碰撞检测


    # 绘制物品 圆形4要素---投影地点/投影颜色/投影位置/半径
    #        矩形3要素---投影地点/投影颜色/Rect的一套(xy长9宽)
    pygame.draw.circle(screen,ball_color,(ball_x,ball_y),20)
    pygame.draw.rect(screen,rect_color,(mouse_x -50,490,100,10))
    # 绘制分数 render(字的内容，布尔值，字体颜色RGB值)
    my_score = font.render(str(score), False, (255,255,255))
    screen.blit(my_score, (500,30))

    # 球的位置变化
    ball_x += speed_x
    ball_y += speed_y
    if ball_x <= 20 or ball_x >= 580:
        # ball_x += -speed_x  效果不同！
        speed_x = -speed_x
    if ball_y <= 20:
        speed_y = -speed_y
    elif mouse_x - 30 - (10*3**0.5) <= ball_x <= mouse_x + 110 + (10*3**0.5)  and ball_y >= 470:
        speed_y = -speed_y
        score += number
        count += 1
        if count == 5:
            count = 0
            number += number
            if speed_x > 0:
                speed_x += 5
            else:
                speed_x -= 10
            speed_y -= 5

    elif ball_y >= 480 and (mouse_x - 35 -(10*3**0.5)  >= ball_x or ball_x >= mouse_x + 110 + (10*3**0.5) ):
        break



    #更新屏幕
    pygame.display.update()

    pass