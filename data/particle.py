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
        while i < 20:
            pygame.time.wait(10)
            i += 1


def setInvicibility(players):
    for player in players:
        player.invincible = True
        player.invincibleTimer = 0


class Particle:
    def __init__(self, x, y, size, screen, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.defaultX = x
        self.defaultY = y
        self.elasticity = 0.8
        self.move_per_second = 800
        self.size = size * 0.75
        self.color = (255, 255, 255)
        self.thickness = 0
        self.speed = 1
        self.angle = 0
        self.circle = pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

    def display(self, screen):
        self.circle = pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

    def move(self, gravity, ms_frame):
        self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0], gravity[1])
        self.x += math.sin(self.angle) * self.speed * self.move_per_second * ms_frame / 1000
        self.y -= math.cos(self.angle) * self.speed * self.move_per_second * ms_frame / 1000

    def bounce(self, players):
        for player in players:
            if player.character.attackMiddleDownRect != 0:
                if self.circle.colliderect(player.character.attackMiddleDownRect):
                    createBulletTime(self.speed)
                    if player.direction == Direction.RIGHT:
                        self.x += 10
                        self.y += player.character.attackMiddleDownRect.height + 10
                        self.angle = (3 * math.pi) / 4
                        if self.speed < 0.5:
                            self.speed *= 5 * player.character.force
                        else:
                            self.speed *= player.character.force
                        self.color = player.color
                    else:
                        self.x -= 10
                        self.y += player.character.attackMiddleDownRect.height + 10
                        self.angle = (5 * math.pi) / 4
                        if self.speed < 0.5:
                            self.speed *= 5 * player.character.force
                        else:
                            self.speed *= player.character.force
                        self.color = player.color
                    player.isAttacking = False
            elif player.character.attackMiddleUpRect != 0:
                if self.circle.colliderect(player.character.attackMiddleUpRect):
                    createBulletTime(self.speed)
                    if player.direction == Direction.RIGHT:
                        self.x += 10
                        self.angle = math.pi / 4
                        self.speed *= player.character.force
                        self.color = player.color
                    else:
                        self.x -= 10
                        self.angle = (7 * math.pi) / 4
                        self.speed *= player.character.force
                        self.color = player.color
                    player.isAttacking = False
            elif player.character.attackMiddleRect != 0:
                if self.circle.colliderect(player.character.attackMiddleRect):
                    createBulletTime(self.speed)
                    if player.direction == Direction.RIGHT:
                        self.y = player.character.attackMiddleRect.y
                        self.x += 10
                        self.angle = math.pi / 2
                        self.speed *= player.character.force
                        self.color = player.color
                    else:
                        self.y = player.character.attackMiddleRect.y
                        self.x -= 10
                        self.angle = (3 * math.pi) / 2
                        self.speed *= player.character.force
                        self.color = player.color
                    player.isAttacking = False
            elif player.character.attackDownRect != 0:
                if self.circle.colliderect(player.character.attackDownRect):
                    createBulletTime(self.speed)
                    if self.x > player.character.attackDownRect.x:
                        self.y = player.character.attackDownRect.y + 32
                        self.angle = 15
                        self.speed *= player.character.force
                        self.color = player.color
                    else:
                        self.y = player.character.attackDownRect.y + 32
                        self.angle = - 15
                        self.speed *= player.character.force
                        self.color = player.color
                    player.isAttacking = False
            elif player.character.attackUpRect != 0:
                if self.circle.colliderect(player.character.attackUpRect):
                    createBulletTime(self.speed)
                    if self.x < player.character.attackUpRect.x:
                        self.y = player.character.attackUpRect.y - 32
                        self.angle = 100
                        self.speed *= player.character.force
                        self.color = player.color

                    else:
                        self.y = player.character.attackUpRect.y - 32
                        self.angle = - 100
                        self.speed *= player.character.force
                        self.color = player.color
                    player.isAttacking = False
            if self.circle.colliderect(player.character.hitbox):
                if self.speed > 0.2:
                    if self.color != player.color and self.color != (255, 255, 255):
                        createBulletTime(self.speed)
                        for playerHit in players:
                            if playerHit.color == self.color:
                                if playerHit.character.__class__.__name__ == "Candyman" and playerHit.usingUltimate:
                                    playerHit.character.health += self.speed * 10
                                    if playerHit.character.health > playerHit.character.maxHealth:
                                        playerHit.character.health = playerHit.character.maxHealth
                                else:
                                    playerHit.power += self.speed * 5
                            if playerHit.color != self.color:
                                if playerHit.character.__class__.__name__ == "Candyman" and playerHit.usingUltimate:
                                    playerHit.character.health += self.speed * 10
                                    if playerHit.character.health > playerHit.character.maxHealth:
                                        playerHit.character.health = playerHit.character.maxHealth
                                else:
                                    playerHit.character.health -= self.speed * 10
                                playerHit.power += self.speed * 10
                        self.color = (255, 255, 255)
                        setInvicibility(players)
                else:
                    self.color = (255, 255, 255)
        if self.x > self.width - self.size:
            self.x = 2 * (self.width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= self.elasticity

        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= self.elasticity

        if self.y > (self.height - 30) - self.size:
            self.y = 2 * ((self.height - 30) - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity

    def resetPosition(self):
        self.x = self.defaultX
        self.y = self.defaultY
        self.angle = 0
        self.speed = 1
