import sys
import pygame

class Person():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('images/peiqi.bmp')
        self.person_rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        # 将佩奇放在中央
        self.person_rect.centerx = 512
        height=(self.person_rect.top-self.person_rect.bottom)/2
        self.person_rect.bottom = 320-height

    def blitme(self):
        """在指定位置绘制佩奇"""
        self.screen.blit(self.image, self.person_rect)
