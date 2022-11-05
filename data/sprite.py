import pygame
from data.character import Character


class Sprite:

    def __init__(self):
        # All lists of sprites that we need
        self.defaultRight = None
        self.defaultLeft = None
        self.runningRight = None
        self.runningLeft = None
        self.jumpingRight = None
        self.jumpingLeft = None
        self.attackingTopRight = None
        self.attackingTopLeft = None
        self.attackingMiddleRight = None
        self.attackingMiddleLeft = None
        self.attackingBottomRight = None
        self.attackingBottomLeft = None
        self.victoryRight = None
        self.victoryLeft = None
        self.hittedRight = None
        self.hittedLeft = None

    def __init__(self, character):
        # If the character chose is Raptor
        if character == Character.RAPTOR:
            self.initRaptorSprites()
        # If the character chose is Switch
        elif character == Character.SWITCH:
            self.initSwitchSprites()
        # If the character chose is CandyMan
        elif character == Character.CANDYMAN:
            self.initCandyManSprites()
        # If the character chose is Sonata
        elif character == Character.SONATA:
            self.initSonataSprites()
        # If the character chose is Latch
        elif character == Character.LATCH:
            self.initLatchSprites()
        # If the character chose is Dice
        elif character == Character.DICE:
            self.initDiceSprites()

    def initRaptorSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("images/Raptor/Default/Raptor_Default_bis.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("images/Raptor/Running/Raptor_18.png"),
                             pygame.image.load("images/Raptor/Running/Raptor_19.png"),
                             pygame.image.load("images/Raptor/Running/Raptor_20.png"),
                             pygame.image.load("images/Raptor/Running/Raptor_21.png"),
                             pygame.image.load("images/Raptor/Running/Raptor_22.png"),
                             pygame.image.load("images/Raptor/Running/Raptor_23.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("images/Raptor/Jumping/Raptor_03.png"),
                             pygame.image.load("images/Raptor/Jumping/Raptor_04.png"),
                             pygame.image.load("images/Raptor/Jumping/Raptor_05.png")]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("images/Raptor/AttackingTop/Raptor_12.png"),
                                  pygame.image.load("images/Raptor/AttackingTop/Raptor_13.png"),
                                  pygame.image.load("images/Raptor/AttackingTop/Raptor_14.png"),
                                  pygame.image.load("images/Raptor/AttackingTop/Raptor_15.png"),
                                  pygame.image.load("images/Raptor/AttackingTop/Raptor_16.png"),
                                  pygame.image.load("images/Raptor/AttackingTop/Raptor_17.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("images/Raptor/AttackingMiddle/Raptor_06.png"),
                                     pygame.image.load("images/Raptor/AttackingMiddle/Raptor_07.png"),
                                     pygame.image.load("images/Raptor/AttackingMiddle/Raptor_08.png"),
                                     pygame.image.load("images/Raptor/AttackingMiddle/Raptor_09.png"),
                                     pygame.image.load("images/Raptor/AttackingMiddle/Raptor_10.png"),
                                     pygame.image.load("images/Raptor/AttackingMiddle/Raptor_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("images/Raptor/AttackingBottom/Raptor_25.png"),
                                     pygame.image.load("images/Raptor/AttackingBottom/Raptor_26.png"),
                                     pygame.image.load("images/Raptor/AttackingBottom/Raptor_27.png"),
                                     pygame.image.load("images/Raptor/AttackingBottom/Raptor_28.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("images/Raptor/Victory/Raptor_37.png"),
                             pygame.image.load("images/Raptor/Victory/Raptor_38.png"),
                             pygame.image.load("images/Raptor/Victory/Raptor_39.png"),
                             pygame.image.load("images/Raptor/Victory/Raptor_40.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("images/Raptor/Hitted/Raptor_24.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)


    def initSwitchSprites(self):
        print()
        # TODO

    def initCandyManSprites(self):
        print()
        # TODO

    def initSonataSprites(self):
        print()
        # TODO

    def initLatchSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("images/Latch/Default/Latch_Default.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("images/Latch/Running/Latch_18.png"),
                             pygame.image.load("images/Latch/Running/Latch_19.png"),
                             pygame.image.load("images/Latch/Running/Latch_20.png"),
                             pygame.image.load("images/Latch/Running/Latch_21.png"),
                             pygame.image.load("images/Latch/Running/Latch_22.png"),
                             pygame.image.load("images/Latch/Running/Latch_23.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("images/Latch/Jumping/Latch_03.png"),
                             pygame.image.load("images/Latch/Jumping/Latch_04.png"),
                             pygame.image.load("images/Latch/Jumping/Latch_05.png"),
                             pygame.image.load("images/Latch/Jumping/Latch_06.png"),]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("images/Latch/AttackingTop/Latch_12.png"),
                                  pygame.image.load("images/Latch/AttackingTop/Latch_13.png"),
                                  pygame.image.load("images/Latch/AttackingTop/Latch_14.png"),
                                  pygame.image.load("images/Latch/AttackingTop/Latch_15.png"),
                                  pygame.image.load("images/Latch/AttackingTop/Latch_16.png"),
                                  pygame.image.load("images/Latch/AttackingTop/Latch_17.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("images/Latch/AttackingMiddle/Latch_07.png"),
                                     pygame.image.load("images/Latch/AttackingMiddle/Latch_08.png"),
                                     pygame.image.load("images/Latch/AttackingMiddle/Latch_09.png"),
                                     pygame.image.load("images/Latch/AttackingMiddle/Latch_10.png"),
                                     pygame.image.load("images/Latch/AttackingMiddle/Latch_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("images/Latch/AttackingBottom/Latch_41.png"),
                                     pygame.image.load("images/Latch/AttackingBottom/Latch_42.png"),
                                     pygame.image.load("images/Latch/AttackingBottom/Latch_43.png"),
                                     pygame.image.load("images/Latch/AttackingBottom/Latch_44.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("images/Latch/Victory/Latch_50.png"),
                             pygame.image.load("images/Latch/Victory/Latch_51.png"),
                             pygame.image.load("images/Latch/Victory/Latch_52.png"),
                             pygame.image.load("images/Latch/Victory/Latch_53.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("images/Latch/Hitted/Latch_24.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    def initDiceSprites(self):
        print()
        # TODO

    def mirrorSprites(self, listOfSprites):
        listOfSpritesMirrored = []
        for i in range(len(listOfSprites)):
            listOfSpritesMirrored.append(pygame.transform.flip(listOfSprites[i], True, False))
        return listOfSpritesMirrored
