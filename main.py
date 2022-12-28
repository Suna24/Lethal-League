import pygame
import math
from data.player import Player
from data.particle import Particle
from data.characterenum import CharacterEnum
from data.sprite import Sprite
from data.score import Score
from data.direction import Direction
from data.chooseElement import ChooseElement
from data.gameManager import GameManager

# Consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lethal League")
clock = pygame.time.Clock()

# Game Manager to store which characters and which map is selected
gameManager = GameManager()

# Background images
listOfMapBackgrounds = [
        pygame.image.load("data/images/Maps/map1.png"),
        pygame.image.load("data/images/Maps/map2.png"),
        pygame.image.load("data/images/Maps/map3.png"),
        pygame.image.load("data/images/Maps/map4.png"),
        pygame.image.load("data/images/Maps/map5.png"),
        pygame.image.load("data/images/Maps/map6.png"),
        pygame.image.load("data/images/Maps/map7.png"),
        pygame.image.load("data/images/Maps/map8.png")]

welcome_background = pygame.image.load("data/images/welcome_background.jpg")
welcome_background_scaled = pygame.transform.scale(welcome_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Players sprites
listOfCharacters = [CharacterEnum.RAPTOR, CharacterEnum.LATCH, CharacterEnum.DICE, CharacterEnum.SONATA,
                    CharacterEnum.CANDYMAN, CharacterEnum.SWITCH]
listOfSprites = [Sprite(CharacterEnum.RAPTOR), Sprite(CharacterEnum.LATCH),
                 Sprite(CharacterEnum.DICE), Sprite(CharacterEnum.SONATA),
                 Sprite(CharacterEnum.CANDYMAN), Sprite(CharacterEnum.SWITCH)]


def gameLoop():
    print(gameManager.map)
    gravity = (math.pi, 0.0003)
    run = True

    player = Player(100, 100, (0, 0, 255), pygame.Rect(0, 0, 300, 30), pygame.Rect(0, 30, 300, 10),
                    listOfCharacters[gameManager.firstCharacter], Direction.RIGHT, listOfSprites)
    player2 = Player(700, 100, (255, 0, 0), pygame.Rect(screen.get_width() - 300, 0, 300, 30),
                     pygame.Rect(screen.get_width() - 300, 30, 300, 10), listOfCharacters[gameManager.secondCharacter], Direction.LEFT,
                     listOfSprites)
    # Map
    map_background_scaled = pygame.transform.scale(listOfMapBackgrounds[gameManager.map], (SCREEN_WIDTH, SCREEN_HEIGHT))
    score = Score()
    particle = Particle(400, 100, 10, screen)
    player.mapControls(pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_c)
    player2.mapControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL, pygame.K_RSHIFT,
                        pygame.K_n)
    players = [player, player2]
    resetPositions(players, particle)
    
    while run:
        ms_frame = clock.tick(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(map_background_scaled, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, SCREEN_HEIGHT - 30, SCREEN_WIDTH, 30))
        for player in players:
            player.draw(screen)
            player.move(screen, ms_frame)
        particle.move(gravity, ms_frame)
        particle.bounce(players)
        score.draw(screen)
        particle.display(screen)
        pygame.display.update()
        if players[0].character.health <= 0:
            score.addScore(2)
            score.displayActualScore(screen)
            pygame.display.update()
            pygame.time.wait(1000)
            resetPositions(players, particle)

        elif players[1].character.health <= 0:
            score.addScore(1)
            score.displayActualScore(screen)
            pygame.display.update()
            pygame.time.wait(1000)
            resetPositions(players, particle)

        if score.oneWon() is True:
            run = False
            score.displayFinalScore(screen)
            pygame.display.update()
            pygame.time.wait(5000)


def resetPositions(players, ball):
    for player in players:
        player.resetPosition()
        player.character.resetUltimate()
    ball.resetPosition()


# Function that displays the first screen of the game
def welcomeScreen():
    # Fonts
    font = pygame.font.SysFont("rubik", 35)
    text = font.render('PRESS ANY KEY TO CONTINUE', True, [255, 255, 255])
    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)
    # Boolean useful
    run = True
    textDisplayed = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                chooseCharacterScreen()
            if event.type == blink:
                textDisplayed = not textDisplayed

        # Background
        screen.blit(welcome_background_scaled, (0, 0))
        # Blinking text
        if textDisplayed is True:
            screen.blit(text, (150, 20))
        pygame.display.update()

    pygame.quit()


def chooseMapScreen():
    print("In choose map screen")

    chooseElement = ChooseElement(screen, listOfMapBackgrounds, 2, 4)

    for i in range(len(listOfMapBackgrounds)):
        listOfMapBackgrounds[i] = pygame.transform.scale(listOfMapBackgrounds[i], (
            listOfMapBackgrounds[i].get_size()[0] / 4, listOfMapBackgrounds[i].get_size()[1] / 4))

    run = True

    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)
    blinking = True
    hasChoosen = False
    index = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == blink:
                blinking = not blinking
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_s or key == pygame.K_d or key == pygame.K_z:
                    index = chooseElement.changeIndex(index, key)
                if key == pygame.K_SPACE:
                    hasChoosen = not hasChoosen
                if key == pygame.K_RETURN:
                    if hasChoosen is True:
                        gameManager.map = index
                        gameLoop()

        screen.fill([0, 0, 0])

        chooseElement.fillRectangleWithBackgrounds(screen)

        if blinking is True:
            if not hasChoosen:
                chooseElement.drawBorderOfRectangleChoice(screen, index, (0, 0, 255))

        if hasChoosen:
            chooseElement.drawBorderOfRectangleChoice(screen, index, (0, 0, 255))

        pygame.display.update()
    pygame.quit()


# Function that enables players to choose their characters
def chooseCharacterScreen():
    print("In choose Character Screen")
    # Load images
    listOfCharacterBg = [
        pygame.image.load("data/images/CharacterSelection/Raptor.png"),
        pygame.image.load("data/images/CharacterSelection/Latch.png"),
        pygame.image.load("data/images/CharacterSelection/Dice.png"),
        pygame.image.load("data/images/CharacterSelection/Sonata.png"),
        pygame.image.load("data/images/CharacterSelection/CandyMan.png"),
        pygame.image.load("data/images/CharacterSelection/Switch.png")]

    chooseElement = ChooseElement(screen, listOfCharacterBg, 3, 2)

    for i in range(len(listOfCharacterBg)):
        listOfCharacterBg[i] = pygame.transform.scale(listOfCharacterBg[i], (
            listOfCharacterBg[i].get_size()[0] / 4, listOfCharacterBg[i].get_size()[1] / 4))

    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)

    run = True
    blinking = True
    hasChoosen1 = False
    hasChoosen2 = False
    index1 = 0
    index2 = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == blink:
                blinking = not blinking
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_s or key == pygame.K_d or key == pygame.K_z:
                    index1 = chooseElement.changeIndex(index1, key)
                if key == pygame.K_UP or key == pygame.K_DOWN or key == pygame.K_LEFT or key == pygame.K_RIGHT:
                    index2 = chooseElement.changeIndex(index2, key)
                if key == pygame.K_SPACE:
                    hasChoosen1 = not hasChoosen1
                if key == pygame.K_RCTRL:
                    hasChoosen2 = not hasChoosen2
                if key == pygame.K_RETURN:
                    if hasChoosen1 is True and hasChoosen2 is True:
                        gameManager.firstCharacter = index1
                        gameManager.secondCharacter = index2
                        chooseMapScreen()

        screen.fill([0, 0, 0])

        chooseElement.fillRectangleWithBackgrounds(screen)

        if blinking is True:
            if not hasChoosen2:
                chooseElement.drawBorderOfRectangleChoice(screen, index2, (255, 0, 0))

            if not hasChoosen1:
                chooseElement.drawBorderOfRectangleChoice(screen, index1, (0, 0, 255))

        if hasChoosen1:
            chooseElement.drawBorderOfRectangleChoice(screen, index1, (0, 0, 255))

        if hasChoosen2:
            chooseElement.drawBorderOfRectangleChoice(screen, index2, (255, 0, 0))

        pygame.display.update()
    pygame.quit()


# Launch the game
welcomeScreen()
