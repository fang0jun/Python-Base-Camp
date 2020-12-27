"""

以事件获取与否 来 获得函数执行与否的标志（True/False）

"""
import pygame, sys, math
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("pie 游戏")

text = pygame.font.Font(None, 50)
img_1 = text.render("1", True, (255, 255, 255))
img_2 = text.render("2", True, (255, 255, 255))
img_3 = text.render("3", True, (255, 255, 255))
img_4 = text.render("4", True, (255, 255, 255))

piece_1 = False
piece_2 = False
piece_3 = False
piece_4 = False


while True:
    for event in pygame.event.get():
        # if event in (QUIT, KEYDOWN):
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece_1 = True
            elif event.key == pygame.K_2:
                piece_2 = True
            elif event.key == pygame.K_3:
                piece_3 = True
            elif event.key == pygame.K_4:
                piece_4 = True

    screen.fill((0, 0, 200))

    # draw the number
    screen.blit(img_1, (160, 50))
    screen.blit(img_2, (60, 50))
    screen.blit(img_3, (60, 150))
    screen.blit(img_4, (160, 150))

    if piece_1:
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (125, 25), 2)
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (225, 125), 2)
        pygame.draw.arc(screen, (255, 255, 255), (25, 25, 200, 200), math.radians(0), math.radians(90),2)
    if piece_2:
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (125, 25), 2)
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (25, 125), 2)
        pygame.draw.arc(screen, (255, 255, 255), (25, 25, 200, 200), math.radians(90), math.radians(180), 2)
    if piece_3:
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (125, 225), 2)
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (25, 125), 2)
        pygame.draw.arc(screen, (255, 255, 255), (25, 25, 200, 200), math.radians(180), math.radians(270), 2)
    if piece_4:
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (125, 225), 2)
        pygame.draw.line(screen, (255, 255, 255), (125, 125), (225, 125), 2)
        pygame.draw.arc(screen, (255, 255, 255), (25, 25, 200, 200), math.radians(270), math.radians(360), 2)
    pygame.display.update()