#  importing pygame
import pygame
# importing the constants of pygame
from pygame.locals import *

# updations to move the block on the screen
def draw_block():
    screen.fill((231, 221, 129))
    screen.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":

    # pygame setup
    pygame.init()

    # setup of window screen
    screen = pygame.display.set_mode((800, 600))

    # setting the color of the window screen
    screen.fill((231, 221, 129))

    # importing image resource
    block = pygame.image.load("./resources/block.jpg").convert()

    # setting the size of the block
    block_x = 100
    block_y = 100

    # showing that block resource on the window screen
    screen.blit(block, (block_x, block_y))
    
    # instance for running the snake game
    running = True

    # loop to run and end the window screen
    while running:
        # poll for events
        for event in pygame.event.get():
            # catching different events and checking
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    # move up
                    block_y = block_y + 10
                    draw_block()
                if event.key == K_DOWN:
                    # move down
                    block_y = block_y + 10
                    draw_block()
                if event.key == K_LEFT:
                    # move left
                    block_x = block_x - 10
                    draw_block()
                if event.key == K_RIGHT:
                    # move right
                    block_x = block_x + 10
                    draw_block()
            elif event.type == QUIT:
                running = False

            # display the window screen
            pygame.display.flip()