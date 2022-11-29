from data.character import character
import pygame

class Sonata(character):
    def __init__(self, sprites):
        character.__init__(self, 3, 100, 2, 0, 0, 0, 0, 0, 0, sprites,25, 15)
        self.attackUpRectDefault = pygame.Rect(0, 0, 70, 20)
        self.aURxoffset = 25
        self.aURyoffset = 15
        self.attackDownRectDefault = pygame.Rect(0, 0, 70, 20)
        self.aDRxoffset = 25
        self.aDRyoffset = 30
        self.attackMiddleUpRectDefault = pygame.Rect(0, 0, 40, 20)
        self.aMURxoffsetRight = -15
        self.aMURyoffsetRight = 0
        self.aMURxoffsetLeft = 45
        self.aMURyoffsetLeft = 0
        self.attackMiddleDownRectDefault = pygame.Rect(0, 0, 50, 20)
        self.aMDRxoffsetRight = -15
        self.aMDRyoffsetRight = 10
        self.aMDRxoffsetLeft = 50
        self.aMDRyoffsetLeft = 10
        self.attackMiddleRectDefault = pygame.Rect(0, 0, 50, 20)
        self.aMRxoffsetRight = -15
        self.aMRyoffsetRight = 0
        self.aMRxoffsetLeft = 50
        self.aMRyoffsetLeft = 0
        self.hitbox = pygame.Rect(0, 0, 40, 100)
        self.attackUpRect = pygame.Rect(0, 0, 0, 0)
        self.attackDownRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleUpRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleDownRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleRect = pygame.Rect(0, 0, 0, 0)


    def deployUltimate(self):
        self.health += 0.5
        print("Ultimate deployed")

    def resetUltimate(self):
        pass