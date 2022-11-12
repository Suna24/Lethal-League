import pygame


class Score:
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.rect1color = (255, 255, 255)
        self.rect2color = (255, 255, 255)
        self.rect3color = (255, 255, 255)

    def draw(self, screen):
        if self.score_p1 == 1 and self.score_p2 == 1:
            self.rect1color = (0, 0, 255)
            self.rect2color = (255, 255, 255)
            self.rect3color = (255, 0, 0)
        elif self.score_p1 == 0 and self.score_p2 == 0:
            self.rect1color = (255, 255, 255)
            self.rect2color = (255, 255, 255)
            self.rect3color = (255, 255, 255)
        elif self.score_p1 == 1 and self.score_p2 == 0:
            self.rect1color = (0, 0, 255)
            self.rect2color = (255, 255, 255)
            self.rect3color = (255, 255, 255)
        elif self.score_p1 == 0 and self.score_p2 == 1:
            self.rect1color = (255, 255, 255)
            self.rect2color = (255, 255, 255)
            self.rect3color = (255, 0, 0)
        elif self.score_p1 == 2 and self.score_p2 == 0:
            self.rect1color = (0, 0, 255)
            self.rect2color = (0, 0, 255)
            self.rect3color = (255, 255, 255)
        elif self.score_p1 == 0 and self.score_p2 == 2:
            self.rect1color = (255, 255, 255)
            self.rect2color = (255, 0, 0)
            self.rect3color = (255, 0, 0)
        elif self.score_p1 == 2 and self.score_p2 == 1:
            self.rect1color = (0, 0, 255)
            self.rect2color = (0, 0, 255)
            self.rect3color = (255, 0, 0)
        elif self.score_p1 == 1 and self.score_p2 == 2:
            self.rect1color = (0, 0, 255)
            self.rect2color = (255, 0, 0)
            self.rect3color = (255, 0, 0)
        rect1 = pygame.Rect(310, 0, 50, 30)
        rect2 = pygame.Rect(440, 0, 50, 30)
        rect3 = pygame.Rect(375, 0, 50, 30)
        pygame.draw.rect(screen, self.rect1color, rect1)
        pygame.draw.rect(screen, self.rect2color, rect2)
        pygame.draw.rect(screen, self.rect3color, rect3)

    def addScore(self, param):
        if param == 1:
            self.score_p1 += 1
        elif param == 2:
            self.score_p2 += 1
