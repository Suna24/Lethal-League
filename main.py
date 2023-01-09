import pygame
import math
from pygame import mixer
from data.player import Player
from data.particle import Particle
from data.characterenum import CharacterEnum
from data.sprite import Sprite
from data.score import Score
from data.direction import Direction
from data.chooseElement import ChooseElement
from data.gameManager import GameManager

# Consts
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SIZE = 275

# Initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lethal League")
clock = pygame.time.Clock()
mixer.init(channels=4)

# Init channels
channel0 = mixer.Channel(0)
channel0.set_volume(0.1)
channel1 = mixer.Channel(1)
channel1.set_volume(0.1)

# For players
channel2 = mixer.Channel(2)
channel2.set_volume(0.75)
channel3 = mixer.Channel(3)
channel3.set_volume(0.7)

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
listOfMapMenuBackgrounds = [
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
listOfCharacters = [CharacterEnum.LATCH, CharacterEnum.RAPTOR, CharacterEnum.DICE, CharacterEnum.CANDYMAN,
                    CharacterEnum.SONATA, CharacterEnum.SWITCH]
listOfSprites = [Sprite(CharacterEnum.LATCH, SIZE), Sprite(CharacterEnum.RAPTOR, SIZE),
                 Sprite(CharacterEnum.DICE, SIZE), Sprite(CharacterEnum.CANDYMAN, SIZE),
                 Sprite(CharacterEnum.SONATA, SIZE), Sprite(CharacterEnum.SWITCH, SIZE)]

# Sounds
listOfMusicPath = [mixer.Sound("data/musics/HomePage.ogg"),
                   mixer.Sound("data/musics/Fight.ogg")]


# Function used to display and play the game loop
def gameLoop(stopAll):
    print(gameManager.map)
    # setting gravity
    gravity = (math.pi, 0.002)
    run = True

    # Creating players
    player = Player(100, SCREEN_HEIGHT - 100, (0, 0, 255), pygame.Rect(0, 0, 400, 40), pygame.Rect(0, 40, 400, 20),
                    listOfCharacters[gameManager.firstCharacter], Direction.RIGHT,
                    listOfSprites[gameManager.firstCharacter], SCREEN_WIDTH, SCREEN_HEIGHT)
    player2 = Player(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, (255, 0, 0), pygame.Rect(screen.get_width() - 400, 0, 400,
                                                                                       40),
                     pygame.Rect(screen.get_width() - 400, 40, 400, 20), listOfCharacters[gameManager.secondCharacter],
                     Direction.LEFT,
                     listOfSprites[gameManager.secondCharacter], SCREEN_WIDTH, SCREEN_HEIGHT)
    # Sound
    channel1.play(listOfMusicPath[1], loops=-1)

    END_MUSIC = pygame.USEREVENT + 100
    channel2.set_endevent(END_MUSIC)
    channel3.set_endevent(END_MUSIC)

    # Map
    map_background_scaled = pygame.transform.scale(listOfMapBackgrounds[gameManager.map], (SCREEN_WIDTH, SCREEN_HEIGHT))
    score = Score()

    # Settings controls
    particle = Particle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 30, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    player.mapControls(pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_c)
    player2.mapControls(pygame.K_KP8, pygame.K_KP5, pygame.K_KP4, pygame.K_KP6, pygame.K_KP_ENTER, pygame.K_RIGHT,
                        pygame.K_DOWN)
    players = [player, player2]
    resetPositions(players, particle, score)

    playerHasScored = pygame.USEREVENT + 1
    eventOccurs = False

    # while loop to keep the game running
    while run:
        # checking the frame rate
        ms_frame = clock.tick(300)
        # checking events
        if stopAll is True:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mixer.music.stop()
                stopAll = True
            # if a player scored
            if event.type == playerHasScored:
                eventOccurs = False
                # Re-enabling movement for players
                players[0].unableToMove = False
                players[1].unableToMove = False
                resetPositions(players, particle, score)
            if event.type == END_MUSIC:
                print("music_end")
        screen.blit(map_background_scaled, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, SCREEN_HEIGHT - 30, SCREEN_WIDTH, 30))
        # drawing the players
        for player in players:
            player.draw(screen)
            player.update(screen, ms_frame, score, channel2, channel3)

        # drawing and moving the particle
        particle.move(gravity, ms_frame)
        particle.bounce(players)
        # drawing scores
        score.draw(screen, SCREEN_WIDTH)
        particle.display(screen)
        # playing animation if a player scored
        if players[0].character.health <= 0:
            # Disabling movement for players
            players[0].unableToMove = True
            players[1].unableToMove = True
            if players[1].direction == Direction.RIGHT:
                players[1].playAnimation(screen, players[1].character.sprite.victoryRight)
            else:
                players[1].playAnimation(screen, players[1].character.sprite.victoryLeft)
            if eventOccurs is False:
                score.addScore(2)
                eventOccurs = True
                score.hasBeenCalled = True
                pygame.time.set_timer(playerHasScored, 3000, True)
            else:
                score.displayActualScore(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            pygame.display.update()

        elif players[1].character.health <= 0:
            # Disabling movement for players
            players[0].unableToMove = True
            players[1].unableToMove = True
            if players[0].direction == Direction.RIGHT:
                players[0].playAnimation(screen, players[0].character.sprite.victoryRight)
            else:
                players[0].playAnimation(screen, players[0].character.sprite.victoryLeft)
            if eventOccurs is False:
                score.addScore(1)
                eventOccurs = True
                score.hasBeenCalled = True
                pygame.time.set_timer(playerHasScored, 3000, True)
            else:
                score.displayActualScore(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            pygame.display.update()

        # checking if someone won
        if score.oneWon() is True:
            if eventOccurs is False:
                run = False
                pygame.time.set_timer(playerHasScored, 6000, True)
            else:
                score.displayActualScore(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.update()

    channel1.stop()
    chooseCharacterScreen(stopAll)


def resetPositions(players, ball, score):
    for player in players:
        player.resetPosition()
        player.character.resetUltimate()
    ball.resetPosition()
    score.hasBeenCalled = False


# Function that displays the first screen of the game
def welcomeScreen():
    # Fonts
    font = pygame.font.SysFont("rubik", 35)
    text = font.render('PRESS ANY KEY TO CONTINUE', True, [255, 255, 255])
    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)
    # Boolean useful
    stopAll = False
    run = True
    textDisplayed = True

    # Play music
    channel0.play(listOfMusicPath[0], loops=-1)

    while run:
        if stopAll is True:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                chooseCharacterScreen(stopAll)
            if event.type == blink:
                textDisplayed = not textDisplayed

        # Background
        screen.blit(welcome_background_scaled, (0, 0))
        # Blinking text
        if textDisplayed is True:
            screen.blit(text, (SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 75))
        pygame.display.update()

    pygame.quit()


def chooseMapScreen(stopAll):
    print("In choose map screen")

    chooseElement = ChooseElement(screen, listOfMapMenuBackgrounds, 2, 4, SCREEN_WIDTH, SCREEN_HEIGHT)
    run = True

    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)
    blinking = True
    hasChoosen = False
    index = 0

    while run:
        if stopAll is True:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopAll = True
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
                        channel0.stop()
                        gameLoop(stopAll)

        screen.fill([0, 0, 0])

        chooseElement.fillRectangleWithBackgrounds(screen)
        if hasChoosen is True:
            drawValidation()

        if blinking is True:
            if not hasChoosen:
                chooseElement.drawBorderOfRectangleChoice(screen, index, (0, 0, 255))

        if hasChoosen:
            chooseElement.drawBorderOfRectangleChoice(screen, index, (0, 0, 255))

        pygame.display.update()
    pygame.quit()


# Function that enables players to choose their characters
def chooseCharacterScreen(stopAll):
    # Sound
    if channel1.get_busy() is True:
        channel1.stop()

    if channel0.get_busy() is False:
        channel0.play(listOfMusicPath[0], loops=-1)

    # Load images
    listOfCharacterBg = [
        pygame.image.load("data/images/CharacterSelection/Latch.png"),
        pygame.image.load("data/images/CharacterSelection/Raptor.png"),
        pygame.image.load("data/images/CharacterSelection/Dice.png"),
        pygame.image.load("data/images/CharacterSelection/CandyMan.png"),
        pygame.image.load("data/images/CharacterSelection/Sonata.png"),
        pygame.image.load("data/images/CharacterSelection/Switch.png")]

    chooseElement = ChooseElement(screen, listOfCharacterBg, 3, 2, SCREEN_WIDTH, SCREEN_HEIGHT)

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
        if stopAll is True:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopAll = True
            if event.type == blink:
                blinking = not blinking
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_s or key == pygame.K_d or key == pygame.K_z:
                    index1 = chooseElement.changeIndex(index1, key)
                if key == pygame.K_KP8 or key == pygame.K_KP5 or key == pygame.K_KP4 or key == pygame.K_KP6:
                    index2 = chooseElement.changeIndex(index2, key)
                if key == pygame.K_SPACE:
                    hasChoosen1 = not hasChoosen1
                if key == pygame.K_KP_ENTER:
                    hasChoosen2 = not hasChoosen2
                if hasChoosen1 is True and hasChoosen2 is True:
                    if key == pygame.K_RETURN:
                        gameManager.firstCharacter = index1
                        gameManager.secondCharacter = index2
                        chooseMapScreen(stopAll)

        screen.fill([0, 0, 0])

        chooseElement.fillRectangleWithBackgrounds(screen)
        if hasChoosen1 is True and hasChoosen2 is True:
            drawValidation()

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


def drawValidation():
    pygame.draw.rect(screen, [0, 0, 0], [0, SCREEN_HEIGHT / 2 - 100, SCREEN_WIDTH, 200])
    text = pygame.font.SysFont("rubik", 80, italic=True).render('PRESS Enter TO CONTINUE', True, [255, 255, 255])
    screen.blit(text, (SCREEN_WIDTH - 1200, SCREEN_HEIGHT / 2 - 20))


# Launch the game
welcomeScreen()
