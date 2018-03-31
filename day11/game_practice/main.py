import sys
import pygame
from person import Person

def run_game():

    pygame.init()
    screen = pygame.display.set_mode((1024,640))
    pygame.display.set_caption("小猪佩奇")
    person=Person(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            # 更新屏幕上的图像，并切换到新屏幕
            screen.fill((70,160,210))
            person.blitme()
            pygame.display.flip()
run_game()