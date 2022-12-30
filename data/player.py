import pygame
from data.particle import Particle
from data.direction import Direction
from data.characterenum import CharacterEnum
from data.charactersClasses.Latch import Latch
from data.charactersClasses.Raptor import Raptor
from data.charactersClasses.Dice import Dice
from data.charactersClasses.Sonata import Sonata
from data.charactersClasses.Candyman import Candyman
from data.charactersClasses.Switch import Switch

class Player:
    def __init__(self, x, y, color, hpRect, powerRect, sprite, direction, spritesList):
        self.in_air = False
        self.vel_y = 0
        self.vel_x = 0
        self.x = x
        self.y = y
        self.defaultX = x
        self.defaultY = y
        # instantiate character
        if sprite == CharacterEnum.RAPTOR:
            self.character = Raptor(spritesList[0])
        elif sprite == CharacterEnum.DICE:
            self.character = Dice(spritesList[2])
        elif sprite == CharacterEnum.LATCH:
            self.character = Latch(spritesList[1])
        elif sprite == CharacterEnum.SONATA:
            self.character = Sonata(spritesList[3])
        elif sprite == CharacterEnum.CANDYMAN:
            self.character = Candyman(spritesList[4])
        elif sprite == CharacterEnum.SWITCH:
            self.character = Switch(spritesList[5])
        self.move_per_second = self.character.speed * 100
        self.colorguard = color
        self.invincible = False
        self.invincibleTimer = 0
        self.isAttacking = False
        self.attackDirection = 0
        self.power = 100
        self.powerRect = powerRect
        self.isJump = True
        self.direction = direction
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
        self.hprect = hpRect
        self.currentSprite = 0
        self.repeatSprite = 30
        self.ultchargeTimer = 0
        self.usingUltimate = False
        self.ultimateTimer = 0

    def mapControls(self, moveUp, moveDown, moveLeft, moveRight, jump, attack, specialAttack):
        self.moveUp = moveUp
        self.moveDown = moveDown
        self.moveLeft = moveLeft
        self.moveRight = moveRight
        self.jump = jump
        self.attack = attack
        self.specialAttack = specialAttack

    def playAnimation(self, screen, listOfSprites):
        if self.currentSprite >= len(listOfSprites):
            self.currentSprite = 0
        screen.blit(listOfSprites[self.currentSprite],
                    (self.x - listOfSprites[self.currentSprite].get_width() // 2,
                     self.y - listOfSprites[self.currentSprite].get_height() + 100))
        self.repeatSprite -= 1
        if self.repeatSprite == 0:
            self.currentSprite += 1
            self.repeatSprite = 30

    def move(self, screen, ms_frame, score):
        self.move_per_second = self.character.speed * 100
        if self.usingUltimate:
            print("using ultimate")
            self.character.deployUltimate()
            if self.character.__class__.__name__ == "Dice":
                self.color = (255, 255, 255)
            self.ultimateTimer += 1
            self.power -= 1
            if self.ultimateTimer == 3000:
                self.usingUltimate = False
                self.character.resetUltimate()
                if self.character.__class__.__name__ == "Dice":
                    self.color = self.colorguard
                self.ultimateTimer = 0
                self.power = 0
        self.ultchargeTimer += 1
        if self.power > 100:
            self.power = 100
        if self.ultchargeTimer == 600:
            self.power += 1
            self.ultchargeTimer = 0
        if self.newAttack:
            self.newattackTimer += 1
            if self.newattackTimer == 100:
                self.newAttack = False
                self.newattackTimer = 0
        if self.invincible:
            self.invincibleTimer += 1
            self.color = (255, 255, 255)
            if self.invincibleTimer >= 1000:
                self.invincible = False
                print("invincible off")
                self.color = self.colorguard
                self.invincibleTimer = 0
        if self.isAttacking:
            self.attackTimer += 1
            if self.attackTimer >= 150:
                self.isAttacking = False
                self.newAttack = True
                self.attackTimer = 0
        keys = pygame.key.get_pressed()
        # Default character position if both keys are pressed
        if keys[self.specialAttack] and self.power == 100:
            self.usingUltimate = True
        if (not (keys[self.moveLeft] or keys[self.moveRight]) or (keys[self.moveLeft] and keys[self.moveRight])) \
                and self.isAttacking is False and self.isJump is False and self.in_air is False and score.hasBeenCalled is False:
            if self.direction == Direction.RIGHT:
                screen.blit(self.character.sprite.defaultRight[0], (
                    self.x - self.character.sprite.defaultRight[0].get_width() // 2,
                    self.y - self.character.sprite.defaultRight[0].get_height() + 100))
            else:
                screen.blit(self.character.sprite.defaultLeft[0], (
                    self.x - self.character.sprite.defaultLeft[0].get_width() // 2,
                    self.y - self.character.sprite.defaultLeft[0].get_height() + 100))
        else:
            if keys[self.moveLeft] and self.x > 0 and self.isAttacking is False:
                self.direction = Direction.LEFT
                self.x -= self.move_per_second * ms_frame / 1000
                if not self.isJump:
                    self.playAnimation(screen, self.character.sprite.runningLeft)
            if keys[self.moveRight] and self.x < 800 - 10 and self.isAttacking is False:
                self.direction = Direction.RIGHT
                self.x += self.move_per_second * ms_frame / 1000
                if not self.isJump:
                    self.playAnimation(screen, self.character.sprite.runningRight)
        if not self.isJump:
            if keys[self.jump] and self.isJump is False and self.in_air is False and self.isAttacking is False:
                self.vel_y = -2
                self.isJump = True
            if not keys[self.jump]:
                self.isJump = False
        elif self.isJump and not self.isAttacking:
            if self.direction == Direction.RIGHT:
                self.playAnimation(screen, self.character.sprite.jumpingRight)
            else:
                self.playAnimation(screen, self.character.sprite.jumpingLeft)
        if keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveUp] \
                and self.isAttacking is False and self.newAttack is False:
            self.isAttacking = True
            self.attackDirection = 3
        elif keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveDown] \
                and self.isAttacking is False and self.newAttack is False:
            self.isAttacking = True
            self.attackDirection = 4
        elif keys[self.attack] and (
                keys[self.moveRight] or keys[self.moveLeft]) and self.isAttacking is False and self.newAttack is False:
            self.isAttacking = True
            self.attackDirection = 5
        elif keys[self.moveUp] and keys[self.attack] and self.isAttacking is False and self.newAttack is False:
            self.isAttacking = True
            self.attackDirection = 1
        elif keys[self.moveDown] and keys[self.attack] and self.isAttacking is False and self.newAttack is False:
            self.isAttacking = True
            self.attackDirection = 2
        self.vel_y += 0.008
        if self.vel_y > 10:
            self.vel_y = 10
        self.y += self.vel_y
        if self.y > 600 - 100:
            self.y = 600 - 100
            self.in_air = False
            self.isJump = False

    def draw(self, screen):
        self.character.attackMiddleRect = 0
        self.character.attackMiddleUpRect = 0
        self.character.attackMiddleDownRect = 0
        self.character.attackUpRect = 0
        self.character.attackDownRect = 0
        self.character.hitbox.x = self.x - self.character.xhitboxoffset
        self.character.hitbox.y = self.y - self.character.yhitboxoffset
        pygame.draw.rect(screen, self.color, self.character.hitbox)
        pygame.draw.rect(screen, (255, 255, 255), self.hprect, 2)
        pygame.draw.rect(screen, (255, 0, 0), self.powerRect, 2)
        pygame.draw.rect(screen, (0, 0, 0), (self.powerRect.x + 2, self.powerRect.y + 2, (self.power * 296) / 100, 6))
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.hprect.x + 2, self.hprect.y + 2, (self.character.health * 296) / 100,
                          self.hprect.height - 4))
        if self.isAttacking:
            if self.attackDirection == 1:
                self.character.attackUpRect = self.character.attackUpRectDefault
                self.character.attackUpRect.x = self.x - 10 - self.character.aURxoffset
                self.character.attackUpRect.y = self.y - 20 - self.character.aURyoffset
                pygame.draw.rect(screen, (255, 0, 0), self.character.attackUpRect)
                if self.direction == Direction.RIGHT:
                    self.playAnimation(screen, self.character.sprite.attackingAboveRight)
                else:
                    self.playAnimation(screen, self.character.sprite.attackingAboveLeft)
            if self.attackDirection == 2:
                self.character.attackDownRect = self.character.attackDownRectDefault
                self.character.attackDownRect.x = self.x - 10 - self.character.aDRxoffset
                self.character.attackDownRect.y = self.y + 100 - self.character.aDRyoffset
                pygame.draw.rect(screen, (0, 255, 0), self.character.attackDownRect)
                if self.direction == Direction.RIGHT:
                    self.playAnimation(screen, self.character.sprite.attackingBelowRight)
                else:
                    self.playAnimation(screen, self.character.sprite.attackingBelowLeft)
            if self.attackDirection == 3:
                self.character.attackMiddleUpRect = self.character.attackMiddleUpRectDefault
                if self.direction == Direction.RIGHT:
                    self.character.attackMiddleUpRect.x = self.x + 10 - self.character.aMURxoffsetRight
                    self.character.attackMiddleUpRect.y = self.y - 20 - self.character.aMURyoffsetRight
                    self.playAnimation(screen, self.character.sprite.attackingTopRight)
                else:
                    self.character.attackMiddleUpRect.x = self.x - 20 - self.character.aMURxoffsetLeft
                    self.character.attackMiddleUpRect.y = self.y - 20 - self.character.aMURyoffsetLeft
                    self.playAnimation(screen, self.character.sprite.attackingTopLeft)
                pygame.draw.rect(screen, (255, 255, 0), self.character.attackMiddleUpRect)
            if self.attackDirection == 4:
                self.character.attackMiddleDownRect = self.character.attackMiddleDownRectDefault
                if self.direction == Direction.RIGHT:
                    self.character.attackMiddleDownRect.x = self.x + 10 - self.character.aMDRxoffsetRight
                    self.character.attackMiddleDownRect.y = self.y + 60 - self.character.aMDRyoffsetRight
                    self.playAnimation(screen, self.character.sprite.attackingBottomRight)
                else:
                    self.character.attackMiddleDownRect.x = self.x - 20 - self.character.aMDRxoffsetLeft
                    self.character.attackMiddleDownRect.y = self.y + 60 - self.character.aMDRyoffsetLeft
                    self.playAnimation(screen, self.character.sprite.attackingBottomLeft)
                pygame.draw.rect(screen, (255, 0, 255), self.character.attackMiddleDownRect)
            if self.attackDirection == 5:
                self.character.attackMiddleRect = self.character.attackMiddleRectDefault
                if self.direction == Direction.RIGHT:
                    self.character.attackMiddleRect.x = self.x + 10 - self.character.aMRxoffsetRight
                    self.character.attackMiddleRect.y = self.y + 20 - self.character.aMRyoffsetRight
                    self.playAnimation(screen, self.character.sprite.attackingMiddleRight)
                else:
                    self.character.attackMiddleRect.x = self.x - 20 - self.character.aMRxoffsetLeft
                    self.character.attackMiddleRect.y = self.y + 20 - self.character.aMRyoffsetLeft
                    self.playAnimation(screen, self.character.sprite.attackingMiddleLeft)
                pygame.draw.rect(screen, (0, 255, 255), self.character.attackMiddleRect)

    def resetPosition(self):
        self.x = self.defaultX
        self.y = self.defaultY
        self.character.health = self.character.maxHealth
