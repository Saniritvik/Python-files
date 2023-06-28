import pygame

# initialize Pygame
pygame.init()

# set the dimensions of the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set the background color
background_color = (255, 255, 255)

# set the dimensions and initial position of the block
block_width = 50
block_height = 50
block_x = 0
block_y = WINDOW_HEIGHT // 2 - block_height // 2

# set the speed of the block
block_speed = 5

# set the FPS (frames per second) of the game
clock = pygame.time.Clock()
FPS = 60

# create a loop that will run until the game is closed
while True:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # move the block
    block_x += block_speed

    # draw the background and the block
    game_window.fill(background_color)
    pygame.draw.rect(game_window, (0, 0, 0), (block_x, block_y, block_width, block_height))

    # update the display
    pygame.display.update()

    # limit the FPS of the game
    clock.tick(FPS)