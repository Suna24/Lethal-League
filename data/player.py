import random

import pygame
from data.attackEnum import AttackEnum
from data.direction import Direction
from data.characterenum import CharacterEnum
from data.charactersClasses.Latch import Latch
from data.charactersClasses.Raptor import Raptor
from data.charactersClasses.Dice import Dice
from data.charactersClasses.Sonata import Sonata
from data.charactersClasses.Candyman import Candyman
from data.charactersClasses.Switch import Switch


# Player class
class Player:
    # init basics attributes of the player
    def __init__(self, x, y, color, hpRect, powerRect, sprite, direction, spritesList, width, height):
        self.in_air = False
        self.vel_y = 0
        self.vel_x = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.defaultX = x
        self.defaultY = y
        # voice lines attributes
        self.listOfMusics = []
        self.attackMusic = None
        self.specialAttackMusic = None
        # instantiate character (checking which character is selected)
        if sprite == CharacterEnum.RAPTOR:
            self.character = Raptor(spritesList)
            self.setVoiceLines("Raptor")
        elif sprite == CharacterEnum.DICE:
            self.character = Dice(spritesList)
            self.setVoiceLines("Dice")
        elif sprite == CharacterEnum.LATCH:
            self.character = Latch(spritesList)
            self.setVoiceLines("Latch")
        elif sprite == CharacterEnum.SONATA:
            self.character = Sonata(spritesList)
            self.setVoiceLines("Sonata")
        elif sprite == CharacterEnum.CANDYMAN:
            self.character = Candyman(spritesList)
            self.setVoiceLines("CandyMan")
        elif sprite == CharacterEnum.SWITCH:
            self.character = Switch(spritesList)
            self.setVoiceLines("Switch")
        # basing on stats from the character class, set the player's stats
        self.move_per_second = self.character.speed * 100
        self.colorguard = color
        # initiating variables for status and effects in game
        self.invincible = False
        self.invincibleTimer = 0
        self.isAttacking = False
        self.attackDirection = 0
        self.power = 0
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
        self.repeatSprite = 20
        self.ultchargeTimer = 0
        self.usingUltimate = False
        self.ultimateTimer = 0
        self.jumpReduce = 0.5
        self.blinking = 0
        self.unableToMove = False

    # function used to set up the voice lines
    def setVoiceLines(self, character):
        self.listOfMusics = ["data/musics/" + character + "/attack1.ogg",
                             "data/musics/" + character + "/attack2.ogg",
                             "data/musics/" + character + "/attack3.ogg"]
        self.attackMusic = pygame.mixer.Sound(self.listOfMusics[random.randint(0, len(self.listOfMusics) - 1)])
        self.specialAttackMusic = pygame.mixer.Sound("data/musics/" + character + "/specialAttack.ogg")

    # function used to attribute keys to the player
    def mapControls(self, moveUp, moveDown, moveLeft, moveRight, jump, attack, specialAttack):
        self.moveUp = moveUp
        self.moveDown = moveDown
        self.moveLeft = moveLeft
        self.moveRight = moveRight
        self.jump = jump
        self.attack = attack
        self.specialAttack = specialAttack

    # function used to play animations of the player
    def playAnimation(self, screen, listOfSprites):
        if self.currentSprite >= len(listOfSprites):
            self.currentSprite = 0
        if self.invincible:
            if self.repeatSprite in range(0, 10):
                pass
            else:
                screen.blit(listOfSprites[self.currentSprite],
                            (self.x - listOfSprites[self.currentSprite].get_width() // 2,
                             self.y - listOfSprites[self.currentSprite].get_height() + 100))
        else:
            screen.blit(listOfSprites[self.currentSprite],
                        (self.x - listOfSprites[self.currentSprite].get_width() // 2,
                         self.y - listOfSprites[self.currentSprite].get_height() + 100))
        self.repeatSprite -= 1
        if self.repeatSprite == 0:
            self.currentSprite += 1
            self.repeatSprite = 20

    # function used to move and do actions with the player
    def update(self, screen, ms_frame, score, channelUltimate, channelAttack):
        self.updateStatus()
        if not self.unableToMove:
            self.move(screen, ms_frame, score, channelUltimate, channelAttack)

    # function used to update invincibility and attack timers
    def updateStatus(self):
        # if in ultimating mode, update the timer and if it's over, set the mode to false
        if self.usingUltimate:
            self.character.deployUltimate()
            # Dice's ultimate is different from others, so it's handled separately
            # Dice is getting invincible while in ultimate mode
            if self.character.__class__.__name__ == "Dice":
                self.color = (255, 255, 255)
                self.invincible = True
            self.ultimateTimer += 1
            self.power -= 1
            if self.ultimateTimer == 3000:
                self.usingUltimate = False
                self.character.resetUltimate()
                if self.character.__class__.__name__ == "Dice":
                    self.color = self.colorguard
                    self.invincible = False
                self.ultimateTimer = 0
                self.power = 0
        self.ultchargeTimer += 1
        # Blocking power when it's full
        if self.power > 100:
            self.power = 100
        # resetting timers for new attacks and ult charge loading
        if self.ultchargeTimer == 200:
            self.power += 1
            self.ultchargeTimer = 0
        if self.newAttack:
            self.newattackTimer += 1
            if self.newattackTimer == 100:
                self.newAttack = False
                self.newattackTimer = 0
        if self.invincible:
            self.invincibleTimer += 1
            self.blinking += 1
            self.color = (255, 255, 255)
            if self.blinking == 20:
                self.blinking = 0
            if self.invincibleTimer >= 1000:
                self.invincible = False
                self.color = self.colorguard
                self.invincibleTimer = 0
        if self.isAttacking:
            self.attackTimer += 1
            if self.attackTimer >= 150:
                self.isAttacking = False
                self.newAttack = True
                self.attackTimer = 0

    # function used to move the player
    def move(self, screen, ms_frame, score, channelUltimate, channelAttack):
        # calculating the distance the player should move in one frame
        self.move_per_second = self.character.speed * 100
        # getting the keys pressed
        keys = pygame.key.get_pressed()
        # if the player is pressing ultimate key and the power is full, set the ultimate mode to true
        if keys[self.specialAttack] and self.power == 100:
            channelUltimate.play(self.specialAttackMusic, loops=0)
            self.usingUltimate = True
        # Default character position if both keys are pressed
        if (not (keys[self.moveLeft] or keys[self.moveRight]) or (keys[self.moveLeft] and keys[self.moveRight])) \
                and self.isAttacking is False and self.isJump is False and self.in_air is False \
                and score.hasBeenCalled is False:
            # checking the direction the player is facing to display the right sprite
            if self.direction == Direction.RIGHT:
                if not self.invincible:
                    screen.blit(self.character.sprite.defaultRight[0], (
                        self.x - self.character.sprite.defaultRight[0].get_width() // 2,
                        self.y - self.character.sprite.defaultRight[0].get_height() + 100))
                else:
                    # let player blink when invincible
                    if self.blinking in range(0, 10):
                        screen.blit(self.character.sprite.defaultRight[0], (
                            self.x - self.character.sprite.defaultRight[0].get_width() // 2,
                            self.y - self.character.sprite.defaultRight[0].get_height() + 100))
                    pass
            else:
                if self.invincible is False:
                    screen.blit(self.character.sprite.defaultLeft[0], (
                        self.x - self.character.sprite.defaultLeft[0].get_width() // 2,
                        self.y - self.character.sprite.defaultLeft[0].get_height() + 100))
                else:
                    # let player blink when invincible
                    if (self.blinking in range(0, 10)) is True:
                        screen.blit(self.character.sprite.defaultLeft[0], (
                            self.x - self.character.sprite.defaultLeft[0].get_width() // 2,
                            self.y - self.character.sprite.defaultLeft[0].get_height() + 100))
                    pass
        else:
            # if the player is pressing left key, move left and display the left sprite
            if keys[self.moveLeft] and self.x > 0 and self.isAttacking is False:
                self.direction = Direction.LEFT
                if (self.isJump is False and self.in_air is False) \
                        or (self.usingUltimate and self.character.__class__.__name__ == "Raptor"):
                    self.x -= self.move_per_second * ms_frame / 1000
                else:
                    self.x -= self.move_per_second * ms_frame / 1000 * self.jumpReduce
                if not self.isJump:
                    self.playAnimation(screen, self.character.sprite.runningLeft)
            # if the player is pressing right key, move right and display the right sprite
            if keys[self.moveRight] and self.x < 1600 - 10 and self.isAttacking is False:
                self.direction = Direction.RIGHT
                if (self.isJump is False and self.in_air is False) \
                        or (self.usingUltimate and self.character.__class__.__name__ == "Raptor"):
                    self.x += self.move_per_second * ms_frame / 1000
                else:
                    self.x += self.move_per_second * ms_frame / 1000 * self.jumpReduce
                if not self.isJump:
                    self.playAnimation(screen, self.character.sprite.runningRight)
        if not self.isJump:
            # if the player is pressing jump key, checking if not jumping and not in air, then jump
            if keys[self.jump] and self.isJump is False and self.in_air is False and self.isAttacking is False:
                self.vel_y = -5
                self.isJump = True
            if not keys[self.jump]:
                self.isJump = False
        elif self.isJump and not self.isAttacking:
            if self.direction == Direction.RIGHT:
                self.playAnimation(screen, self.character.sprite.jumpingRight)
            else:
                self.playAnimation(screen, self.character.sprite.jumpingLeft)
        # if the player pressed the attack key, and pressed left or right and moveUp then attacking on Up attack
        if keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveUp] \
                and self.isAttacking is False and self.newAttack is False:
            self.updateWhenAttacking(AttackEnum.ATTACKMIDDLEUP, channelAttack)
            # if the player pressed the attack key, and pressed left or right and moveDown then attacking on Down attack
        elif keys[self.attack] and (keys[self.moveRight] or keys[self.moveLeft]) and keys[self.moveDown] \
                and self.isAttacking is False and self.newAttack is False:
            self.updateWhenAttacking(AttackEnum.ATTACKMIDDLEDOWN, channelAttack)
            # if the player pressed the attack key, and pressed left or right then attacking on middle attack
        elif keys[self.attack] and (
                keys[self.moveRight] or keys[self.moveLeft]) and self.isAttacking is False and self.newAttack is False:
            self.updateWhenAttacking(AttackEnum.ATTACKMIDDLE, channelAttack)
            # if the player pressed the attack key, and pressed top then attacking on top attack
        elif keys[self.moveUp] and keys[self.attack] and self.isAttacking is False and self.newAttack is False:
            self.updateWhenAttacking(AttackEnum.ATTACKTOP, channelAttack)
            # if the player pressed the attack key, and pressed down then attacking on down attack
        elif keys[self.moveDown] and keys[self.attack] and self.isAttacking is False and self.newAttack is False:
            self.updateWhenAttacking(AttackEnum.ATTACKBOTTOM, channelAttack)
        # adding velocity y to the player
        self.vel_y += 0.038
        # if the player velocity y is bigger than 5, set it to 5
        if self.vel_y > 5:
            self.vel_y = 5
        # adding velocity y to the player y
        self.y += self.vel_y
        # if the player hits the ground, set the player y to the ground y
        if self.y > self.height - 100:
            self.y = self.height - 100
            self.in_air = False
            self.isJump = False

    # function to update some status and play sounds while attacking
    def updateWhenAttacking(self, attackDirection, channelAttack):
        self.isAttacking = True
        self.attackDirection = attackDirection
        # play sounds and generate a new random one among the list
        channelAttack.play(self.attackMusic, loops=0)
        self.attackMusic = pygame.mixer.Sound(self.listOfMusics[random.randint(0, 2)])

    # function to draw on screen the player
    def draw(self, screen):
        # if the player is attacking, display the right sprite
        self.character.attackMiddleRect = 0
        self.character.attackMiddleUpRect = 0
        self.character.attackMiddleDownRect = 0
        self.character.attackUpRect = 0
        self.character.attackDownRect = 0
        self.character.hitbox.x = self.x - self.character.xhitboxoffset
        self.character.hitbox.y = self.y - self.character.yhitboxoffset
        # pygame.draw.rect(screen, self.color, self.character.hitbox)
        #displaying HUD for the player
        pygame.draw.polygon(screen, self.color, ((self.x - 20, self.y - 150), (self.x + 20, self.y - 150),
                                                 (self.x, self.y - 125)))
        pygame.draw.rect(screen, (255, 255, 255), self.hprect, 2)
        pygame.draw.rect(screen, (255, 0, 0), self.powerRect, 2)
        pygame.draw.rect(screen, (0, 0, 0), (self.powerRect.x + 2, self.powerRect.y + 2, (self.power * 396) / 100, 16))
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.hprect.x + 2, self.hprect.y + 2, (self.character.health * 396) / 100,
                          self.hprect.height - 4))
        # if the player is attacking, display the right sprite
        # and play the right sound and animation
        if self.isAttacking:
            if self.attackDirection == AttackEnum.ATTACKTOP:
                self.character.attackUpRect = self.character.attackUpRectDefault
                self.character.attackUpRect.x = self.x - 10 - self.character.aURxoffset
                self.character.attackUpRect.y = self.y - 20 - self.character.aURyoffset
                # pygame.draw.rect(screen, (255, 0, 0), self.character.attackUpRect)
                if self.direction == Direction.RIGHT:
                    self.playAnimation(screen, self.character.sprite.attackingAboveRight)
                else:
                    self.playAnimation(screen, self.character.sprite.attackingAboveLeft)
            if self.attackDirection == AttackEnum.ATTACKBOTTOM:
                self.character.attackDownRect = self.character.attackDownRectDefault
                self.character.attackDownRect.x = self.x - 10 - self.character.aDRxoffset
                self.character.attackDownRect.y = self.y + 100 - self.character.aDRyoffset
                # pygame.draw.rect(screen, (0, 255, 0), self.character.attackDownRect)
                if self.direction == Direction.RIGHT:
                    self.playAnimation(screen, self.character.sprite.attackingBelowRight)
                else:
                    self.playAnimation(screen, self.character.sprite.attackingBelowLeft)
            if self.attackDirection == AttackEnum.ATTACKMIDDLEUP:
                self.character.attackMiddleUpRect = self.character.attackMiddleUpRectDefault
                if self.direction == Direction.RIGHT:
                    self.character.attackMiddleUpRect.x = self.x + 10 - self.character.aMURxoffsetRight
                    self.character.attackMiddleUpRect.y = self.y - 20 - self.character.aMURyoffsetRight
                    self.playAnimation(screen, self.character.sprite.attackingTopRight)
                else:
                    self.character.attackMiddleUpRect.x = self.x - 20 - self.character.aMURxoffsetLeft
                    self.character.attackMiddleUpRect.y = self.y - 20 - self.character.aMURyoffsetLeft
                    self.playAnimation(screen, self.character.sprite.attackingTopLeft)
                # pygame.draw.rect(screen, (255, 255, 0), self.character.attackMiddleUpRect)
            if self.attackDirection == AttackEnum.ATTACKMIDDLEDOWN:
                self.character.attackMiddleDownRect = self.character.attackMiddleDownRectDefault
                if self.direction == Direction.RIGHT:
                    self.character.attackMiddleDownRect.x = self.x + 10 - self.character.aMDRxoffsetRight
                    self.character.attackMiddleDownRect.y = self.y + 60 - self.character.aMDRyoffsetRight
                    self.playAnimation(screen, self.character.sprite.attackingBottomRight)
                else:
                    self.character.attackMiddleDownRect.x = self.x - 20 - self.character.aMDRxoffsetLeft
                    self.character.attackMiddleDownRect.y = self.y + 60 - self.character.aMDRyoffsetLeft
                    self.playAnimation(screen, self.character.sprite.attackingBottomLeft)
                # pygame.draw.rect(screen, (255, 0, 255), self.character.attackMiddleDownRect)
            if self.attackDirection == AttackEnum.ATTACKMIDDLE:
                self.character.attackMiddleRect = self.character.attackMiddleRectDefault
                if self.direction == Direction.RIGHT:
                    self.character.attackMiddleRect.x = self.x + 10 - self.character.aMRxoffsetRight
                    self.character.attackMiddleRect.y = self.y + 20 - self.character.aMRyoffsetRight
                    self.playAnimation(screen, self.character.sprite.attackingMiddleRight)
                else:
                    self.character.attackMiddleRect.x = self.x - 20 - self.character.aMRxoffsetLeft
                    self.character.attackMiddleRect.y = self.y + 20 - self.character.aMRyoffsetLeft
                    self.playAnimation(screen, self.character.sprite.attackingMiddleLeft)
                # pygame.draw.rect(screen, (0, 255, 255), self.character.attackMiddleRect)

    # function used to replace the default position of the player
    def resetPosition(self):
        self.x = self.defaultX
        self.y = self.defaultY
        self.character.health = self.character.maxHealth
