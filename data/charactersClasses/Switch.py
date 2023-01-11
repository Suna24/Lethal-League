from data.character import character
import pygame


# Switch class inherits from character class
# So we init the character class with the specific Switch values
class Switch(character):
    def __init__(self, sprites):
        character.__init__(self, 5, 100, 2, 0, 0, 0, 0, 0, 0, sprites, sprites.size - (25 * 10),
                           sprites.size - (15 * 10))
        self.sprites = sprites
        self.hitbox = pygame.Rect(0, 0, sprites.size * 0.43, sprites.size * 0.73)
        self.attackUpRectDefault = pygame.Rect(0, 0, 70, 20)
        self.attackUpRectDefault = pygame.Rect(0, 0, sprites.size * 0.57, sprites.size * 0.1)
        self.aURxoffset = self.hitbox.width * 0.5
        self.aURyoffset = self.hitbox.height * 0.70
        self.attackDownRectDefault = pygame.Rect(0, 0, sprites.size * 0.57, sprites.size * 0.1)
        self.aDRxoffset = self.hitbox.width * 0.5
        self.aDRyoffset = sprites.size * 0.1
        self.attackMiddleUpRectDefault = pygame.Rect(0, 0, sprites.size * 0.4, sprites.size * 0.1)
        self.aMURxoffsetRight = -self.hitbox.width * 0.5
        self.aMURyoffsetRight = self.hitbox.height * 0.5
        self.aMURxoffsetLeft = self.hitbox.width
        self.aMURyoffsetLeft = self.hitbox.height * 0.5
        self.attackMiddleDownRectDefault = pygame.Rect(0, 0, sprites.size * 0.4, sprites.size * 0.1)
        self.aMDRxoffsetRight = -self.hitbox.width * 0.5
        self.aMDRyoffsetRight = self.hitbox.height * 0.1
        self.aMDRxoffsetLeft = self.hitbox.width
        self.aMDRyoffsetLeft = self.hitbox.height * 0.1
        self.attackMiddleRectDefault = pygame.Rect(0, 0, sprites.size * 0.4, sprites.size * 0.1)
        self.aMRxoffsetRight = -self.hitbox.width * 0.5
        self.aMRyoffsetRight = self.hitbox.height * 0.3
        self.aMRxoffsetLeft = self.hitbox.width
        self.aMRyoffsetLeft = self.hitbox.height * 0.3
        self.attackUpRect = pygame.Rect(0, 0, 0, 0)
        self.attackDownRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleUpRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleDownRect = pygame.Rect(0, 0, 0, 0)
        self.attackMiddleRect = pygame.Rect(0, 0, 0, 0)

    def deployUltimate(self):
        # Switch's ultimate is about growing their smash hitboxes
        self.attackUpRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.57 + 20, self.sprites.size * 0.1 + 20)
        self.attackDownRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.57 + 20, self.sprites.size * 0.1 + 20)
        self.attackMiddleUpRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.4 + 20, self.sprites.size * 0.1 + 20)
        self.attackMiddleDownRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.4 + 20, self.sprites.size * 0.1 + 20)
        self.attackMiddleRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.4 + 20, self.sprites.size * 0.1 + 20)

    def resetUltimate(self):
        # Reverting the hitboxes to their original size
        self.attackUpRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.57, self.sprites.size * 0.1)
        self.attackDownRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.57, self.sprites.size * 0.1)
        self.attackMiddleUpRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.4, self.sprites.size * 0.1)
        self.attackMiddleDownRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.4, self.sprites.size * 0.1)
        self.attackMiddleRectDefault = pygame.Rect(0, 0, self.sprites.size * 0.4, self.sprites.size * 0.1)
