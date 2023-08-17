#  importing pygame
import pygame
# importing the constants of pygame
from pygame.locals import *
# importing time module
import time

# global size value
SIZE = 40

# apple class
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        
        # image of apple
        self.image = pygame.image.load("./resources/apple.jpg").convert()

        #  coordinates of apple
        self.x = SIZE*3
        self.y = SIZE*3

    # draw method for apple
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        
        # updating the display to show changes
        pygame.display.flip()

# game class
class Game:
    def __init__(self):

        # pygame setup
        pygame.init()

        # setup of window screen
        self.screen = pygame.display.set_mode((800, 600))

        #  instance of snake
        self.snake = Snake(self.screen, 5)

        # calling draw method of snake to draw block on the window screen
        self.snake.draw()

        #  instance of apple
        self.apple = Apple(self.screen)

        # calling draw method of apple to draw it on the window screen
        self.apple.draw()
    
    # play
    def play(self):
        # change the direction
        self.snake.walk()

        # draw apple
        self.apple.draw()

    # run
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

            # play
            self.play()

            #  continues walking in the particular direction after every given seconds
            time.sleep(0.2)

            # display the window screen or updating the display to show changes
            pygame.display.flip()

# snake class
class Snake:
    def __init__(self, parent_screen, length):

        self.parent_screen = parent_screen
        # importing image resource
        self.block = pygame.image.load("./resources/block.jpg").convert()
        # setting the lenth of the snake
        self.length = length
        # setting the coordinates of the blocks
        self.x = [SIZE]*self.length
        self.y = [SIZE]*self.length
        #  setting inital movement of block
        self.direction = "right"

    # updations to draw/move the block on the screen
    def draw(self):

        # setting the bg color of the window screen
        self.parent_screen.fill((231, 221, 129))
        
        # showing blocks on the window screen
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        
        # updating the display to show changes
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

        # shifting blocks to the previous position
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        # checking direction and moving to that specific direction
        if self.direction == "up":
            self.y[0] = self.y[0] - SIZE
        elif self.direction == "down":
            self.y[0] = self.y[0] + SIZE
        elif self.direction == "left":
            self.x[0] = self.x[0] - SIZE
        elif self.direction == "right":
            self.x[0] = self.x[0] + SIZE
        
        #  draw the block
        self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()