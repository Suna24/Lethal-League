import pygame
from data.characterenum import CharacterEnum


class Sprite:

    def __init__(self, character, size):
        # All lists of sprites that we need

        self.defaultRight = None
        self.defaultLeft = None
        self.runningRight = None
        self.runningLeft = None
        self.jumpingRight = None
        self.jumpingLeft = None
        self.fallingRight = None
        self.fallingLeft = None
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
        self.attackingAboveRight = None
        self.attackingAboveLeft = None
        self.attackingBelowRight = None
        self.attackingBelowLeft = None

        self.size = size
        # If the character chose is Raptor
        if character == CharacterEnum.RAPTOR:
            self.initRaptorSprites()
        # If the character chose is Switch
        elif character == CharacterEnum.SWITCH:
            self.initSwitchSprites()
        # If the character chose is CandyMan
        elif character == CharacterEnum.CANDYMAN:
            self.initCandyManSprites()
        # If the character chose is Sonata
        elif character == CharacterEnum.SONATA:
            self.initSonataSprites()
        # If the character chose is Latch
        elif character == CharacterEnum.LATCH:
            self.initLatchSprites()
        # If the character chose is Dice
        elif character == CharacterEnum.DICE:
            self.initDiceSprites()

    # function that init Raptor sprites
    def initRaptorSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Raptor/Default/Raptor_Default.png")]
        for i in range(len(self.defaultRight)):
            self.defaultRight[i] = pygame.transform.scale(self.defaultRight[i], (self.size, self.size))
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Raptor/Running/Raptor_18.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_19.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_20.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_21.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_22.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_23.png")]
        for i in range(len(self.runningRight)):
            self.runningRight[i] = pygame.transform.scale(self.runningRight[i], (self.size, self.size))
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Raptor/Jumping/Raptor_04.png")]
        for i in range(len(self.jumpingRight)):
            self.jumpingRight[i] = pygame.transform.scale(self.jumpingRight[i], (self.size, self.size))
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Raptor/Falling/Raptor_05.png")]
        for i in range(len(self.fallingRight)):
            self.fallingRight[i] = pygame.transform.scale(self.fallingRight[i], (self.size, self.size))
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Raptor/AttackingTop/Raptor_12.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_13.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_14.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_15.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_16.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_17.png")]
        for i in range(len(self.attackingTopRight)):
            self.attackingTopRight[i] = pygame.transform.scale(self.attackingTopRight[i], (self.size, self.size))
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_06.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_07.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_08.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_09.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_10.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_11.png")]
        for i in range(len(self.attackingMiddleRight)):
            self.attackingMiddleRight[i] = pygame.transform.scale(self.attackingMiddleRight[i], (self.size, self.size))
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_25.png"),
                                     pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_26.png"),
                                     pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_27.png"),
                                     pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_28.png")]
        for i in range(len(self.attackingBottomRight)):
            self.attackingBottomRight[i] = pygame.transform.scale(self.attackingBottomRight[i], (self.size, self.size))
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Attacking Above sprites
        self.attackingAboveRight = [pygame.image.load("data/images/Raptor/AttackingAbove/Raptor_29.png"),
                                    pygame.image.load("data/images/Raptor/AttackingAbove/Raptor_30.png")]
        for i in range(len(self.attackingAboveRight)):
            self.attackingAboveRight[i] = pygame.transform.scale(self.attackingAboveRight[i], (self.size, self.size))
        self.attackingAboveLeft = self.mirrorSprites(self.attackingAboveRight)

        # Attacking Below sprites
        self.attackingBelowRight = [pygame.image.load("data/images/Raptor/AttackingBelow/Raptor_29.png"),
                                    pygame.image.load("data/images/Raptor/AttackingBelow/Raptor_30.png")]
        for i in range(len(self.attackingBelowRight)):
            self.attackingBelowRight[i] = pygame.transform.scale(self.attackingBelowRight[i], (self.size, self.size))
        self.attackingBelowLeft = self.mirrorSprites(self.attackingBelowRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Raptor/Victory/Raptor_37.png"),
                             pygame.image.load("data/images/Raptor/Victory/Raptor_38.png"),
                             pygame.image.load("data/images/Raptor/Victory/Raptor_39.png"),
                             pygame.image.load("data/images/Raptor/Victory/Raptor_40.png")]
        for i in range(len(self.victoryRight)):
            self.victoryRight[i] = pygame.transform.scale(self.victoryRight[i], (self.size, self.size))
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Raptor/Hitted/Raptor_24.png")]
        for i in range(len(self.hittedRight)):
            self.hittedRight[i] = pygame.transform.scale(self.hittedRight[i], (self.size, self.size))
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    # function that init Switch sprites
    def initSwitchSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Switch/Default/Switch_Default.png")]
        for i in range(len(self.defaultRight)):
            self.defaultRight[i] = pygame.transform.scale(self.defaultRight[i], (self.size, self.size))
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Switch/Running/Switch_18.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_19.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_20.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_21.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_22.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_23.png")]
        for i in range(len(self.runningRight)):
            self.runningRight[i] = pygame.transform.scale(self.runningRight[i], (self.size, self.size))
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Switch/Jumping/Switch_04.png")]
        for i in range(len(self.jumpingRight)):
            self.jumpingRight[i] = pygame.transform.scale(self.jumpingRight[i], (self.size, self.size))
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Switch/Falling/Switch_05.png")]
        for i in range(len(self.fallingRight)):
            self.fallingRight[i] = pygame.transform.scale(self.fallingRight[i], (self.size, self.size))
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Switch/AttackingTop/Switch_12.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_13.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_14.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_15.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_16.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_17.png")]
        for i in range(len(self.attackingTopRight)):
            self.attackingTopRight[i] = pygame.transform.scale(self.attackingTopRight[i], (self.size, self.size))
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Switch/AttackingMiddle/Switch_07.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_08.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_09.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_10.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_11.png")]
        for i in range(len(self.attackingMiddleRight)):
            self.attackingMiddleRight[i] = pygame.transform.scale(self.attackingMiddleRight[i], (self.size, self.size))
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/Switch/AttackingBottom/Switch_35.png"),
                                     pygame.image.load("data/images/Switch/AttackingBottom/Switch_36.png"),
                                     pygame.image.load("data/images/Switch/AttackingBottom/Switch_37.png"),
                                     pygame.image.load("data/images/Switch/AttackingBottom/Switch_38.png")]
        for i in range(len(self.attackingBottomRight)):
            self.attackingBottomRight[i] = pygame.transform.scale(self.attackingBottomRight[i], (self.size, self.size))
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Attacking Above sprites
        self.attackingAboveRight = [pygame.image.load("data/images/Switch/AttackingAbove/Switch_31.png"),
                                    pygame.image.load("data/images/Switch/AttackingAbove/Switch_32.png"),
                                    pygame.image.load("data/images/Switch/AttackingAbove/Switch_33.png"),
                                    pygame.image.load("data/images/Switch/AttackingAbove/Switch_34.png")]
        for i in range(len(self.attackingAboveRight)):
            self.attackingAboveRight[i] = pygame.transform.scale(self.attackingAboveRight[i], (self.size, self.size))
        self.attackingAboveLeft = self.mirrorSprites(self.attackingAboveRight)

        # Attacking Below sprites
        self.attackingBelowRight = [pygame.image.load("data/images/Switch/AttackingBelow/Switch_25.png"),
                                    pygame.image.load("data/images/Switch/AttackingBelow/Switch_26.png"),
                                    pygame.image.load("data/images/Switch/AttackingBelow/Switch_27.png"),
                                    pygame.image.load("data/images/Switch/AttackingBelow/Switch_28.png")]
        for i in range(len(self.attackingBelowRight)):
            self.attackingBelowRight[i] = pygame.transform.scale(self.attackingBelowRight[i], (self.size, self.size))
        self.attackingBelowLeft = self.mirrorSprites(self.attackingBelowRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Switch/Victory/Switch_42.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_43.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_44.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_45.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_46.png")]
        for i in range(len(self.victoryRight)):
            self.victoryRight[i] = pygame.transform.scale(self.victoryRight[i], (self.size, self.size))
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Switch/Hitted/Switch_24.png")]
        for i in range(len(self.hittedRight)):
            self.hittedRight[i] = pygame.transform.scale(self.hittedRight[i], (self.size, self.size))
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    # function that init CandyMan sprites
    def initCandyManSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/CandyMan/Default/CandyMan_Default.png")]
        for i in range(len(self.defaultRight)):
            self.defaultRight[i] = pygame.transform.scale(self.defaultRight[i], (self.size, self.size))
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/CandyMan/Running/CandyMan_19.png"),
                             pygame.image.load("data/images/CandyMan/Running/CandyMan_20.png")]
        for i in range(len(self.runningRight)):
            self.runningRight[i] = pygame.transform.scale(self.runningRight[i], (self.size, self.size))
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/CandyMan/Jumping/CandyMan_04.png")]
        for i in range(len(self.jumpingRight)):
            self.jumpingRight[i] = pygame.transform.scale(self.jumpingRight[i], (self.size, self.size))
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/CandyMan/Falling/CandyMan_05.png")]
        for i in range(len(self.fallingRight)):
            self.fallingRight[i] = pygame.transform.scale(self.fallingRight[i], (self.size, self.size))
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_12.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_13.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_14.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_15.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_16.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_17.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_18.png")]
        for i in range(len(self.attackingTopRight)):
            self.attackingTopRight[i] = pygame.transform.scale(self.attackingTopRight[i], (self.size, self.size))
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_06.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_07.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_08.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_09.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_10.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_11.png")]
        for i in range(len(self.attackingMiddleRight)):
            self.attackingMiddleRight[i] = pygame.transform.scale(self.attackingMiddleRight[i], (self.size, self.size))
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/CandyMan/AttackingBottom/CandyMan_25.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingBottom/CandyMan_25.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingBottom/CandyMan_26.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingBottom/CandyMan_26.png")]
        for i in range(len(self.attackingBottomRight)):
            self.attackingBottomRight[i] = pygame.transform.scale(self.attackingBottomRight[i], (self.size, self.size))
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Attacking Above sprites
        self.attackingAboveRight = []
        for i in range(len(self.attackingTopRight)):
            self.attackingAboveRight.append(pygame.transform.rotate(self.attackingTopRight[i], 90))
        for i in range(len(self.attackingAboveRight)):
            self.attackingAboveRight[i] = pygame.transform.scale(self.attackingAboveRight[i],
                                                                 (self.size, self.size))
        self.attackingAboveLeft = self.mirrorSprites(self.attackingAboveRight)

        # Attacking Below sprites
        self.attackingBelowRight = []
        for i in range(len(self.attackingTopRight)):
            self.attackingBelowRight.append(pygame.transform.rotate(self.attackingTopRight[i], -90))
        for i in range(len(self.attackingBelowRight)):
            self.attackingBelowRight[i] = pygame.transform.scale(self.attackingBelowRight[i],
                                                                 (self.size, self.size))
        self.attackingBelowLeft = self.mirrorSprites(self.attackingBelowRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/CandyMan/Victory/CandyMan_31.png"),
                             pygame.image.load("data/images/CandyMan/Victory/CandyMan_32.png"),
                             pygame.image.load("data/images/CandyMan/Victory/CandyMan_33.png"),
                             pygame.image.load("data/images/CandyMan/Victory/CandyMan_34.png")]
        for i in range(len(self.victoryRight)):
            self.victoryRight[i] = pygame.transform.scale(self.victoryRight[i], (self.size, self.size))
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/CandyMan/Hitted/CandyMan_29.png")]
        for i in range(len(self.hittedRight)):
            self.hittedRight[i] = pygame.transform.scale(self.hittedRight[i], (self.size, self.size))
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    # function that init Sonata sprites
    def initSonataSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Sonata/Default/Sonata_Default.png")]
        for i in range(len(self.defaultRight)):
            self.defaultRight[i] = pygame.transform.scale(self.defaultRight[i], (self.size, self.size))
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Sonata/Running/Sonata_18.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_19.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_20.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_21.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_22.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_23.png")]
        for i in range(len(self.runningRight)):
            self.runningRight[i] = pygame.transform.scale(self.runningRight[i], (self.size, self.size))
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Sonata/Jumping/Sonata_04.png")]
        for i in range(len(self.jumpingRight)):
            self.jumpingRight[i] = pygame.transform.scale(self.jumpingRight[i], (self.size, self.size))
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Sonata/Falling/Sonata_05.png")]
        for i in range(len(self.fallingRight)):
            self.fallingRight[i] = pygame.transform.scale(self.fallingRight[i], (self.size, self.size))
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Sonata/AttackingTop/Sonata_27.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_28.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_29.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_30.png")]
        for i in range(len(self.attackingTopRight)):
            self.attackingTopRight[i] = pygame.transform.scale(self.attackingTopRight[i], (self.size, self.size))
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_06.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_07.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_08.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_09.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_10.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_11.png")]
        for i in range(len(self.attackingMiddleRight)):
            self.attackingMiddleRight[i] = pygame.transform.scale(self.attackingMiddleRight[i], (self.size, self.size))
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/Sonata/AttackingBottom/Sonata_27.png"),
                                     pygame.image.load("data/images/Sonata/AttackingBottom/Sonata_28.png"),
                                     pygame.image.load("data/images/Sonata/AttackingBottom/Sonata_29.png"),
                                     pygame.image.load("data/images/Sonata/AttackingBottom/Sonata_30.png")]
        for i in range(len(self.attackingBottomRight)):
            self.attackingBottomRight[i] = pygame.transform.scale(self.attackingBottomRight[i], (self.size, self.size))
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Attacking Above sprites
        self.attackingAboveRight = [pygame.image.load("data/images/Sonata/AttackingAbove/Sonata_12.png"),
                                    pygame.image.load("data/images/Sonata/AttackingAbove/Sonata_13.png"),
                                    pygame.image.load("data/images/Sonata/AttackingAbove/Sonata_14.png"),
                                    pygame.image.load("data/images/Sonata/AttackingAbove/Sonata_15.png"),
                                    pygame.image.load("data/images/Sonata/AttackingAbove/Sonata_16.png"),
                                    pygame.image.load("data/images/Sonata/AttackingAbove/Sonata_17.png")]
        for i in range(len(self.attackingAboveRight)):
            self.attackingAboveRight.append(pygame.transform.rotate(self.attackingAboveRight[i], 90))
            self.attackingAboveRight[i] = pygame.transform.scale(self.attackingAboveRight[i], (self.size, self.size))
        self.attackingAboveLeft = self.mirrorSprites(self.attackingAboveRight)

        # Attacking Below sprites
        self.attackingBelowRight = []
        for i in range(len(self.attackingAboveRight)):
            self.attackingBelowRight.append(pygame.transform.rotate(self.attackingAboveRight[i], -180))
            self.attackingBelowRight[i] = pygame.transform.scale(self.attackingBelowRight[i], (self.size, self.size))
        self.attackingBelowLeft = self.mirrorSprites(self.attackingBelowRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Sonata/Victory/Sonata_37.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_38.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_39.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_40.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_41.png")]
        for i in range(len(self.victoryRight)):
            self.victoryRight[i] = pygame.transform.scale(self.victoryRight[i], (self.size, self.size))
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Sonata/Hitted/Sonata_24.png")]
        for i in range(len(self.hittedRight)):
            self.hittedRight[i] = pygame.transform.scale(self.hittedRight[i], (self.size, self.size))
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    # function that init Latch sprites
    def initLatchSprites(self):
        # Default sprite
        self.defaultRight = [pygame.transform.scale(pygame.image.load("data/images/Latch/Default/Latch_Default.png"),
                                                    (self.size, self.size))]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [
            pygame.transform.scale(pygame.image.load("data/images/Latch/Running/Latch_18.png"), (self.size,
                                                                                                 self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/Running/Latch_19.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/Running/Latch_20.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/Running/Latch_21.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/Running/Latch_22.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/Running/Latch_23.png"), (
                self.size, self.size))]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.transform.scale(pygame.image.load("data/images/Latch/Jumping/Latch_04.png"), (
            self.size, self.size))]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.transform.scale(pygame.image.load("data/images/Latch/Falling/Latch_05.png"), (
            self.size, self.size))]
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingTop/Latch_12.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingTop/Latch_13.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingTop/Latch_14.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingTop/Latch_15.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingTop/Latch_16.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingTop/Latch_17.png"), (
                self.size, self.size))]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingMiddle/Latch_07.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingMiddle/Latch_08.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingMiddle/Latch_09.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingMiddle/Latch_10.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingMiddle/Latch_11.png"), (
                self.size, self.size))]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingBottom/Latch_41.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingBottom/Latch_42.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingBottom/Latch_43.png"), (
                self.size, self.size)),
            pygame.transform.scale(pygame.image.load("data/images/Latch/AttackingBottom/Latch_44.png"), (
                self.size, self.size))]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Attacking Above sprites
        self.attackingAboveRight = []
        for i in range(len(self.attackingTopRight)):
            self.attackingAboveRight.append(pygame.transform.rotate(self.attackingTopRight[i], 90))
        self.attackingAboveLeft = self.mirrorSprites(self.attackingAboveRight)

        # Attacking Below sprites
        self.attackingBelowRight = []
        for i in range(len(self.attackingTopRight)):
            self.attackingBelowRight.append(pygame.transform.rotate(self.attackingTopRight[i], -90))
        self.attackingBelowLeft = self.mirrorSprites(self.attackingBelowRight)

        # Victory sprites
        self.victoryRight = [pygame.transform.scale(pygame.image.load("data/images/Latch/Victory/Latch_50.png"), (
            self.size, self.size)),
                             pygame.transform.scale(pygame.image.load("data/images/Latch/Victory/Latch_51.png"), (
                                 self.size, self.size)),
                             pygame.transform.scale(pygame.image.load("data/images/Latch/Victory/Latch_52.png"), (
                                 self.size, self.size)),
                             pygame.transform.scale(pygame.image.load("data/images/Latch/Victory/Latch_53.png"), (
                                 self.size, self.size))]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.transform.scale(pygame.image.load("data/images/Latch/Hitted/Latch_24.png"), (
            self.size, self.size))]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    # function that init Dice sprites
    def initDiceSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Dice/Default/Dice_Default.png")]
        self.defaultRight = self.sizeSprites(self.defaultRight, self.size)
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Dice/Running/Dice_18.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_19.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_20.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_21.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_22.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_23.png")]
        for i in range(len(self.runningRight)):
            self.runningRight[i] = pygame.transform.scale(self.runningRight[i], (self.size, self.size))
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Dice/Jumping/Dice_04.png")]
        for i in range(len(self.jumpingRight)):
            self.jumpingRight[i] = pygame.transform.scale(self.jumpingRight[i], (self.size, self.size))
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Dice/Falling/Dice_05.png")]
        for i in range(len(self.fallingRight)):
            self.fallingRight[i] = pygame.transform.scale(self.fallingRight[i], (self.size, self.size))
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Dice/AttackingTop/Dice_12.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_13.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_14.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_15.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_16.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_17.png")]
        for i in range(len(self.attackingTopRight)):
            self.attackingTopRight[i] = pygame.transform.scale(self.attackingTopRight[i], (self.size, self.size))
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Dice/AttackingMiddle/Dice_06.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_07.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_08.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_09.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_10.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_11.png")]
        self.attackingMiddleRight = self.sizeSprites(self.attackingMiddleRight, self.size)
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = self.rotateSprites(self.attackingTopLeft, 180)
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Attacking Above sprites
        self.attackingAboveRight = self.rotateSprites(self.attackingTopRight, 90)
        self.attackingAboveRight = self.sizeSprites(self.attackingAboveRight, self.size)
        self.attackingAboveLeft = self.mirrorSprites(self.attackingAboveRight)

        # Attacking Below sprites
        self.attackingBelowRight = self.rotateSprites(self.attackingTopRight, -90)
        self.attackingBelowRight = self.sizeSprites(self.attackingBelowRight, self.size)
        self.attackingBelowLeft = self.mirrorSprites(self.attackingBelowRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Dice/Victory/Dice_32.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_33.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_34.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_35.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_36.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_37.png")]
        for i in range(len(self.victoryRight)):
            self.victoryRight[i] = pygame.transform.scale(self.victoryRight[i], (self.size, self.size))
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Dice/Hitted/Dice_24.png")]
        for i in range(len(self.hittedRight)):
            self.hittedRight[i] = pygame.transform.scale(self.hittedRight[i], (self.size, self.size))
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    @staticmethod
    def mirrorSprites(listOfSprites):
        listOfSpritesMirrored = []
        for i in range(len(listOfSprites)):
            listOfSpritesMirrored.append(pygame.transform.flip(listOfSprites[i], True, False))
        return listOfSpritesMirrored

    @staticmethod
    def rotateSprites(listOfSprites, angle):
        listOfSpritesRotated = []
        for i in range(len(listOfSprites)):
            listOfSpritesRotated.append(pygame.transform.rotate(listOfSprites[i], angle))
        return listOfSpritesRotated

    @staticmethod
    def sizeSprites(listOfSprites, size):
        listOfSpritesSized = []
        for i in range(len(listOfSprites)):
            listOfSpritesSized.append(pygame.transform.scale(listOfSprites[i], (size, size)))
        return listOfSpritesSized
