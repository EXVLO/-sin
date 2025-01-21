from turtle import distance
import pygame
import math
import logging

pygame.init()

w = 600
h = 600

start2 = -6
end2 = 6
dist2 = end2 - start2

scale = 10  

screen = pygame.display.set_mode((w, h))

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def square_function(x):
    return x**2

def sin(x, time):
    return math.sin(x + time)

running = True
clock = pygame.time.Clock()
time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # for i in range(w):
    #     x = i / w * dist1 - 2
    #     y = h - square_function(x) * h / scale

    #     screen.set_at((i, int(y)), (255, 255, 255))

    for i in range(w):
        x = i / w * dist2
        y = h / 2 - sin(x, time) * h / scale

        screen.set_at((i, int(y)), (255, 255, 255))

    pygame.display.flip()

    time += 0.1  
    clock.tick(60)  

pygame.quit()
