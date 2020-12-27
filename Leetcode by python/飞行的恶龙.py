import pygame, sys
from pygame.locals import *


class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0


def _getx(self):return self.rect.x
def _setx(self, value):self.rect.x = value
def _gety(self):return self.rect.y
def _sety(self, value):self.rect.y = value


def _getpos(self):return self.rect.topleft
def _setpos(self, pos):self.rect.topleft = pos
position = property(_getpos, _setpos)


def load(self, filename, width, height, columns):
    self.master_image = pygame.image.load(filename).convert_alpha()
    self.frame_width = width
    self.frame_height = height
    self.rect = Rect(0, 0, width, height)
    self.columns = columns
    rect = self.master_image.get_rect()
    self.last_frame = (rect.width // width) * (rect.height // height) - 1


def print_text(font, x, y , text, color = (255, 255, 255)):
    img_text = font.render(text, True, color)
    screen.blit(img_text, (x, y))


pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.caption("飞行的恶龙")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

# create a dragon sprite

