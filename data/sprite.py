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
        self.defaultRight = [pygame.image.load("data/images/Raptor/Default/Raptor_Default.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Raptor/Running/Raptor_18.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_19.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_20.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_21.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_22.png"),
                             pygame.image.load("data/images/Raptor/Running/Raptor_23.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Raptor/Jumping/Raptor_04.png")]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Raptor/Falling/Raptor_05.png")]
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Raptor/AttackingTop/Raptor_12.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_13.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_14.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_15.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_16.png"),
                                  pygame.image.load("data/images/Raptor/AttackingTop/Raptor_17.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_06.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_07.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_08.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_09.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_10.png"),
                                     pygame.image.load("data/images/Raptor/AttackingMiddle/Raptor_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_25.png"),
                                     pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_26.png"),
                                     pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_27.png"),
                                     pygame.image.load("data/images/Raptor/AttackingBottom/Raptor_28.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Raptor/Victory/Raptor_37.png"),
                             pygame.image.load("data/images/Raptor/Victory/Raptor_38.png"),
                             pygame.image.load("data/images/Raptor/Victory/Raptor_39.png"),
                             pygame.image.load("data/images/Raptor/Victory/Raptor_40.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Raptor/Hitted/Raptor_24.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)


    def initSwitchSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Switch/Default/Switch_Default.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Switch/Running/Switch_18.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_19.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_20.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_21.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_22.png"),
                             pygame.image.load("data/images/Switch/Running/Switch_23.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Switch/Jumping/Switch_04.png")]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Switch/Falling/Switch_05.png")]
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Switch/AttackingTop/Switch_12.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_13.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_14.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_15.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_16.png"),
                                  pygame.image.load("data/images/Switch/AttackingTop/Switch_17.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Switch/AttackingMiddle/Switch_07.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_08.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_09.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_10.png"),
                                     pygame.image.load("data/images/Switch/AttackingMiddle/Switch_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/Switch/AttackingBottom/Switch_35.png"),
                                     pygame.image.load("data/images/Switch/AttackingBottom/Switch_36.png"),
                                     pygame.image.load("data/images/Switch/AttackingBottom/Switch_37.png"),
                                     pygame.image.load("data/images/Switch/AttackingBottom/Switch_38.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Switch/Victory/Switch_42.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_43.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_44.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_45.png"),
                             pygame.image.load("data/images/Switch/Victory/Switch_46.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Switch/Hitted/Switch_24.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    def initCandyManSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/CandyMan/Default/CandyMan_Default.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/CandyMan/Running/CandyMan_19.png"),
                             pygame.image.load("data/images/CandyMan/Running/CandyMan_20.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/CandyMan/Jumping/CandyMan_04.png")]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/CandyMan/Falling/CandyMan_05.png")]
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_12.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_13.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_14.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_15.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_16.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_17.png"),
                                  pygame.image.load("data/images/CandyMan/AttackingTop/CandyMan_18.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_06.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_07.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_08.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_09.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_10.png"),
                                     pygame.image.load("data/images/CandyMan/AttackingMiddle/CandyMan_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/CandyMan/Default/CandyMan_Default.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/CandyMan/Victory/CandyMan_31.png"),
                             pygame.image.load("data/images/CandyMan/Victory/CandyMan_32.png"),
                             pygame.image.load("data/images/CandyMan/Victory/CandyMan_33.png"),
                             pygame.image.load("data/images/CandyMan/Victory/CandyMan_34.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/CandyMan/Hitted/CandyMan_29.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)


    def initSonataSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Sonata/Default/Sonata_Default.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Sonata/Running/Sonata_18.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_19.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_20.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_21.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_22.png"),
                             pygame.image.load("data/images/Sonata/Running/Sonata_23.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Sonata/Jumping/Sonata_04.png")]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Sonata/Falling/Sonata_05.png")]
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Sonata/AttackingTop/Sonata_12.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_13.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_14.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_15.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_16.png"),
                                  pygame.image.load("data/images/Sonata/AttackingTop/Sonata_17.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_06.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_07.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_08.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_09.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_10.png"),
                                     pygame.image.load("data/images/Sonata/AttackingMiddle/Sonata_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/Sonata/Default/Sonata_Default.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Sonata/Victory/Sonata_37.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_38.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_39.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_40.png"),
                             pygame.image.load("data/images/Sonata/Victory/Sonata_41.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Sonata/Hitted/Sonata_24.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    def initLatchSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Latch/Default/Latch_Default.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Latch/Running/Latch_18.png"),
                             pygame.image.load("data/images/Latch/Running/Latch_19.png"),
                             pygame.image.load("data/images/Latch/Running/Latch_20.png"),
                             pygame.image.load("data/images/Latch/Running/Latch_21.png"),
                             pygame.image.load("data/images/Latch/Running/Latch_22.png"),
                             pygame.image.load("data/images/Latch/Running/Latch_23.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Latch/Jumping/Latch_04.png")]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Latch/Falling/Latch_05.png")]
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Latch/AttackingTop/Latch_12.png"),
                                  pygame.image.load("data/images/Latch/AttackingTop/Latch_13.png"),
                                  pygame.image.load("data/images/Latch/AttackingTop/Latch_14.png"),
                                  pygame.image.load("data/images/Latch/AttackingTop/Latch_15.png"),
                                  pygame.image.load("data/images/Latch/AttackingTop/Latch_16.png"),
                                  pygame.image.load("data/images/Latch/AttackingTop/Latch_17.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Latch/AttackingMiddle/Latch_07.png"),
                                     pygame.image.load("data/images/Latch/AttackingMiddle/Latch_08.png"),
                                     pygame.image.load("data/images/Latch/AttackingMiddle/Latch_09.png"),
                                     pygame.image.load("data/images/Latch/AttackingMiddle/Latch_10.png"),
                                     pygame.image.load("data/images/Latch/AttackingMiddle/Latch_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        self.attackingBottomRight = [pygame.image.load("data/images/Latch/AttackingBottom/Latch_41.png"),
                                     pygame.image.load("data/images/Latch/AttackingBottom/Latch_42.png"),
                                     pygame.image.load("data/images/Latch/AttackingBottom/Latch_43.png"),
                                     pygame.image.load("data/images/Latch/AttackingBottom/Latch_44.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Latch/Victory/Latch_50.png"),
                             pygame.image.load("data/images/Latch/Victory/Latch_51.png"),
                             pygame.image.load("data/images/Latch/Victory/Latch_52.png"),
                             pygame.image.load("data/images/Latch/Victory/Latch_53.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Latch/Hitted/Latch_24.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    def initDiceSprites(self):
        # Default sprite
        self.defaultRight = [pygame.image.load("data/images/Dice/Default/Dice_Default.png")]
        self.defaultLeft = self.mirrorSprites(self.defaultRight)

        # Running sprites
        self.runningRight = [pygame.image.load("data/images/Dice/Running/Dice_18.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_19.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_20.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_21.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_22.png"),
                             pygame.image.load("data/images/Dice/Running/Dice_23.png")]
        self.runningLeft = self.mirrorSprites(self.runningRight)

        # Jumping sprites
        self.jumpingRight = [pygame.image.load("data/images/Dice/Jumping/Dice_04.png")]
        self.jumpingLeft = self.mirrorSprites(self.jumpingRight)

        # Falling sprites
        self.fallingRight = [pygame.image.load("data/images/Dice/Falling/Dice_05.png")]
        self.fallingLeft = self.mirrorSprites(self.fallingRight)

        # Attacking Top sprites
        self.attackingTopRight = [pygame.image.load("data/images/Dice/AttackingTop/Dice_12.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_13.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_14.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_15.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_16.png"),
                                  pygame.image.load("data/images/Dice/AttackingTop/Dice_17.png")]
        self.attackingTopLeft = self.mirrorSprites(self.attackingTopRight)

        # Attacking Middle sprites
        self.attackingMiddleRight = [pygame.image.load("data/images/Dice/AttackingMiddle/Dice_06.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_07.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_08.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_09.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_10.png"),
                                     pygame.image.load("data/images/Dice/AttackingMiddle/Dice_11.png")]
        self.attackingMiddleLeft = self.mirrorSprites(self.attackingMiddleRight)

        # Attacking Bottom sprites
        # TODO sprite bottom
        self.attackingBottomRight = [pygame.image.load("data/images/Dice/Default/Dice_Default.png")]
        self.attackingBottomLeft = self.mirrorSprites(self.attackingBottomRight)

        # Victory sprites
        self.victoryRight = [pygame.image.load("data/images/Dice/Victory/Dice_32.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_33.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_34.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_35.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_36.png"),
                             pygame.image.load("data/images/Dice/Victory/Dice_37.png")]
        self.victoryLeft = self.mirrorSprites(self.victoryRight)

        # Hitted sprite
        self.hittedRight = [pygame.image.load("data/images/Dice/Hitted/Dice_24.png")]
        self.hittedLeft = self.mirrorSprites(self.hittedRight)

    def mirrorSprites(self, listOfSprites):
        listOfSpritesMirrored = []
        for i in range(len(listOfSprites)):
            listOfSpritesMirrored.append(pygame.transform.flip(listOfSprites[i], True, False))
        return listOfSpritesMirrored
