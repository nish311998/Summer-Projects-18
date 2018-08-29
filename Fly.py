import pygame, sys
from pygame.locals import *


#setup color of screen and bricks and figure
white = [255,255,255]
blue = [0,0,255]
red = [255, 0, 0]
green = [69,139,0]
black = [0,0,0]

#Game Stats
winWidth = 1000
winHeight = 1000
brick_height = 12
brick_width_max_range = 50 #this can be any random size

#Dimensions
#max_sprite_x
#max_sprite_y
#max_brick_x

class Fly:
    def__init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([winWidth, winHeight])
        pygame.display.set_caption("To Space")
        self.clock = pygame.time.Clock()

        if pygame.font:
            self.font = pygame.font.Font(None, 25)

        self.init_game()
        
    def init_game(self):

    def move_bricks(self):

    def move_block(self):

    def show_message(self, str):

    def run(self):
        
