import pygame
import random

number = 0

# Initialize pygame
pygame.init()

# Creating the Window
screen = pygame.display.set_mode((800, 600))

# Creating Logo and Caption
pygame.display.set_caption("img/Roll Dice")
pygame.display.set_icon(pygame.image.load("img/dice.png"))

# Displaying image
image = None


def show_image():
    screen.blit(image, (150, 30))


# Function for showing text
def show_text():
    screen.blit(pygame.font.Font("freesansbold.ttf", 32).render("Next Roll - enter    Quit - escape key", True,
                                                                (255, 0, 0)), (125, 560))


# Random for dice
def roll_dice():
    global image, number
    choices = []
    for i in range(1, 7):
        if i != number:
            choices.append(i)
    number = random.choice(choices)

    image = pygame.image.load(f"img/{number}.png")


roll_dice()

# Main Loop
running = True

while running:
    # Background
    screen.fill((255, 255, 255))  # RGB

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                roll_dice()

            if event.key == pygame.K_ESCAPE:
                running = False

    show_image()

    show_text()

    pygame.display.update()
