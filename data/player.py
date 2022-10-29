import pygame
from data.direction import Direction


class Player:
    def __init__(self, x, y, color,hprect):
        self.in_air = False
        self.vel_y = 0
        self.vel_x = 0
        self.x = x
        self.y = y
        self.speed = 0.5
        self.colorguard = color
        self.invincible = False
        self.invincibleTimer = 0
        self.onGround = True
        self.isAttacking = False
        self.attackDirection = 0
        self.rect = pygame.Rect(self.x, self.y, 10, 60)
        self.health = 100
        self.attackUpRect = 0
        self.attackDownRect = 0
        self.attackMiddleUpRect = 0
        self.attackMiddleDownRect = 0
        self.attackMiddleRect = 0
        self.isJump = True
        self.direction = Direction.RIGHT
        self.jumpCount = 0
        self.hprect = hprect
        self.moveUp = None
        self.moveDown = None
        self.moveLeft = None
        self.moveRight = None
        self.jump = None
        self.attack = None
        self.color = color
        self.specialAttack = None

    def mapControls(self, moveUp, moveDown, moveLeft, moveRight, jump, attack, specialAttack):
        self.moveUp = moveUp
        self.moveDown = moveDown
        self.moveLeft = moveLeft
        self.moveRight = moveRight
        self.jump = jump
        self.attack = attack
        self.specialAttack = specialAttack

    def move(self, ball):
        if self.invincible:
            self.invincibleTimer += 1
            self.color = (255, 255, 255)
            if self.invincibleTimer >= 3000:
                self.invincible = False
                print("invincible off")
                self.color = self.colorguard
                self.invincibleTimer = 0
        keys = pygame.key.get_pressed()
        if keys[self.moveLeft] and self.x > 0:
            self.direction = Direction.LEFT
            self.x -= self.speed / 2
        if keys[self.moveRight] and self.x < 800 - 10:
            self.direction = Direction.RIGHT
            self.x += self.speed / 2
        if not self.isJump:
            if keys[self.moveUp] and self.y > 0:
                if not self.rect.colliderect(ball.circle):
                    self.y -= self.speed / 2
            if keys[self.moveDown] and self.y < 600 - 60:
                if not self.rect.colliderect(ball.circle):
                    self.y += self.speed / 2
            if keys[self.jump] and self.isJump == False and self.in_air == False:
                self.vel_y = -0.5
                self.isJump = True
            if not keys[self.jump]:
                self.isJump = False
        if keys[self.moveUp] and keys[self.attack]:
            self.isAttacking = True
            self.attackDirection = 1
        if keys[pygame.K_b]:
            self.isAttacking = False
        if keys[self.moveDown] and keys[self.attack]:
            self.isAttacking = True
            self.attackDirection = 2
        if keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]):
            self.isAttacking = True
            self.attackDirection = 5
        if keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveUp]:
            self.isAttacking = True
            self.attackDirection = 3
        if keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveDown]:
            self.isAttacking = True
            self.attackDirection = 4
        self.vel_y += 0.0006
        if self.vel_y > 10:
            self.vel_y = 10
        self.y += self.vel_y
        if self.y > 600 - 60:
            self.y = 600 - 60
            self.in_air = False
            self.isJump = False

    def draw(self, screen):
        self.attackMiddleRect = 0
        self.attackMiddleUpRect = 0
        self.attackMiddleDownRect = 0
        self.attackUpRect = 0
        self.attackDownRect = 0
        self.rect = pygame.Rect(self.x, self.y, 10, 60)
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.hprect,2)
        pygame.draw.rect(screen, (255, 0, 0), (self.hprect.x + 2, self.hprect.y + 2, (self.health * 296) / 100, self.hprect.height-4))
        if self.isAttacking:
            if self.attackDirection == 1:
                self.attackUpRect = pygame.Rect(self.x - 10, self.y - 20, 32, 20)
                pygame.draw.rect(screen, (255, 0, 0), self.attackUpRect)
            if self.attackDirection == 2:
                self.attackDownRect = pygame.Rect(self.x - 10, self.y + 60, 32, 20)
                pygame.draw.rect(screen, (0, 255, 0), self.attackDownRect)
            if self.attackDirection == 3:
                if self.direction == Direction.RIGHT:
                    self.attackMiddleUpRect = pygame.Rect(self.x + 10, self.y - 20, 20, 20)
                else:
                    self.attackMiddleUpRect = pygame.Rect(self.x - 20, self.y - 20, 20, 20)
                pygame.draw.rect(screen, (255, 255, 0), self.attackMiddleUpRect)
            if self.attackDirection == 4:
                if self.direction == Direction.RIGHT:
                    self.attackMiddleDownRect = pygame.Rect(self.x + 10, self.y + 40, 20, 20)
                else:
                    self.attackMiddleDownRect = pygame.Rect(self.x - 20, self.y + 40, 20, 20)
                pygame.draw.rect(screen, (255, 0, 255), self.attackMiddleDownRect)
            if self.attackDirection == 5:
                if self.direction == Direction.RIGHT:
                    self.attackMiddleRect = pygame.Rect(self.x + 10, self.y + 20, 20, 20)
                else:
                    self.attackMiddleRect = pygame.Rect(self.x - 20, self.y + 20, 20, 20)
                pygame.draw.rect(screen, (0, 255, 255), self.attackMiddleRect)
