import pygame, sys
from pygame.locals import *



#Game Stats
winWidth = 400
winHeight = 400
paddle_height = 12
paddle_width = 50
brick_width = 50
brick_height = 12
ball_diameter = 16
ball_radius = int(ball_diameter/2)

#Dimensions
max_ball_y = winHeight - ball_diameter
max_ball_x = winWidth - ball_diameter
max_paddle_x = winWidth - paddle_width

#y-coord of paddle
paddle_y = winHeight - paddle_height


#states
ball_paddle = 0
play = 1
lose = 2
win = 3

#setup color of screen and bricks and balls
white = [255,255,255]
blue = [0,0,255]
red = [255, 0, 0]
green = [69,139,0]
black = [0,0,0]



#creating a class for the ball


class BallGame:

    def __init__(self):
       pygame.init()
       self.screen = pygame.display.set_mode([winWidth, winHeight])
       pygame.display.set_caption("Break the Bricks")
       self.clock = pygame.time.Clock()
       
       if pygame.font:
           self.font = pygame.font.Font(None, 25)
        
       else:
           self.font = None
        
       self.init_game()

    def init_game(self):
        self.ball_vel = [5,-5]
        self.paddle = pygame.Rect(175, paddle_y, paddle_width, paddle_height)
        self.ball = pygame.Rect(194, paddle_y - ball_diameter, ball_diameter, ball_diameter) 
        self.lives = 3
        self.score = 0
        self.level = 0
        self.game_state = ball_paddle
        self.ballcolor = red

        self.create_bricks()

    def create_bricks(self):
        self.brick_list = []
        y_incr = 50
        for i in range(7):
            x_incr = 30
            for j in range(6):
                self.brick_list.append(pygame.Rect(x_incr, y_incr, brick_width, brick_height))
                x_incr+=60
            y_incr+=20
            
    def draw_bricks(self):
        for brick in self.brick_list:
            pygame.draw.rect(self.screen, black, brick)
        
    def check_input(self):
        key_val = pygame.key.get_pressed()

        if key_val[pygame.K_LEFT] and self.game_state != ball_paddle:
            self.paddle.left-=6
            if self.paddle.left < 0:
                self.paddle.left = 0

        if key_val[pygame.K_RIGHT] and self.game_state != ball_paddle:
            self.paddle.left+=6
            if self.paddle.left > max_paddle_x:
                self.paddle.left = max_paddle_x

        if key_val[pygame.K_SPACE] and self.game_state == ball_paddle:
            self.ball_vel = [5,-5]
            self.game_state = play
        elif key_val[pygame.K_RETURN] and (self.game_state == lose or self.game_state == win):
            self.init_game()

    def move_ball(self):
        self.ball.left += self.ball_vel[0]
        self.ball.top += self.ball_vel[1]
        
        if self.ball.left < 0:
            self.ball.left = 0
            self.ball_vel[0]*=-1

        elif self.ball.left > max_ball_x:
            self.ball.left = max_ball_x
            self.ball_vel[0]*=-1
            
        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_vel[1]*=-1

        elif (self.ball.top > max_ball_y) or self.ball.top > paddle_y:
            self.lives-=1
            self.ballcolor = red
            if self.lives == 0:
                self.game_state = lose
            else:
                self.game_state = ball_paddle
                self.paddle = pygame.Rect(175, paddle_y, paddle_width, paddle_height)
                self.ball = pygame.Rect(194, paddle_y - ball_diameter, ball_diameter, ball_diameter)            
        
    def handle_collision(self):
        if self.ball.colliderect(self.paddle):
            self.ball_vel[1]*=-1
            self.ballcolor = red
            
        for brick in self.brick_list:
            if self.ball.colliderect(brick):
                self.score +=5
                self.brick_list.remove(brick)
                self.ball_vel[1]*=-1
                self.ballcolor = green
                break
        if len(self.brick_list) == 0:
            self.game_state = win
            
        
            
        
    def show_stat(self):
        tempstr = "Score:" + str(self.score) + "  Lives:" + str(self.lives) + " Level:" + str(self.level)
        self.text = self.font.render(tempstr, False, black)
        center = (400 - self.font.size(tempstr)[0])/2
        self.screen.blit(self.text, (center,0))
        
    def show_message(self, str):
        self.message = self.font.render(str, False, black)
        initpos = (400 - self.font.size(str)[0])/2
        self.screen.blit(self.message, (initpos,300))
        
            
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            self.clock.tick(50)
            self.screen.fill(white)
            #check input
            self.check_input()

            #Printing messages
            
            if self.game_state == win:
                self.show_message("You Won! Press Enter to play again")
            elif self.game_state == lose:
                self.show_message("Game Over. Press Enter to play again")
            elif self.game_state == ball_paddle:
                self.show_message("Press Space to play")
            elif self.game_state == play:
                self.move_ball()
                self.handle_collision()



            #Draw bricks
            self.draw_bricks()
            
            #Draw paddle
            pygame.draw.rect(self.screen, black, self.paddle)

            #Draw ball
            pygame.draw.circle(self.screen, self.ballcolor,(self.ball.left + ball_radius, self.ball.top + ball_radius), ball_radius)

            self.show_stat()

            pygame.display.flip()


if __name__ == "__main__":
    BallGame().run()
    


