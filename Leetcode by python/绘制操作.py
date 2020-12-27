import pygame, sys, math
from pygame.locals import *
pygame.init()


# 创建一个游戏窗口  ---必须创建一个屏幕对象
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing a circle")

# 绘制文本  ---创建一个字体对象
# 注意：pygame文本并不是快速绘制在屏幕上，而是渲染到一个平面上以后，再贴在屏幕上
# 故具体步骤为：1，创建一个文本对象（有字型字号） 2，渲染到一个平面对象上（文本/抗/RGB） 3，screen.blit(平面/（位置）)
my_font = pygame.font.Font(None, 60)
white = 255, 255, 255
blue = 0, 0, 255
text_image = my_font.render("Hello pygame", True, white)

circle_color = 255, 0, 0
circle_position = (150, 200)
circle_width = 10
circle_radius = 50


while True:
    # pygame.event.get()可看作是一个用户时间元组
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(text_image, (150, 100))
    # pygame.display.update  一次程序里不能出现俩个刷新屏幕（会闪屏）

    # 绘制参数规律： 屏色位尺边
    # 绘制圆形的参数（屏幕/颜色/位置/半径/边宽）
    pygame.draw.circle(screen, circle_color, circle_position, circle_radius, circle_width)
    # 绘制矩形的参数（屏幕/颜色/位置与边长/四边间距）
    pygame.draw.rect(screen, white, (300,300,100,100))
    # 绘制线条的参数（屏幕/颜色/起点/终点/粗细）
    pygame.draw.line(screen, (0, 255, 0), (200, 0), (250,300), 10)
    # 绘制弧形的参数（屏幕/颜色/矩形Rect/起点/终点/弧度/粗细）
    pygame.draw.arc(screen, blue, (300,300,100,100),math.radians(10), math.radians(180), 10)
    
    pygame.display.update()

