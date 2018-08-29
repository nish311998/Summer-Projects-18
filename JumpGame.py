import pygame, sys, random
from random import randint
from pygame.locals import *


#setup color of screen and bricks and figure
white = [255,255,255]
blue = [0,0,255]
red = [255, 0, 0]
green = [69,139,0]
black = [0,0,0]

#Game Stats
winWidth = 600
winHeight = 600
brick_height = 12
brick_width = 50 #this can be any random size
sprite_diameter = 30 #sprite diameter
sprite_radius = int(sprite_diameter/2)

#states
win = 1
lose = 2
ingame = 3
start = 4

#Dimensions
#brick_max_x =
sprite_placement_x = (winWidth - sprite_diameter)/2
sprite_placement_y = (winHeight - sprite_diameter)/2
sprite_max_x = winWidth-sprite_diameter

class Fly:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([winWidth, winHeight])
        pygame.display.set_caption("To Space")
        self.clock = pygame.time.Clock()

        if pygame.font:
            self.font = pygame.font.Font(None, 25)
        else:
            self.font = None

        self.init_game()


    def init_game(self):
        self.brickvel = [0,2] #the rate at which the bricks falls down
        self.sprite = pygame.Rect(sprite_placement_x, sprite_placement_y, sprite_diameter, sprite_diameter) 
        self.lives = 1
        self.score = 0
        self.game_state = start
        self.arr = []
        self.makeBricks()
        self.time = 0                         
    def makeBricks(self):
        helperlist = [pygame.Rect(randint(0,winWidth - brick_width), 0, brick_width, brick_height), 15]
        self.arr.append(helperlist)
        
    def moveBricks(self):
        for brick in self.arr:
            brick[0].left+=self.brickvel[0]
            brick[0].top+=self.brickvel[1]
            self.time+=self.brickvel[1]
            
    def drawBricks(self): 
        for brick in self.arr:
            pygame.draw.rect(self.screen, white, brick[0])

    def moveSprite(self):
            
        key_val = pygame.key.get_pressed()
        if key_val[pygame.K_LEFT] and self.game_state == ingame:
            self.sprite.left-=2
            if self.sprite.left<0:
                self.sprite.left = 0

        if key_val[pygame.K_RIGHT] and self.game_state == ingame:
            self.sprite.left+=2
            if self.sprite.left>sprite_max_x:
                self.sprite.left = sprite_max_x

        if key_val[pygame.K_SPACE] and self.game_state == start:
            self.game_state = ingame

        if  key_val[pygame.K_RETURN] and self.game_state == (lose or win):
            self.init_game()
            

    def collision(self):
        for brick in self.arr:
            if brick[0].colliderect(self.sprite):
                self.lives-=1
                self.game_state = lose
            if brick[0].top>(winWidth - brick_height):
                self.arr.remove(brick)
            if brick[0].top > (winWidth - sprite_placement_y):
                self.score += brick[1]
                brick[1] = 0
            
                
                
    def checkWin(self):
        if self.score >= 10000:
            self.game_state = win

    def show_message(self, str):
        self.message = self.font.render(str, False, white)
        initpos = (winWidth - self.font.size(str)[0])/2
        self.screen.blit(self.message, (initpos,int(winHeight*4/5)))

    def show_stats(self):
        tempstr = "Score:" + str(self.score) + "  Lives:" + str(self.lives)
        self.text = self.font.render(tempstr, False, white)
        center = (winWidth - self.font.size(tempstr)[0])/2
        self.screen.blit(self.text, (center,0))

    def run(self):

        while True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            self.clock.tick(50)
            background = pygame.image.load("starry night.jpg").convert()
            background = pygame.transform.scale(background, (winWidth, winHeight))
            self.screen.blit(background, [0,0])

            #call movesprite to initalize the game
            self.moveSprite()

            #show stats
            self.show_stats()

            #check for a win
            self.checkWin()
            if self.game_state == start:
                self.show_message("Dodge all the obstacles. Press space to start the game")
            elif self.game_state == win:
                self.show_message("You won! Press Enter to play again")
            elif self.game_state == lose:
                self.show_message("That's the end.. Press Enter to play again")
            elif self.game_state == ingame:
                if self.time != 0 and self.time%(self.brickvel[1]*20) == 0:
                    self.makeBricks()
                self.moveBricks()
                self.collision()
                
            #Draw Everything
            self.drawBricks()

            pygame.draw.circle(self.screen, white,(self.sprite.left + sprite_radius, self.sprite.top + sprite_radius), sprite_radius)

            pygame.display.flip()  
        


if __name__ == "__main__":
    Fly().run()
