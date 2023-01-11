import pygame
import math
from data.direction import Direction


# function used to add vectors
def addVectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return angle, length


# function used to create a time delay to intense actions
def createBulletTime(speed, clock):
    i = 0
    if speed > 0.5:
        while i < 20:
            clock.tick(120)
            i += 1


# function used to tell the players to be invincible for a short time
def setInvicibility(players):
    for player in players:
        player.invincible = True
        player.invincibleTimer = 0


# Class particle is used to tell the game how does work the particle
class Particle:
    # constructor of a particle
    # simple parameters
    # x, y: position of the particle
    # angle: angle of the particle
    # speed: speed of the particle
    # elasticity: bounce of the particle
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

    # function used to display the particle
    def display(self, screen):
        self.circle = pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

    # function used to move the ball in the screen
    def move(self, gravity, ms_frame):
        self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0], gravity[1])
        self.x += math.sin(self.angle) * self.speed * self.move_per_second * ms_frame / 1000
        self.y -= math.cos(self.angle) * self.speed * self.move_per_second * ms_frame / 1000

    # function used to calculate the bounce and the trajectory of the ball
    def bounce(self, players, clock):
        # checking if a player has hit the ball
        for player in players:
            if player.character.attackMiddleDownRect != 0:
                if self.circle.colliderect(player.character.attackMiddleDownRect):
                    createBulletTime(self.speed, clock)
                    # calculating the angle of the ball
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
                    createBulletTime(self.speed, clock)
                    # calculating the angle of the ball
                    if player.direction == Direction.RIGHT:
                        self.x += 10
                        self.angle = math.pi / 4
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    else:
                        self.x -= 10
                        self.angle = (7 * math.pi) / 4
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    player.isAttacking = False
            elif player.character.attackMiddleRect != 0:
                if self.circle.colliderect(player.character.attackMiddleRect):
                    createBulletTime(self.speed, clock)
                    if player.direction == Direction.RIGHT:
                        self.y = player.character.attackMiddleRect.y
                        self.x += 10
                        self.angle = math.pi / 2
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    else:
                        self.y = player.character.attackMiddleRect.y
                        self.x -= 10
                        self.angle = (3 * math.pi) / 2
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    player.isAttacking = False
            elif player.character.attackDownRect != 0:
                if self.circle.colliderect(player.character.attackDownRect):
                    createBulletTime(self.speed, clock)
                    # calculating the angle of the ball
                    if self.x > player.character.attackDownRect.x:
                        self.y = player.character.attackDownRect.y + 32
                        self.angle = 15
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    else:
                        self.y = player.character.attackDownRect.y + 32
                        self.angle = - 15
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    player.isAttacking = False
            elif player.character.attackUpRect != 0:
                if self.circle.colliderect(player.character.attackUpRect):
                    createBulletTime(self.speed, clock)
                    # calculating the angle of the ball
                    if self.x < player.character.attackUpRect.x:
                        self.y = player.character.attackUpRect.y - 32
                        self.angle = 100
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    else:
                        self.y = player.character.attackUpRect.y - 32
                        self.angle = - 100
                        self.speed *= player.character.force
                        self.color = player.colorguard
                    player.isAttacking = False
            # checking hitted player
            if self.circle.colliderect(player.character.hitbox):
                # checking if the ball has speed
                if self.speed > 0.5:
                    # checking if color of the ball is the same of the player
                    # if not the player will be hitted
                    if self.color != player.color and self.color != (255, 255, 255) and not player.invincible:
                        createBulletTime(self.speed, clock)
                        # boosting ultimate charge for player who hit the ball
                        self.returnOneOfTwo(player, players).power += self.speed * 5
                        # boosting more for player who was hit
                        player.power += self.speed * 10
                        player.character.health -= self.speed * 10
                        # setting ball to white color
                        self.color = (255, 255, 255)
                        setInvicibility([player])
                        # Candyman's ability is about healing herself when he is hit
                        if player.character.__class__.__name__ == "Candyman" and player.usingUltimate:
                            player.character.health += self.speed * 15
                            if player.character.health > player.character.maxHealth:
                                player.character.health = player.character.maxHealth
                else:
                    self.color = (255, 255, 255)

        # checking if the ball has hit the wall
        if self.x > self.width - self.size:
            self.x = 2 * (self.width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= self.elasticity
        # checking if the ball has hit the wall
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= self.elasticity
        # checking if the ball has hit the top
        if self.y > (self.height - 30) - self.size:
            self.y = 2 * ((self.height - 30) - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity
            # When bouncing on ground, letting ball with a minimum speed to simplify the game
            if self.speed < 0.5:
                self.speed = 0.5
        # checking if the ball has hit the bottom
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity

    # function used to reset the ball to their original position
    def resetPosition(self):
        self.x = self.defaultX
        self.y = self.defaultY
        self.angle = 0
        self.speed = 1

    # function used to return one of the two players
    @staticmethod
    def returnOneOfTwo(player, players):
        if player == players[0]:
            return players[1]
        else:
            return players[0]
