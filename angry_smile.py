import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
bg_color = (135, 206, 235)
screen.fill(bg_color)

circle(screen, (0, 0, 255), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 1)
circle(screen, (255, 255, 255), (155, 150), 20)
circle(screen, (0, 0, 0), (155, 150), 20, 1)
circle(screen, (0, 0, 0), (155, 150), 7)
circle(screen, (0, 0, 0), (155, 150), 7, 1)
circle(screen, (255, 255, 255), (245, 150), 20)
circle(screen, (0, 0, 0), (245, 150), 20, 1)
circle(screen, (0, 0, 0), (245, 150), 7)
circle(screen, (0, 0, 0), (245, 150), 7, 1)
pygame.draw.line(screen, (0,0,0),
                 [150, 100],
                 [180, 115], 7)

pygame.draw.line(screen, (0,0,0),
                 [250, 110],
                 [220, 120], 7)
polygon(screen, (139, 0, 139), [(150,180), (150,240),
                               (250,210), (250,200)])





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
