from data.character import character
import pygame


class Latch(character):
    def __init__(self, sprites):
        character.__init__(self, 3, 100, 0, 0, 0, 0, 0, 0, sprites,25, 15)
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
        self.attackMiddleDownRectDefault = pygame.Rect(0, 0, 0, 0)
        self.aMDRxoffsetRight = 0
        self.aMDRyoffsetRight = 0
        self.aMDRxoffsetLeft = 0
        self.aMDRyoffsetLeft = 0
        self.attackMiddleRectDefault = pygame.Rect(0, 0, 0, 0)
        self.aMRxoffsetRight = 0
        self.aMRyoffsetRight = 0
        self.aMRxoffsetLeft = 0
        self.aMRyoffsetLeft = 0
        self.hitbox = pygame.Rect(0, 0, 50, 87)
        self.attackUpRect = pygame.Rect(0, 0, 0, 0)
        self.attackDownRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleUpRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleDownRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleRect = pygame.Rect(0, 0, 0, 0)
