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
# Icon
icon = pygame.image.load("data/images/Latch/Default/Latch_Default.png")
pygame.display.set_icon(icon)
# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lethal League")
# Clock
clock = pygame.time.Clock()
# Music
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

defaultControls = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_c,
                   pygame.K_o,
                   pygame.K_l, pygame.K_k, pygame.K_m, pygame.K_RCTRL,
                   pygame.K_n,
                   pygame.K_p]

controls = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_c, pygame.K_o,
            pygame.K_l, pygame.K_k, pygame.K_m, pygame.K_RCTRL,
            pygame.K_n,
            pygame.K_p]

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

    # play gameLoop sound
    channel1.play(listOfMusicPath[1], loops=-1)

    # Map
    map_background_scaled = pygame.transform.scale(listOfMapBackgrounds[gameManager.map], (SCREEN_WIDTH, SCREEN_HEIGHT))
    score = Score()

    # Settings controls
    particle = Particle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 30, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    player.mapControls(controls[0:7])
    player2.mapControls(controls[7:14])
    players = [player, player2]
    resetPositions(players, particle, score)

    # events
    playerHasScored = pygame.USEREVENT + 1
    eventOccurs = False

    # while loop to keep the game running
    while run:
        # checking the frame rate
        ms_frame = clock.tick(300)
        # checking events
        if stopAll is True:
            run = False
            return True
        for event in pygame.event.get():
            # if the player decide to quit
            if event.type == pygame.QUIT:
                mixer.music.stop()
                stopAll = True
            # if a player scored
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.music.stop()
                    run = False
                    break
            if event.type == playerHasScored:
                eventOccurs = False
                # Re-enabling movement for players
                players[0].unableToMove = False
                players[1].unableToMove = False
                resetPositions(players, particle, score)
        screen.blit(map_background_scaled, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, SCREEN_HEIGHT - 30, SCREEN_WIDTH, 30))
        # drawing the players
        for player in players:
            player.draw(screen)
            player.update(screen, ms_frame, score, channel2, channel3)

        # drawing and moving the particle
        particle.move(gravity, ms_frame)
        particle.bounce(players, clock)
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

    # stop the channel which is playing the music
    channel1.stop()
    stopAll = chooseCharacterScreen(stopAll)


# function that reset position of the ball, the players and score attribute
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
    text2 = font.render('OR R TO CHANGE CONTROLS', True, [255, 255, 255])

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
            mixer.music.stop()
            pygame.quit()
            exit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopAll = True
                mixer.music.stop()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mapControlsMenu()
                    break
                if event.key == pygame.K_ESCAPE:
                    mixer.music.stop()
                    pygame.quit()
                    exit()
                    break
                stopAll = chooseCharacterScreen(stopAll)
            # blinking event
            if event.type == blink:
                textDisplayed = not textDisplayed

        # Background
        if stopAll is False:
            screen.blit(welcome_background_scaled, (0, 0))
        # Blinking text
        if textDisplayed is True:
            screen.blit(text, (SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 75))
            screen.blit(text2, (SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 40))
        pygame.display.update()


# function that enables the player to choose the map
def chooseMapScreen(stopAll):
    # create the object used to handle map choices
    chooseElement = ChooseElement(screen, listOfMapMenuBackgrounds, 2, 4, SCREEN_WIDTH, SCREEN_HEIGHT)
    run = True

    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)

    # Useful boolean
    blinking = True
    hasChoosen = False
    index = 0

    # loop
    while run:
        if stopAll is True:
            return True
        for event in pygame.event.get():
            # if the player decide to quit
            if event.type == pygame.QUIT:
                stopAll = True
                break
            # blinking event
            if event.type == blink:
                blinking = not blinking
            # if player is moving to choose the game map
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_r:
                    mapControlsMenu()
                    break
                if key == controls[0] or key == controls[1] or key == controls[2] or key == controls[3]:
                    index = chooseElement.changeIndex(index, key, controls[0:5], controls[7:11])
                # if he selects/not selects the map
                if key == pygame.K_SPACE:
                    hasChoosen = not hasChoosen
                # if he validates the map
                if key == pygame.K_RETURN:
                    if hasChoosen is True:
                        gameManager.map = index
                        # stop music
                        channel0.stop()
                        stopAll = gameLoop(stopAll)

        screen.fill([0, 0, 0])

        # draw rectangles choices
        chooseElement.fillRectangleWithBackgrounds(screen)

        if hasChoosen is True:
            drawValidation()

        # this part is used to make the "blinking event"
        if blinking is True:
            if not hasChoosen:
                chooseElement.drawBorderOfRectangleChoice(screen, index, (0, 0, 255))

        if hasChoosen:
            chooseElement.drawBorderOfRectangleChoice(screen, index, (0, 0, 255))

        pygame.display.update()


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

    # # create the object used to handle characters choices
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
            return True
        for event in pygame.event.get():
            # if the player decide to quit
            if event.type == pygame.QUIT:
                stopAll = True
                welcomeScreen()
                return
            # if there is a blinking event
            if event.type == blink:
                blinking = not blinking
            # if players are moving to choose their characters
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    welcomeScreen()
                # player 1
                if key == controls[0] or key == controls[1] or key == controls[2] or key == controls[3]:
                    index1 = chooseElement.changeIndex(index1, key, controls[0:4], controls[7:11])
                if event.key == pygame.K_r:
                    mapControlsMenu()
                    break
                # player 2
                if key == controls[7] or key == controls[8] or key == controls[9] or key == controls[10]:
                    index2 = chooseElement.changeIndex(index2, key, controls[0:4], controls[7:11])
                # selection
                if key == controls[4]:
                    hasChoosen1 = not hasChoosen1
                if key == controls[11]:
                    hasChoosen2 = not hasChoosen2
                # if validation, update gameManager values
                if hasChoosen1 is True and hasChoosen2 is True:
                    if key == pygame.K_RETURN:
                        gameManager.firstCharacter = index1
                        gameManager.secondCharacter = index2
                        stopAll = chooseMapScreen(stopAll)

        screen.fill([0, 0, 0])

        # fill rectangle choices with backgrounds
        chooseElement.fillRectangleWithBackgrounds(screen)

        # if the two players have chosen
        if hasChoosen1 is True and hasChoosen2 is True:
            drawValidation()

        # blinking events
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


def mapControlsMenu():
    # Fonts
    font = pygame.font.SysFont("rubik", 35)
    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)
    rectangles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    text = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    textCommands = [0, 0, 0, 0, 0, 0, 0]
    currentIndex = 0
    # create a reset button at middle
    rectangleReset = pygame.Rect(SCREEN_WIDTH / 2 - 100, 25, 200, 75)
    textReset = font.render("Reset - R", True, (255, 255, 255))
    changingKey = False
    strings = ["Attaque haute", "Attaque basse", "Aller a gauche", "Aller a droite",
               "Sauter / Confirmer",
               "Attaquer",
               "Coup spécial"]
    textJ1 = font.render("Joueur 1", True, (0, 0, 255))
    textJ2 = font.render("Joueur 2", True, (255, 0, 0))
    textReturn = font.render("<- Retour - Echap", True, (255, 255, 255))
    for i in range(0, 14):
        if i <= 6:
            rectangles[i] = pygame.Rect(SCREEN_WIDTH / 4 - 100, SCREEN_HEIGHT / 2 - 300 + i * 100, 200, 75)
        else:
            rectangles[i] = pygame.Rect(SCREEN_WIDTH / 4 * 3 - 100, SCREEN_HEIGHT / 2 - 300 + (i - 7) * 100, 200, 75)
        text[i] = font.render(pygame.key.name(controls[i]), True, (255, 255, 255))
    for i in range(0, 7):
        textCommands[i] = font.render(strings[i], True, (255, 255, 255))
    run = True
    print(rectangles)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if changingKey:
                    controls[currentIndex] = key
                    text[currentIndex] = font.render(pygame.key.name(controls[currentIndex]), True, (255, 255, 255))
                    changingKey = False
                    break
                if key == pygame.K_ESCAPE and changingKey is False:
                    run = False
                    break
                if key == pygame.K_r:
                    for i in range(0, 14):
                        controls[i] = defaultControls[i]
                        text[i] = font.render(pygame.key.name(controls[i]), True, (255, 255, 255))
                    break
                if (key == pygame.K_z or key == pygame.K_UP) and changingKey is False:
                    currentIndex = (currentIndex - 1) % len(rectangles)
                elif key == pygame.K_s or key == pygame.K_DOWN and changingKey is False:
                    currentIndex = (currentIndex + 1) % len(rectangles)
                elif key == pygame.K_q or key == pygame.K_LEFT and changingKey is False:
                    if currentIndex > len(rectangles) / 2 - 1:
                        currentIndex -= len(rectangles) / 2
                elif key == pygame.K_d or key == pygame.K_RIGHT and changingKey is False:
                    if currentIndex < len(rectangles) / 2:
                        currentIndex += len(rectangles) / 2
                elif key == pygame.K_RETURN and changingKey is False:
                    changingKey = True
                    text[currentIndex] = font.render("...", True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        for i in range(0, 14):
            if i == currentIndex and changingKey is False:
                pygame.draw.rect(screen, (255, 0, 255), rectangles[i], 5)
            elif i == currentIndex and changingKey is True:
                pygame.draw.rect(screen, (0, 255, 0), rectangles[i], 5)
            else:
                pygame.draw.rect(screen, (255, 255, 255), rectangles[i], 2)
        screen.blit(textJ1, (SCREEN_WIDTH / 4 - 50, SCREEN_HEIGHT / 2 - 400))
        screen.blit(textJ2, (SCREEN_WIDTH / 4 * 3 - 50, SCREEN_HEIGHT / 2 - 400))
        screen.blit(textReturn, (50, 50))
        for i in range(0, 7):
            screen.blit(textCommands[i], (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 275 + i * 100))
        for i in range(0, 14):
            screen.blit(text[i], (rectangles[i].x + 50, rectangles[i].y + 25))
        pygame.draw.rect(screen, (255, 255, 255), rectangleReset, 2)
        screen.blit(textReset, (rectangleReset.x + 50, rectangleReset.y + 25))
        pygame.display.update()


# function used to print on screen the key to press to validate choices
def drawValidation():
    pygame.draw.rect(screen, [0, 0, 0], [0, SCREEN_HEIGHT / 2 - 100, SCREEN_WIDTH, 200])
    text = pygame.font.SysFont("rubik", 80, italic=True).render('PRESS Enter TO CONTINUE', True, [255, 255, 255])
    screen.blit(text, (SCREEN_WIDTH - 1200, SCREEN_HEIGHT / 2 - 20))


# Launch the game
welcomeScreen()
