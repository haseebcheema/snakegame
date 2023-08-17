#  importing pygame
import pygame
# importing the constants of pygame
from pygame.locals import *
# importing time module
import time

# game class
class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        # setup of window screen
        self.screen = pygame.display.set_mode((800, 600))
        #  instance of snake
        self.snake = Snake(self.screen)
        # calling draw method of snake to draw block on the window screen
        self.snake.draw()
    
    def run(self):

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
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        # move down
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        # move left
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        # move right
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False

            # change the direction
            self.snake.walk()
            #  continues walking in the particular direction after every given seconds
            time.sleep(0.2)

            # display the window screen
            pygame.display.flip()

# snake class
class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # importing image resource
        self.block = pygame.image.load("./resources/block.jpg").convert()
        # setting the size of the block
        self.x = 100
        self.y = 100
        #  setting inital movement of block
        self.direction = "right"

    # updations to draw/move the block on the screen
    def draw(self):
        # setting the bg color of the window screen
        self.parent_screen.fill((231, 221, 129))
        # showing that block resource on the window screen
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    # update the direction for move up
    def move_up(self):
        self.direction = "up"

    # update the direction for move down
    def move_down(self):
        self.direction = "down"

    # update the direction for move left
    def move_left(self):
        self.direction = "left"

    # update the direction for move right
    def move_right(self):
        self.direction = "right"

    # walk method for the snake
    def walk(self):
        if self.direction == "up":
            self.y = self.y - 10
        elif self.direction == "down":
            self.y = self.y + 10
        elif self.direction == "left":
            self.x = self.x - 10
        elif self.direction == "right":
            self.x = self.x + 10
        
        #  draw the block
        self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()