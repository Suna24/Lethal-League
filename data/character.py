# Base code for a character
# creating hitboxes for the character
# like attack or touch hitboxes
# setting also character's attributes (speed, force, etc.)
# creating offsets in order to make the hitboxes corresponding to each character

class character:
    def __init__(self, speed, health, force, hitbox, attackUpRectDefault, attackDownRectDefault,
                 attackMiddleUpRectDefault, attackMiddleDownRectDefault, attackMiddleRectDefault, sprite, xhitboxoffset,
                 yhitboxoffset):
        self.speed = speed  # 3
        self.health = health  # 100
        self.maxHealth = health
        self.hitbox = hitbox  # 0
        self.force = force  # 2
        self.attackUpRectDefault = attackUpRectDefault
        self.aURxoffset = 0
        self.aURyoffset = 0
        self.attackUpRect = self.attackUpRectDefault
        self.attackDownRectDefault = attackDownRectDefault
        self.aDRxoffset = 0
        self.aDRyoffset = 0
        self.attackDownRect = self.attackDownRectDefault
        self.attackMiddleUpRectDefault = attackMiddleUpRectDefault
        self.aMURxoffsetRight = 0
        self.aMURyoffsetRight = 0
        self.aMURxoffsetLeft = 0
        self.aMURyoffsetLeft = 0
        self.attackMiddleUpRect = self.attackMiddleUpRectDefault
        self.attackMiddleDownRectDefault = attackMiddleDownRectDefault
        self.aMDRxoffsetRight = 0
        self.aMDRyoffsetRight = 0
        self.aMDRxoffsetLeft = 0
        self.aMDRyoffsetLeft = 0
        self.attackMiddleDownRect = self.attackMiddleDownRectDefault
        self.attackMiddleRectDefault = attackMiddleRectDefault
        self.aMRxoffsetRight = 0
        self.aMRyoffsetRight = 0
        self.aMRxoffsetLeft = 0
        self.aMRyoffsetLeft = 0
        self.attackMiddleRect = self.attackMiddleRectDefault
        self.sprite = sprite
        self.xhitboxoffset = xhitboxoffset
        self.yhitboxoffset = yhitboxoffset

    def deployUltimate(self):
        # raise Error on mother class
        raise NotImplementedError("Subclass must implement abstract method")

    def resetUltimate(self):
        # raise Error on mother class
        raise NotImplementedError("Subclass must implement abstract method")
