import pygame  # import pygame, system and os to use within code
import random
import sys
from pygame.locals import *  # remove the need to type pygame.local

pygame.init()  # start/initialize pygame

WIDTH = 400
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # set screen/display size
clock = pygame.time.Clock()


class DisplayText:
    def __init__(self):
        self.text_rect = None
        self.font = None
        self.text = None

    def displayTextCenter(self, size, line, color, y=HEIGHT / 2):
        self.font = pygame.font.Font("freesansbold.ttf", size)
        self.text = self.font.render(line, True, color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (WIDTH / 2, y)
        SCREEN.blit(self.text, self.text_rect)

    def displayTextAnywhere(self, size, line, color, pos):
        self.font = pygame.font.Font("freesansbold.ttf", size)
        self.text = self.font.render(line, True, color)
        self.text_rect = self.text.get_rect()
        self.text_rect.topleft = pos
        SCREEN.blit(self.text, self.text_rect)


class Boy:
    def __init__(self, points=0, life=3):
        self.coin_time = random.randint(100, 250)
        self.show = None
        self.points = points
        self.MOVE = None
        self.BOY_WIDTH = 50
        self.BOY_HEIGHT = 50
        self.BOY_X = 175
        self.BOY_Y = 500
        self.BOY_SPEED = 2
        self.BOY = pygame.transform.scale(pygame.image.load("boy.png"), (self.BOY_WIDTH, self.BOY_HEIGHT))
        self.lives = life
        self.invincible = 0
        self.counter = 1000
        self.BOY_RECT = pygame.Rect(self.BOY_X, self.BOY_Y, self.BOY_WIDTH, self.BOY_HEIGHT)

    def boyMove(self):
        for i in gold_coins:
            i.draw()
        self.coin_append()
        if self.counter > 0:
            self.counter -= 1
        else:
            self.BOY_SPEED += 0.1
            self.counter = 100
        self.MOVE = pygame.key.get_pressed()
        if self.MOVE[pygame.K_LEFT] and self.BOY_X > 0:
            self.BOY_X -= self.BOY_SPEED
        if self.MOVE[pygame.K_RIGHT] and self.BOY_X < 350:
            self.BOY_X += self.BOY_SPEED
        if self.MOVE[pygame.K_UP] and self.BOY_Y > 0:
            self.BOY_Y -= self.BOY_SPEED
        if self.MOVE[pygame.K_DOWN] and self.BOY_Y < 550:
            self.BOY_Y += self.BOY_SPEED
        if self.BOY_SPEED == 0 and self.MOVE[pygame.K_SPACE]:
            self.__init__()
            Level1()

    def displayBoy(self, display):
        self.BOY_RECT = pygame.Rect(self.BOY_X + 15, self.BOY_Y, self.BOY_WIDTH - 20, self.BOY_HEIGHT)
        if self.invincible == 0:
            display.blit(self.BOY, (self.BOY_X, self.BOY_Y))
        else:
            if self.show == 1:
                display.blit(self.BOY, (self.BOY_X, self.BOY_Y))
                self.show = 0
            else:
                self.show = 1
            
        start.displayTextAnywhere(15, "SCORE: " + str(self.points), (255, 255, 255), (10, 10))
        start.displayTextAnywhere(15, "LIFE: " + str(self.lives), (255, 255, 255), (10, 30))

    def gameOver(self):
        self.invincible = 0
        self.BOY_SPEED = 0
        for b in range(len(balls)):
            balls[b].BALL_DIRECTION = 0
        start.displayTextCenter(40, "GAME OVER", (0, 255, 0), 260)
        start.displayTextCenter(35, "FINAL SCORE: " + str(self.points), (0, 255, 0), 320)
        start.displayTextCenter(20, "Too restart press SPACEBAR", (0, 255, 0), 400)
        
    def coin_append(self):
        if self.coin_time <= 0:
            self.coin_time = random.randint(100, 250)
            gold_coins.append(Gold())
        else:
            self.coin_time -= 1


class Ball:
    def __init__(self, poss):
        self.poss = poss
        self.place = None
        self.BALL_RECT = None
        self.BALL_WIDTH = 50
        self.BALL_HEIGHT = 50
        self.BALL_X = random.randint(0, 350)
        self.BALL_Y = -50
        self.BALL_DIRECTION = random.randint(1, 3)
        self.BALL = pygame.transform.scale(pygame.image.load("ball.png"), (self.BALL_WIDTH, self.BALL_HEIGHT))

    def ballMove(self):
        self.BALL_Y += self.BALL_DIRECTION
        if self.BALL_Y >= HEIGHT:
            self.BALL_X = random.randint(0, 350)
            self.BALL_Y = 10
            self.BALL_DIRECTION += random.randint(5, 10) / 100
            boy.points += 1

    def ballDisplay(self, display):
        display.blit(self.BALL, (self.BALL_X, self.BALL_Y))
        self.place = (20 * self.poss) + 50

    def collide(self):
        self.BALL_RECT = pygame.Rect(self.BALL_X + 10, self.BALL_Y, self.BALL_WIDTH - 20, self.BALL_HEIGHT)
        if boy.invincible > 0:
            boy.invincible -= 1

        elif self.BALL_RECT.colliderect(boy.BOY_RECT):
            if boy.lives <= 1:
                boy.lives = 0
                boy.gameOver()
            else:
                boy.BOY_Y = 500
                boy.BOY_X = 175
                boy.invincible = 200 * len(balls)
                boy.lives -= 1


class Heart:
    def __init__(self):
        self.heart_rect = None
        self.circle = pygame.transform.scale(pygame.image.load("heart.png"), (32, 32))
        self.choice = None
        self.x = random.randint(0, 368)
        self.y = -25
        self.speed = None
        self.time = 5000

    def Life(self):
        if self.y == -25:
            self.choice = random.randint(0, 20)
            self.time -= 3
            self.x = random.randint(0, 368)
        if self.time <= 0:
            if self.choice >= 5:
                SCREEN.blit(self.circle, (self.x, self.y))
                self.y += boy.BOY_SPEED * 1.25
                self.catch()
                if self.y >= HEIGHT:
                    self.y = -25
                    self.time = 5000

    def catch(self):
        self.heart_rect = pygame.Rect(self.x, self.y, 32, 32)
        if self.heart_rect.colliderect(boy.BOY_RECT):
            self.y = -25
            self.time = 5000
            boy.lives += 1


class Gold:
    def __init__(self):
        self.coin_rect = None
        self.coin_y = -35
        self.coin_x = random.randint(0, WIDTH - 32)
        self.coin = pygame.transform.scale(pygame.image.load("coin.png"), (32, 32))

    def draw(self):
        SCREEN.blit(self.coin, (self.coin_x, self.coin_y))
        self.coin_rect = pygame.Rect(self.coin_x, self.coin_y, 32, 32)
        if self.coin_rect.colliderect(boy.BOY_RECT):
            boy.points += 5
            self.coin_y = HEIGHT + 10


start = DisplayText()

heart = Heart()
boy = Boy()
balls = []
gold_coins = []


def Home():
    pygame.display.set_caption("Dropper")  # set screen name/headline
    pygame.display.set_icon(boy.BOY)

    start.displayTextCenter(20, "Too start game press spacebar", (255, 0, 0))
    start.displayTextCenter(75, "DROPPER", (239, 255, 0), 100)

    while True:
        for happenings in pygame.event.get():  # check if X in top right has been clicked to end the program and update the
            # screen as needed
            if happenings.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        startup = pygame.key.get_pressed()
        if startup[K_SPACE]:
            Level()


def Level(level=1, ):
    state = 1
    heart.time = 5000
    boy.__init__(boy.points, boy.lives)
    time = 120
    balls.clear()
    gold_coins.clear()
    for i in range(5 + level):
        balls.append(Ball(i))
    while True:
        pygame.display.update()
        SCREEN.fill((0, 0, 0))
        pygame.time.Clock().tick(60)
        pygame.display.set_icon(boy.BOY)
        pygame.display.set_caption(f"Dropper: Level {level}")  # set screen name/headline

        for event in pygame.event.get():  # check if X in top right has been clicked to end the program and update the
            # screen as needed
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    state *= -1
                    start.displayTextCenter(95, "PAUSED", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        if state == 1:
            if boy.BOY_SPEED != 0:
                heart.Life()
            boy.boyMove()
            boy.displayBoy(SCREEN)

            for a in range(len(balls)):
                balls[a].ballMove()
                balls[a].collide()
                balls[a].ballDisplay(SCREEN)

            for i in gold_coins:
                if i.coin_y < HEIGHT:
                    i.coin_y += boy.BOY_SPEED * 1.25
                else:
                    gold_coins.pop(gold_coins.index(i))

        pygame.display.update()

        if boy.points >= level * 100 :
            if time > 0:
                time -= 1
                start.displayTextCenter(40, f"Stage {level} cleared.", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            level += 1
            Level(level)

            
Home()
