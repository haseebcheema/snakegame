#  importing pygame
import pygame

# importing the constants of pygame
from pygame.locals import *

# importing time module
import time

# importing random module
import random


# global size and background colour
SIZE = 40
BACKGROUND_COLOR = (231, 221, 129)

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

    # shift apple to random position
    def move(self):
        self.x = random.randint(1, 19) * SIZE
        self.y = random.randint(1, 14) * SIZE

# game class
class Game:
    def __init__(self):

        # pygame setup
        pygame.init()

        # setup of window screen
        self.screen = pygame.display.set_mode((800, 600))

        #  instance of snake
        self.snake = Snake(self.screen, 1)

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

        # display score
        self.display_score()

        # called when any update occurs
        pygame.display.flip()

        # check if apple collides with snake's head
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # check if snake collides with itself
        for i in range(5, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "GAME OVER!"
    
    # reset/restart the game
    def reset(self):

         # new instance of snake
        self.snake = Snake(self.screen, 1)

        # new instance of apple
        self.apple = Apple(self.screen)

    # collision of snake with apple
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True
        return False

    # calculate score
    def display_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: { self.snake.length }", True, (0, 0, 0))
        self.screen.blit(score, (680, 10))

    # game over
    def show_game_over(self):
        self.screen.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont("arial", 30)
        line1 = font.render(f"Game is over! Score: { self.snake.length }", True, (0, 0, 0))
        self.screen.blit(line1, (300, 300))
        line2 = font.render("To play again, press Enter otherwise press Escape to exit!", True, (0, 0, 0))
        self.screen.blit(line2, (120, 350))
        pygame.display.flip()
    
    # run
    def run(self):

        # instance for running the snake game
        running = True

        # instance for pausing the snake game
        pause = False
        # loop to run and end the window screen
        while running:
            # poll for events
            for event in pygame.event.get():
                # catching different events and checking
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
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

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()


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
        self.parent_screen.fill(BACKGROUND_COLOR)
        
        # showing blocks on the window screen
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        
        # updating the display to show changes
        pygame.display.flip()

    #  increase snake's length and add block
    def increase_length(self):
        self.length = self.length + 1
        self.x.append(-1)
        self.y.append(-1)

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