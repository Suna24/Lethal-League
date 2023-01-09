import pygame

# This class is used to display some rectangles choices like
# when users choose their characters or the map on which the want to play


class ChooseElement:

    # width and height are screen's ones
    def __init__(self, screen, listOfBackgrounds, rows, columns, width, height):
        self.screen = screen
        self.rows = rows
        self.columns = columns
        self.listOfBackgrounds = listOfBackgrounds
        self.allChoices = []

        if rows * columns != len(listOfBackgrounds):
            print("WARNING : the number of choices does not correspond to the number of background passed in parameters")

        # Initialize allChoices
        self.initIndexOfChoices()

        # Create all rectangle choices
        self.listOfRectangleChoices = self.makeRectangleChoices(width, height)

    # function used to initialize all index of choose element component
    def initIndexOfChoices(self):
        # Initialization by filling 0 in all "boxes"
        self.allChoices = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        index = 0

        # fill the "boxes" by their correspondant index like the example below
        #  ______________________________
        # |    0    |    1    |    2    |
        #  ______________________________
        # |    3    |    4    |    5    |
        #  ______________________________

        for i in range(self.rows):
            for j in range(self.columns):
                self.allChoices[i][j] = index
                index += 1

    # function used to get the couple of index (like in a 2D Array) on which we are (identified by the index)
    def getCoupleOfIndex(self, value):
        x, y = 0, 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.allChoices[i][j] == value:
                    x = i
                    y = j
        return [x, y]

    # function used to change the index of the player (when he wants to move on a choos screen)
    def changeIndex(self, currentIndex, key):

        # we get the couple of index used to know on which index we currently are
        [x, y] = self.getCoupleOfIndex(currentIndex)

        # if the player go on the top
        if key == pygame.K_z or key == pygame.K_KP8:
            # if we are on the top row, then the next choice is on the last row
            if currentIndex in self.allChoices[0]:
                return self.allChoices[self.rows - 1][y]
            # else simply go on the choice just above
            else:
                return self.allChoices[x - 1][y]

        # if the player go below
        if key == pygame.K_s or key == pygame.K_KP5:
            # if we are on the last row, then the next choice is on the top row
            if currentIndex in self.allChoices[self.rows - 1]:
                return self.allChoices[0][y]
            # else simply go on the choice just below
            else:
                return self.allChoices[x + 1][y]

        # if the player go on the left
        if key == pygame.K_q or key == pygame.K_KP4:
            # we memorize all index that are situated on the first column
            indexToRemember = []
            for i in range(0, self.rows):
                indexToRemember.append(i * self.columns)
            # if we are on the first column, then the next choice is on the last column
            if currentIndex in indexToRemember:
                return self.allChoices[x][self.columns - 1]
            # else simply got on the left
            else:
                return self.allChoices[x][y - 1]

        # if the player go on right
        if key == pygame.K_d or key == pygame.K_KP6:
            # we memorize all index that are situated on the last column
            indexToRemember = [self.columns - 1]
            for i in range(1, self.rows):
                indexToRemember.append((self.columns - 1) + i * self.columns)
            # if we are on the last column, then the next choice is on the first column
            if currentIndex in indexToRemember:
                return self.allChoices[x][0]
            # else simply got on the right
            else:
                return self.allChoices[x][y + 1]

        return 0

    # this function draw rectangles to fill all screen size
    def makeRectangleChoices(self, screenWidth, screenHeight):

        # variables
        listOfRectangleChoices = []
        x, y = 0, 0

        # initialize indexes to organize rect, we store all index that are on the right of the screen
        # to know when we have to start a new row/line
        indexToRemember = [self.columns - 1]
        for i in range(1, self.rows):
            indexToRemember.append((self.columns - 1) + i * self.columns)

        # we create a rectangle location x,y for each background
        for i in range(len(self.listOfBackgrounds)):
            listOfRectangleChoices.append(
                pygame.Rect(x, y, screenWidth / self.columns, screenHeight / self.rows))

            # if we are at the end of the screen, we have to modify y value to start a new line under
            # the last constructed row, otherwise we just modify x value to add a new column offset
            if i in indexToRemember:
                x = 0
                y += screenHeight / self.rows
            else:
                x += screenWidth / self.columns

        return listOfRectangleChoices

    # function used to bind rectangle choices with their corresponding backgrounds
    def fillRectangleWithBackgrounds(self, screen):
        for i in range(len(self.listOfBackgrounds)):
            # draw a yellow rectangle
            pygame.draw.rect(screen, [255, 255, 0], self.listOfRectangleChoices[i])

            # get the center of the rectangle to place the background correctly
            center = (self.listOfRectangleChoices[i].centerx - self.listOfBackgrounds[i].get_width() / 4,
                      self.listOfRectangleChoices[i].y)

            # get the size of the rectangle to draw a "squared" background
            size = self.listOfRectangleChoices[i].height
            screen.blit(pygame.transform.scale(self.listOfBackgrounds[i], (size, size)), center)

    # function used to draw border on the chose rectangle
    def drawBorderOfRectangleChoice(self, screen, indexOfRectangle, color):
        # get the position of the rectangle by its index
        x, y = self.listOfRectangleChoices[indexOfRectangle].x, self.listOfRectangleChoices[indexOfRectangle].y
        rect_width, rect_height = self.listOfRectangleChoices[indexOfRectangle].width, self.listOfRectangleChoices[
            indexOfRectangle].height
        # draw lines
        pygame.draw.lines(screen, color, True,
                          ((x, y), (x + rect_width, y), (x + rect_width, y + rect_height), (x, y + rect_height)), 5)
