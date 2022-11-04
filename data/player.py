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
        self.health = 100
        self.attackUpRect = 0
        self.attackDownRect = 0
        self.attackMiddleUpRect = 0
        self.attackMiddleDownRect = 0
        self.attackMiddleRect = 0
        self.isJump = True
        self.direction = Direction.RIGHT
        self.jumpCount = 0
        self.attackTimer = 0
        self.newattackTimer = 0
        self.newAttack = False
        self.moveUp = None
        self.moveDown = None
        self.moveLeft = None
        self.moveRight = None
        self.jump = None
        self.attack = None
        self.color = color
        self.specialAttack = None
        self.hprect = hprect
        self.currentSprite = 0
        self.repeatSprite = 30
        self.defaultSprite = pygame.image.load("images/RapRapDefault/RapRap_bis.png")
        self.RapRapRunningRight = []
        self.RapRapRunningLeft = []

    def initSprites(self):
        self.RapRapRunningRight = [pygame.image.load("images/RapRapRunning/RapRap_18.png"),
                                   pygame.image.load("images/RapRapRunning/RapRap_19.png"),
                                   pygame.image.load("images/RapRapRunning/RapRap_20.png"),
                                   pygame.image.load("images/RapRapRunning/RapRap_21.png"),
                                   pygame.image.load("images/RapRapRunning/RapRap_22.png"),
                                   pygame.image.load("images/RapRapRunning/RapRap_23.png")]
        for i in range(6):
            self.RapRapRunningLeft.append(pygame.transform.flip(self.RapRapRunningRight[i], True, False))

    def mapControls(self, moveUp, moveDown, moveLeft, moveRight, jump, attack, specialAttack):
        self.moveUp = moveUp
        self.moveDown = moveDown
        self.moveLeft = moveLeft
        self.moveRight = moveRight
        self.jump = jump
        self.attack = attack
        self.specialAttack = specialAttack

    def playAnimation(self, screen, listOfSprites):
        if self.currentSprite >= 6:
            self.currentSprite = 0
        screen.blit(listOfSprites[self.currentSprite],
                    (self.x - listOfSprites[self.currentSprite].get_width() // 2,
                     self.y - listOfSprites[self.currentSprite].get_height() + 100))
        self.repeatSprite -= 1
        if self.repeatSprite == 0:
            self.currentSprite += 1
            self.repeatSprite = 30

    def move(self, ball, screen):
        if self.newAttack:
            self.newattackTimer += 1
            if self.newattackTimer == 500:
                self.newAttack = False
                self.newattackTimer = 0
        if self.invincible:
            self.invincibleTimer += 1
            self.color = (255, 255, 255)
            if self.invincibleTimer >= 3000:
                self.invincible = False
                print("invincible off")
                self.color = self.colorguard
                self.invincibleTimer = 0
        if self.isAttacking:
            self.attackTimer += 1
            if self.attackTimer >= 1000:
                self.isAttacking = False
                self.newAttack = True
                self.attackTimer = 0
        keys = pygame.key.get_pressed()
        # Default character position
        if not(keys[self.moveLeft] or keys[self.moveUp] or keys[self.moveRight] or keys[self.moveDown]):
            screen.blit(self.defaultSprite,(self.x - self.defaultSprite.get_width() // 2, self.y - self.defaultSprite.get_height() + 100))
        if keys[self.moveLeft] and self.x > 0:
            self.direction = Direction.LEFT
            self.x -= self.speed / 2
            self.playAnimation(screen, self.RapRapRunningLeft)
        if keys[self.moveRight] and self.x < 800 - 10:
            self.direction = Direction.RIGHT
            self.x += self.speed / 2
            self.playAnimation(screen, self.RapRapRunningRight)
        if not self.isJump:
            if keys[self.moveUp] and self.y > 0:
                if not self.rect.colliderect(ball.circle):
                    self.y -= self.speed / 2
            if keys[self.moveDown] and self.y < 600 - 100:
                if not self.rect.colliderect(ball.circle):
                    self.y += self.speed / 2
            if keys[self.jump] and self.isJump == False and self.in_air == False:
                self.vel_y = -0.5
                self.isJump = True
            if not keys[self.jump]:
                self.isJump = False
        if keys[pygame.K_b]:
            self.isAttacking = False
        if keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveUp] and self.isAttacking == False and self.newAttack == False:
            self.isAttacking = True
            self.attackDirection = 3
        elif keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveDown] and self.isAttacking == False and self.newAttack == False:
            self.isAttacking = True
            self.attackDirection = 4
        elif keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and self.isAttacking == False and self.newAttack == False:
            self.isAttacking = True
            self.attackDirection = 5
        elif keys[self.moveUp] and keys[self.attack] and self.isAttacking == False and self.newAttack == False:
            self.isAttacking = True
            self.attackDirection = 1
        elif keys[self.moveDown] and keys[self.attack] and self.isAttacking == False and self.newAttack == False:
            self.isAttacking = True
            self.attackDirection = 2
        self.vel_y += 0.0006
        if self.vel_y > 10:
            self.vel_y = 10
        self.y += self.vel_y
        if self.y > 600 - 100:
            self.y = 600 - 100
            self.in_air = False
            self.isJump = False

    def draw(self, screen):
        self.attackMiddleRect = 0
        self.attackMiddleUpRect = 0
        self.attackMiddleDownRect = 0
        self.attackUpRect = 0
        self.attackDownRect = 0
        self.rect = pygame.Rect(self.x, self.y, 10, 100)
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.hprect,2)
        pygame.draw.rect(screen, (255, 0, 0), (self.hprect.x + 2, self.hprect.y + 2, (self.health * 296) / 100, self.hprect.height-4))
        pygame.draw.rect(self.defaultSprite, (255, 0, 0), self.defaultSprite.get_rect(), 1)
        if self.isAttacking:
            if self.attackDirection == 1:
                self.attackUpRect = pygame.Rect(self.x - 10, self.y - 20, 32, 20)
                pygame.draw.rect(screen, (255, 0, 0), self.attackUpRect)
            if self.attackDirection == 2:
                self.attackDownRect = pygame.Rect(self.x - 10, self.y + 100, 32, 20)
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

