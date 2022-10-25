import pygame
import math
from data.player import Player
from data.particle import Particle

gravity = (math.pi, 0.0003)

run = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame")
pygame.time.Clock().tick(60)
player = Player(100, 100)
player2 = Player(700, 100)
particle = Particle(300, 100, 10, screen)
player.mapControls(pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_LCTRL)
player2.mapControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL, pygame.K_RSHIFT, pygame.K_n)
players = [player, player2]
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    for player in players:
        player.move(particle)
        player.draw(screen)
    particle.move(gravity)
    particle.bounce(players)
    particle.display(screen)
    pygame.display.update()
    print(particle.speed)
