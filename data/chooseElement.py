import pygame


class ChooseElement:
    def __init__(self, screen, listOfBackgrounds, rows, columns, width, height):
        self.screen = screen
        self.rows = rows
        self.columns = columns
        self.listOfBackgrounds = listOfBackgrounds

        if rows * columns != len(listOfBackgrounds):
            print("ATTENTION : le nombre de choix ne correspond pas au nombre de background passé en paramètres")

        # Initialize allChoices
        self.initIndexOfChoices()

        # Create all rectangle choices
        self.listOfRectangleChoices = self.makeRectangleChoices(width, height)

    def initIndexOfChoices(self):
        self.allChoices = [[0 for i in range(self.columns)] for i in range(self.rows)]
        index = 0
        for i in range(self.rows):
            for j in range(self.columns):
                self.allChoices[i][j] = index
                index += 1

    def getCoupleOfIndex(self, value):
        x, y = 0, 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.allChoices[i][j] == value:
                    x = i
                    y = j
        print("i : " + str(x) + "\t" + "j : " + str(y))
        return [x, y]

    def changeIndex(self, currentIndex, key):
        print("Current Index : " + str(currentIndex))
        print("All choices available : " + str(self.allChoices))

        [x, y] = self.getCoupleOfIndex(currentIndex)

        if key == pygame.K_z or key == pygame.K_UP:
            print("Z pressed")
            if currentIndex in self.allChoices[0]:
                print("New index : " + str(self.allChoices[self.rows - 1][y]))
                return self.allChoices[self.rows - 1][y]
            else:
                print("New index : " + str(self.allChoices[x - 1][y]))
                return self.allChoices[x - 1][y]

        if key == pygame.K_s or key == pygame.K_DOWN:
            print("S pressed")
            if currentIndex in self.allChoices[self.rows - 1]:
                print("New index : " + str(self.allChoices[0][y]))
                return self.allChoices[0][y]
            else:
                print("New index : " + str(self.allChoices[x + 1][y]))
                return self.allChoices[x + 1][y]

        if key == pygame.K_q or key == pygame.K_LEFT:
            print("Q pressed")
            indexToRemember = []
            for i in range(0, self.rows):
                indexToRemember.append(i * self.columns)
            if currentIndex in indexToRemember:
                print("New index (in indexToRemember) : " + str(self.allChoices[x][self.columns - 1]))
                return self.allChoices[x][y + 1]
            else:
                print("New index (not in indexToRemember) : " + str(self.allChoices[x][y - 1]))
                return self.allChoices[x][y - 1]

        if key == pygame.K_d or key == pygame.K_RIGHT:
            print("D pressed")
            indexToRemember = [self.columns - 1]
            for i in range(1, self.rows):
                indexToRemember.append((self.columns - 1) + i * self.columns)
            if currentIndex in indexToRemember:
                print("New index : " + str(self.allChoices[x][0]))
                return self.allChoices[x][0]
            else:
                print("New index : " + str(self.allChoices[x][y + 1]))
                return self.allChoices[x][y + 1]

        return 0

    def makeRectangleChoices(self, screenWidth, screenHeight):
        listOfRectangleChoices = []
        x, y = 0, 0

        # initialize indexes to organize rect
        indexToRemember = [self.columns - 1]
        for i in range(1, self.rows):
            indexToRemember.append((self.columns - 1) + i * self.columns)

        for i in range(len(self.listOfBackgrounds)):
            listOfRectangleChoices.append(
                pygame.Rect(x, y, screenWidth / self.columns, screenHeight / self.rows, width=5))
            if i in indexToRemember:
                x = 0
                y += screenHeight / self.rows
            else:
                x += screenWidth / self.columns

            print(str(x) + " " + str(y))

        return listOfRectangleChoices

    def fillRectangleWithBackgrounds(self, screen):
        for i in range(len(self.listOfBackgrounds)):
            pygame.draw.rect(screen, [255, 255, 0], self.listOfRectangleChoices[i])
            center = (self.listOfRectangleChoices[i].centerx - self.listOfBackgrounds[i].get_width() / 4,
                      self.listOfRectangleChoices[i].y)
            size = self.listOfRectangleChoices[i].height
            screen.blit(pygame.transform.scale(self.listOfBackgrounds[i], (size, size)), center)

    def drawBorderOfRectangleChoice(self, screen, indexOfRectangle, color):
        x, y = self.listOfRectangleChoices[indexOfRectangle].x, self.listOfRectangleChoices[indexOfRectangle].y
        rect_width, rect_height = self.listOfRectangleChoices[indexOfRectangle].width, \
                                  self.listOfRectangleChoices[indexOfRectangle].height
        pygame.draw.lines(screen, color, True,
                          ((x, y), (x + rect_width, y), (x + rect_width, y + rect_height), (x, y + rect_height)), 5)
