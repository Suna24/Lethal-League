import pygame
import math
from data.player import Player
from data.particle import Particle
from data.characterenum import CharacterEnum
from data.sprite import Sprite
from data.score import Score
from data.direction import Direction

# Consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lethal League")
clock = pygame.time.Clock()

# Background images
game_background = pygame.image.load("data/images/bg.png")
game_background_scaled = pygame.transform.scale(game_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
welcome_background = pygame.image.load("data/images/welcome_background.jpg")
welcome_background_scaled = pygame.transform.scale(welcome_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Players sprites
listOfCharacters = [CharacterEnum.RAPTOR, CharacterEnum.LATCH, CharacterEnum.DICE, CharacterEnum.SONATA,
                    CharacterEnum.CANDYMAN, CharacterEnum.SWITCH]
listOfSprites = [Sprite(CharacterEnum.RAPTOR), Sprite(CharacterEnum.LATCH),
                 Sprite(CharacterEnum.DICE), Sprite(CharacterEnum.SONATA),
                 Sprite(CharacterEnum.CANDYMAN), Sprite(CharacterEnum.SWITCH)]


def gameLoop(ch1, ch2):
    gravity = (math.pi, 0.0003)
    run = True

    player = Player(100, 100, (0, 0, 255), pygame.Rect(0, 0, 300, 30), pygame.Rect(0, 30, 300, 10),
                    listOfCharacters[ch1], Direction.RIGHT, listOfSprites)
    player2 = Player(700, 100, (255, 0, 0), pygame.Rect(screen.get_width() - 300, 0, 300, 30),
                     pygame.Rect(screen.get_width() - 300, 30, 300, 10), listOfCharacters[ch2], Direction.LEFT,
                     listOfSprites)
    score = Score()
    particle = Particle(400, 100, 10, screen)
    player.mapControls(pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_LCTRL)
    player2.mapControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL, pygame.K_RSHIFT,
                        pygame.K_n)
    players = [player, player2]
    resetPositions(players, particle)
    while run:
        ms_frame = clock.tick(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(game_background_scaled, (0, 0))
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
            resetPositions(players, particle)
            score.addScore(2)

        elif players[1].character.health <= 0:
            resetPositions(players, particle)
            score.addScore(1)


def resetPositions(players, ball):
    for player in players:
        player.resetPosition()
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


def changeIndex(index, key):
    print(index)
    if key == pygame.K_z or key == pygame.K_UP:
        print("Z pressed")
        if index == 0 or index == 1:
            return index + 4
        else:
            return index - 2
    if key == pygame.K_s or key == pygame.K_DOWN:
        print("S pressed")
        if index == 4 or index == 5:
            return index - 4
        else:
            return index + 2
    if key == pygame.K_q or key == pygame.K_LEFT:
        print("Q pressed")
        if index == 0 or index == 2 or index == 4:
            return index + 1
        else:
            return index - 1
    if key == pygame.K_d or key == pygame.K_RIGHT:
        print("D pressed")
        if index == 1 or index == 3 or index == 5:
            return index - 1
        else:
            return index + 1

    return 0


def validateCharacter(index1, hasChoosen1, index2, hasChoosen2):
    if hasChoosen1 is True and hasChoosen2 is True:
        gameLoop(index1, index2)


# Function that enables players to choose their characters
def chooseCharacterScreen():
    # Load images
    listOfCharacterBg = [
        pygame.image.load("data/images/CharacterSelection/Raptor.png"),
        pygame.image.load("data/images/CharacterSelection/Latch.png"),
        pygame.image.load("data/images/CharacterSelection/Dice.png"),
        pygame.image.load("data/images/CharacterSelection/Sonata.png"),
        pygame.image.load("data/images/CharacterSelection/CandyMan.png"),
        pygame.image.load("data/images/CharacterSelection/Switch.png")]

    for i in range(len(listOfCharacterBg)):
        listOfCharacterBg[i] = pygame.transform.scale(listOfCharacterBg[i], (
            listOfCharacterBg[i].get_size()[0] / 4, listOfCharacterBg[i].get_size()[1] / 4))

    # Those rectangles will represent characters
    raptorRect = pygame.Rect(30, 20, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    latchRect = pygame.Rect(SCREEN_WIDTH - 30 - SCREEN_WIDTH / 2.5, 20, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    diceRect = pygame.Rect(30, 20 + SCREEN_HEIGHT / 4 + 55, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    sonataRect = pygame.Rect(SCREEN_WIDTH - 30 - SCREEN_WIDTH / 2.5, 20 + SCREEN_HEIGHT / 4 + 55, SCREEN_WIDTH / 2.5,
                             SCREEN_HEIGHT / 4)
    candyManRect = pygame.Rect(30, SCREEN_HEIGHT - 20 - SCREEN_HEIGHT / 4, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    switchRect = pygame.Rect(SCREEN_WIDTH - 30 - SCREEN_WIDTH / 2.5, SCREEN_HEIGHT - 20 - SCREEN_HEIGHT / 4,
                             SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)

    listOfRect = [raptorRect, latchRect, diceRect, sonataRect, candyManRect, switchRect]

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
                    index1 = changeIndex(index1, key)
                if key == pygame.K_UP or key == pygame.K_DOWN or key == pygame.K_LEFT or key == pygame.K_RIGHT:
                    index2 = changeIndex(index2, key)
                if key == pygame.K_SPACE:
                    hasChoosen1 = not hasChoosen1
                if key == pygame.K_RCTRL:
                    hasChoosen2 = not hasChoosen2
                if key == pygame.K_RETURN:
                    validateCharacter(index1, hasChoosen1, index2, hasChoosen2)

        screen.fill([0, 0, 0])

        if blinking is True:
            if not hasChoosen2:
                pygame.draw.rect(screen, [255, 0, 0],
                                 pygame.Rect(listOfRect[index2].x - 4, listOfRect[index2].y - 4, SCREEN_WIDTH / 2.5 + 8,
                                             SCREEN_HEIGHT / 4 + 8))
            if not hasChoosen1:
                pygame.draw.rect(screen, [0, 0, 255],
                                 pygame.Rect(listOfRect[index1].x - 4, listOfRect[index1].y - 4, SCREEN_WIDTH / 2.5 + 8,
                                             SCREEN_HEIGHT / 4 + 8))

        if hasChoosen1:
            pygame.draw.rect(screen, [0, 0, 255],
                             pygame.Rect(listOfRect[index1].x - 4, listOfRect[index1].y - 4, SCREEN_WIDTH / 2.5 + 8,
                                         SCREEN_HEIGHT / 4 + 8))

        if hasChoosen2:
            pygame.draw.rect(screen, [255, 0, 0],
                             pygame.Rect(listOfRect[index2].x - 4, listOfRect[index2].y - 4, SCREEN_WIDTH / 2.5 + 8,
                                         SCREEN_HEIGHT / 4 + 8))

        for i in range(len(listOfRect)):
            pygame.draw.rect(screen, [255, 255, 0], listOfRect[i])
            center = (listOfRect[i].centerx - listOfCharacterBg[i].get_size()[0] / 2, listOfRect[i].y)
            screen.blit(listOfCharacterBg[i], center)

        pygame.display.update()
    pygame.quit()


# Launch the game
welcomeScreen()
