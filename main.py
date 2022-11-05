import pygame
import math
from data.player import Player
from data.particle import Particle
from data.character import Character
from data.sprite import Sprite

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lethal League")
clock = pygame.time.Clock()
raptor = Sprite(Character.RAPTOR)
latch = Sprite(Character.LATCH)


def gameLoop():
    gravity = (math.pi, 0.0003)
    run = True

    player = Player(100, 100, (0, 0, 255), pygame.Rect(0, 0, 300, 30), raptor)
    player2 = Player(700, 100, (255, 0, 0), pygame.Rect(screen.get_width() - 300, 0, 300, 30), latch)
    particle = Particle(300, 100, 10, screen)
    player.mapControls(pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_LCTRL)
    player2.mapControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL, pygame.K_RSHIFT,
                        pygame.K_n)
    players = [player, player2]
    while run:
        ms_frame = clock.tick(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0, 0, 0))
        for player in players:
            player.draw(screen)
            player.move(particle, screen, ms_frame)
        particle.move(gravity, ms_frame)
        particle.bounce(players, ms_frame)
        particle.display(screen)
        pygame.display.update()


def gameMenu():
    print()
    # TODO : Screen Menu


gameLoop()