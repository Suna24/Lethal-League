import pygame


# class Score is used to display the score of the players
# and to count the score
class Score:
    # Constructor
    # initing all scores to 0
    # and display rectangles for the scores
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.rect1color = (255, 255, 255)
        self.rect2color = (255, 255, 255)
        self.rect3color = (255, 255, 255)
        self.hasBeenCalled = False

    # display the score of the players
    # with rectangles at the top of the screen
    def draw(self, screen, width):
        # searching which case we are in
        # displaying rectangles with the right color
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
        # drawing the rectangles
        rect1 = pygame.Rect(width / 2 - 100 - 65, 0, 100, 60)
        rect2 = pygame.Rect(width / 2 - 50, 0, 100, 60)
        rect3 = pygame.Rect(width / 2 + 65, 0, 100, 60)
        pygame.draw.rect(screen, self.rect1color, rect1)
        pygame.draw.rect(screen, self.rect2color, rect2)
        pygame.draw.rect(screen, self.rect3color, rect3)

    # count the score
    def addScore(self, param):
        if param == 1:
            self.score_p1 += 1
        elif param == 2:
            self.score_p2 += 1

    # display the actual score after a round at the middle of the screen
    def displayActualScore(self, screen, width, height):
        font = pygame.font.SysFont("rubik", 150)
        text = font.render(str(self.score_p1) + " - " + str(self.score_p2), True, [255, 255, 255])
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, height / 2 - 100, width, 100))
        screen.blit(text, (width / 2 - 100, height / 2 - 100))

    # function to check if the game is over and who is the winner
    def oneWon(self):
        if self.score_p1 == 2 or self.score_p2 == 2:
            return True
        else:
            return False

    # function to display the winner at the middle of the screen
    def displayFinalScore(self, screen):
        font = pygame.font.SysFont("rubik", 150)
        text = font.render(str(self.score_p1) + " - " + str(self.score_p2), True, [255, 255, 255])
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 200, 800, 100))
        screen.blit(text, (350, 200))
