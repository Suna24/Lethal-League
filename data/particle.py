import pygame
import math
from data.direction import Direction


def addVectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return angle, length


def createBulletTime(speed):
    i = 0
    if speed > 0.5:
        while i < 10:
            pygame.time.wait(10)
            i += 1


class Particle:
    def __init__(self, x, y, size, screen):
        self.x = x
        self.y = y
        self.elasticity = 0.75
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 0
        self.speed = 1
        self.angle = 0
        self.circle = pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def display(self, screen):
        self.circle = pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def move(self, gravity):
        self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0], gravity[1])
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self, players):
        for player in players:
            if player.attackMiddleDownRect != 0:
                if self.circle.colliderect(player.attackMiddleDownRect):
                    createBulletTime(self.speed)
                    if player.direction == Direction.RIGHT:
                        self.x += 10
                        self.angle = (3 * math.pi) / 4
                        self.speed *= 2
                    else:
                        self.x -= 10
                        self.angle = (5 * math.pi) / 4
                        self.speed *= 2
            elif player.attackMiddleUpRect != 0:
                if self.circle.colliderect(player.attackMiddleUpRect):
                    createBulletTime(self.speed)
                    if player.direction == Direction.RIGHT:
                        self.x += 10
                        self.angle = math.pi / 4
                        self.speed *= 2
                    else:
                        self.x -= 10
                        self.angle = (7 * math.pi) / 4
                        self.speed *= 2
            elif player.attackMiddleRect != 0:
                if self.circle.colliderect(player.attackMiddleRect):
                    createBulletTime(self.speed)
                    if player.direction == Direction.RIGHT:
                        self.y = player.attackMiddleRect.y
                        self.x += 10
                        self.angle = math.pi / 2
                        self.speed *= 2
                    else:
                        self.y = player.attackMiddleRect.y
                        self.x -= 10
                        self.angle = (3 * math.pi) / 2
                        self.speed *= 2
            elif player.attackDownRect != 0:
                if self.circle.colliderect(player.attackDownRect):
                    createBulletTime(self.speed)
                    if self.x > player.attackDownRect.x:
                        self.y = player.attackDownRect.y + 32
                        self.angle = 15
                        self.speed *= 2
                    else:
                        self.y = player.attackDownRect.y + 32
                        self.angle = - 15
                        self.speed *= 2
            elif player.attackUpRect != 0:
                if self.circle.colliderect(player.attackUpRect):
                    createBulletTime(self.speed)
                    if self.x < player.attackUpRect.x:
                        self.y = player.attackUpRect.y - 32
                        self.angle = 100
                        self.speed *= 2
                    else:
                        self.y = player.attackUpRect.y - 32
                        self.angle = - 100
                        self.speed *= 2
            if self.circle.colliderect(player.rect):
                if self.speed > 0.2:
                    if self.x < player.x:
                        self.x = player.x - 20
                        player.x = self.x + 22
                    elif self.x > player.x:
                        self.x = player.x + 21
                        player.x = self.x - 22
                    elif self.y > player.y:
                        self.x = player.x + 10
                    elif self.y < player.y:
                        if self.x < player.x:
                            self.x = player.x - 10
                        elif self.x > player.x:
                            self.x = player.x + 10
        if self.x > 800 - self.size:
            self.x = 2 * (800 - self.size) - self.x
            self.angle = - self.angle
            self.speed *= self.elasticity

        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= self.elasticity

        if self.y > 600 - self.size:
            self.y = 2 * (600 - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity
