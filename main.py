import pygame
import math
from data.player import Player
from data.particle import Particle
from data.character import Character
from data.sprite import Sprite

# Consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lethal League")
clock = pygame.time.Clock()

# Players
raptor = Sprite(Character.RAPTOR)
latch = Sprite(Character.LATCH)

# Background images
game_background = pygame.image.load("data/images/bg.png")
game_background_scaled = pygame.transform.scale(game_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
welcome_background = pygame.image.load("data/images/welcome_background.jpg")
welcome_background_scaled = pygame.transform.scale(welcome_background, (SCREEN_WIDTH, SCREEN_HEIGHT))


def gameLoop():
    gravity = (math.pi, 0.0003)
    run = True

    player = Player(100, 100, (0, 0, 255), pygame.Rect(0, 0, 300, 30), raptor)
    player2 = Player(700, 100, (255, 0, 0), pygame.Rect(screen.get_width() - 300, 0, 300, 30), latch)
    particle = Particle(300, 100, 10, screen)
    player.mapControls(pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_LCTRL)
    player2.mapControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL, pygame.K_RSHIFT,
                        pygame.K_n)
    players = [player, player2]
    while run:
        ms_frame = clock.tick(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(game_background_scaled, (0, 0))
        for player in players:
            player.draw(screen)
            player.move(particle, screen, ms_frame)
        particle.move(gravity, ms_frame)
        particle.bounce(players)
        particle.display(screen)
        pygame.display.update()

    pygame.quit()


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


# Function that enables players to choose their characters
def chooseCharacterScreen():

    # Those rectangles will represent characters
    raptorRect = pygame.Rect(30, 20, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    latchRect = pygame.Rect(SCREEN_WIDTH - 30 - SCREEN_WIDTH / 2.5, 20, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    diceRect = pygame.Rect(30, 20 + SCREEN_HEIGHT / 4 + 55, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    sonataRect = pygame.Rect(SCREEN_WIDTH - 30 - SCREEN_WIDTH / 2.5, 20 + SCREEN_HEIGHT / 4 + 55, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    candyManRect = pygame.Rect(30, SCREEN_HEIGHT - 20 - SCREEN_HEIGHT / 4, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)
    switchRect = pygame.Rect(SCREEN_WIDTH - 30 - SCREEN_WIDTH / 2.5, SCREEN_HEIGHT - 20 - SCREEN_HEIGHT / 4, SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 4)

    listOfRect = [raptorRect, latchRect, diceRect, sonataRect, candyManRect, switchRect]
    listOfCharacter = [Character.RAPTOR, Character.LATCH, Character.DICE, Character.SONATA, Character.CANDYMAN, Character.SWITCH]

    # Create a user event appearing every 0.5 sec
    blink = pygame.USEREVENT
    pygame.time.set_timer(blink, 500)

    run = True
    blinking = True
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

        screen.fill([0, 0, 0])

        if blinking is True:
            pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(listOfRect[index2].x - 4, listOfRect[index2].y - 4, SCREEN_WIDTH / 2.5 + 8, SCREEN_HEIGHT / 4 + 8))
            pygame.draw.rect(screen, [0, 0, 255], pygame.Rect(listOfRect[index1].x - 4, listOfRect[index1].y - 4, SCREEN_WIDTH / 2.5 + 8, SCREEN_HEIGHT / 4 + 8))

        for i in range(len(listOfRect)):
            pygame.draw.rect(screen, [255, 255, 255], listOfRect[i])

        pygame.display.update()
    pygame.quit()


# Launch the game
welcomeScreen()
