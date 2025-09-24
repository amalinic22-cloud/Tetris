import pygame, sys
from grid import Grid
from blocks import *


pygame.init()
purple = (240, 100, 227)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris!")

clock = pygame.time.Clock()

game_grid = Grid()
fall_time = 0
fall_speed = 60

block = LBlock()

while True:
    fall_time += clock.get_rawtime()
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                block.move_down()
            elif event.key == pygame.K_LEFT:
                block.move_left()
            elif event.key == pygame.K_RIGHT:
                block.move_right()


    if fall_time > fall_speed:
        block.move_down()
        fall_time = 0
    

    screen.fill(purple)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)

