import pygame


class Score:
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.rect1color = (255, 255, 255)
        self.rect2color = (255, 255, 255)
        self.rect3color = (255, 255, 255)
        self.hasBeenCalled = False

    def draw(self, screen, width):
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
        rect1 = pygame.Rect(width / 2 - 100 - 65, 0, 100, 60)
        rect2 = pygame.Rect(width / 2 - 50, 0, 100, 60)
        rect3 = pygame.Rect(width / 2 + 65, 0, 100, 60)
        pygame.draw.rect(screen, self.rect1color, rect1)
        pygame.draw.rect(screen, self.rect2color, rect2)
        pygame.draw.rect(screen, self.rect3color, rect3)

    def addScore(self, param):
        if param == 1:
            self.score_p1 += 1
        elif param == 2:
            self.score_p2 += 1

    def displayActualScore(self, screen, width, height):
        font = pygame.font.SysFont("rubik", 150)
        text = font.render(str(self.score_p1) + " - " + str(self.score_p2), True, [255, 255, 255])
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, height/2 - 100, width, 100))
        screen.blit(text, (width/2 - 100, height/2 - 100))

    def oneWon(self):
        if self.score_p1 == 2 or self.score_p2 == 2:
            return True
        else:
            return False

    def displayFinalScore(self, screen):
        font = pygame.font.SysFont("rubik", 150)
        text = font.render(str(self.score_p1) + " - " + str(self.score_p2), True, [255, 255, 255])
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 200, 800, 100))
        screen.blit(text, (350, 200))
