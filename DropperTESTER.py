import pygame  # import pygame, system and os to use within code
import random
import sys
from pygame.locals import *  # remove the need to type pygame.local

pygame.init()  # start/initialize pygame
lies = False
while not lies:
    for event in pygame.event.get():  # check if X in top right has been clicked to end the program and update the
        # screen as needed
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Dropper")  # set screen name/headline
    font_S = pygame.font.Font("freesansbold.ttf", 20)
    start = font_S.render("Too start game press spacebar", True, (255, 0, 0))
    startRect = start.get_rect()
    startRect.center = (200, 300)
    SCREEN.blit(start, startRect)
    pygame.display.update()

    startup = pygame.key.get_pressed()
    if startup[K_SPACE]:
        lies = True

# def gold():


BOY_WIDTH = 50
BOY_HEIGHT = 50
BOY_X = 175
BOY_Y = 500

BOY_SPEED = 0.5

BALL_WIDTH = 50
BALL_HEIGHT = 50

BALL_X1 = 150
BALL_Y1 = 10
BALL_DIRECTION1 = random.randint(1, 10) / 10

BALL_X2 = 150
BALL_Y2 = 10
BALL_DIRECTION2 = random.randint(1, 10) / 10

BALL_X3 = 150
BALL_Y3 = 10
BALL_DIRECTION3 = random.randint(1, 10) / 10

BALL_X4 = 150
BALL_Y4 = 10
BALL_DIRECTION4 = random.randint(1, 10) / 10

BALL_X5 = 150
BALL_Y5 = 10
BALL_DIRECTION5 = random.randint(1, 10) / 10

BOY = pygame.transform.scale(pygame.image.load("Dropper\\boy.png"), (BOY_WIDTH, BOY_HEIGHT))
BALL1 = pygame.transform.scale(pygame.image.load("Dropper\\bowling-ball.png"), (BALL_WIDTH, BALL_HEIGHT))
BALL2 = pygame.transform.scale(pygame.image.load("Dropper\\bowling-ball.png"), (BALL_WIDTH, BALL_HEIGHT))
BALL3 = pygame.transform.scale(pygame.image.load("Dropper\\bowling-ball.png"), (BALL_WIDTH, BALL_HEIGHT))
BALL4 = pygame.transform.scale(pygame.image.load("Dropper\\bowling-ball.png"), (BALL_WIDTH, BALL_HEIGHT))
BALL5 = pygame.transform.scale(pygame.image.load("Dropper\\bowling-ball.png"), (BALL_WIDTH, BALL_HEIGHT))

points = 0
life = 3
counter = 500
invincible = 0

while True:
    for event in pygame.event.get():  # check if X in top right has been clicked to end the program and update the
        # screen as needed
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_icon(BOY)
    SCREEN = pygame.display.set_mode((400, 600))  # set screen/display size

    SCREEN.blit(BOY, (BOY_X, BOY_Y))

    if BALL_Y1 < 600:
        SCREEN.blit(BALL1, (BALL_X1, BALL_Y1))
        BALL_Y1 = BALL_Y1 + BALL_DIRECTION1
    else:
        BALL_X1 = random.randint(0, 350)
        BALL_Y1 = 10
        BALL_DIRECTION1 = BALL_DIRECTION1 + random.randint(1, 10) / 100
        points += 1

    if BALL_Y2 < 600:
        SCREEN.blit(BALL2, (BALL_X2, BALL_Y2))
        BALL_Y2 = BALL_Y2 + BALL_DIRECTION2
    else:
        BALL_X2 = random.randint(0, 350)
        BALL_Y2 = 10
        BALL_DIRECTION2 = BALL_DIRECTION2 + random.randint(1, 10) / 100
        points += 1

    if BALL_Y3 < 600:
        SCREEN.blit(BALL3, (BALL_X3, BALL_Y3))
        BALL_Y3 = BALL_Y3 + BALL_DIRECTION3
    else:
        BALL_X3 = random.randint(0, 350)
        BALL_Y3 = 10
        BALL_DIRECTION3 = BALL_DIRECTION3 + random.randint(1, 10) / 100
        points += 1

    if BALL_Y4 < 600:
        SCREEN.blit(BALL4, (BALL_X4, BALL_Y4))
        BALL_Y4 = BALL_Y4 + BALL_DIRECTION4
    else:
        BALL_X4 = random.randint(0, 350)
        BALL_Y4 = 10
        BALL_DIRECTION4 = BALL_DIRECTION4 + random.randint(1, 10) / 100
        points += 1

    if BALL_Y5 < 600:
        SCREEN.blit(BALL5, (BALL_X5, BALL_Y5))
        BALL_Y5 = BALL_Y5 + BALL_DIRECTION5
    else:
        BALL_X5 = random.randint(0, 350)
        BALL_Y5 = 10
        BALL_DIRECTION5 = BALL_DIRECTION5 + random.randint(1, 10) / 100
        points += 1

    MOVE = pygame.key.get_pressed()

    if MOVE[pygame.K_LEFT] and BOY_X > 0:
        BOY_X -= BOY_SPEED
    if MOVE[pygame.K_RIGHT] and BOY_X < 350:
        BOY_X += BOY_SPEED
    if MOVE[pygame.K_UP] and BOY_Y > 0:
        BOY_Y -= BOY_SPEED
    if MOVE[pygame.K_DOWN] and BOY_Y < 550:
        BOY_Y += BOY_SPEED

    BALL_RECT1 = pygame.Rect(BALL_X1, BALL_Y1, BALL_WIDTH - 20, BALL_HEIGHT)
    BALL_RECT2 = pygame.Rect(BALL_X2, BALL_Y2, BALL_WIDTH - 20, BALL_HEIGHT)
    BALL_RECT3 = pygame.Rect(BALL_X3, BALL_Y3, BALL_WIDTH - 20, BALL_HEIGHT)
    BALL_RECT4 = pygame.Rect(BALL_X4, BALL_Y4, BALL_WIDTH - 20, BALL_HEIGHT)
    BALL_RECT5 = pygame.Rect(BALL_X5, BALL_Y5, BALL_WIDTH - 20, BALL_HEIGHT)
    BOY_RECT = pygame.Rect(BOY_X, BOY_Y, BOY_WIDTH - 20, BOY_HEIGHT)

    font_s = pygame.font.Font("freesansbold.ttf", 15)
    score = font_s.render("SCORE: " + str(points), True, (255, 255, 255))
    scoreRect = score.get_rect()
    scoreRect.center = (35, 25)
    SCREEN.blit(score, scoreRect)

    font_l = pygame.font.Font("freesansbold.ttf", 15)
    life_c = font_l.render("LIFE: " + str(life), True, (255, 255, 255))
    lifeRect = life_c.get_rect()
    lifeRect.center = (35, 40)
    SCREEN.blit(life_c, lifeRect)

    if invincible > 0:
        invincible -= 1
        font_i = pygame.font.Font("freesansbold.ttf", 15)
        invin = font_i.render("invincibility :" + str(invincible), True, (255, 255, 255))
        invinRect = invin.get_rect()
        invinRect.center = (60, 570)
        SCREEN.blit(invin, invinRect)

    elif BALL_RECT1.colliderect(BOY_RECT) or BALL_RECT2.colliderect(BOY_RECT) or BALL_RECT3.colliderect(
            BOY_RECT) or BALL_RECT4.colliderect(BOY_RECT) or BALL_RECT5.colliderect(BOY_RECT):

        if life == 0:
            BOY_SPEED = 0
            BALL_DIRECTION1 = 0
            BALL_DIRECTION2 = 0
            BALL_DIRECTION3 = 0
            BALL_DIRECTION4 = 0
            BALL_DIRECTION5 = 0
            font = pygame.font.Font("freesansbold.ttf", 40)
            text = font.render("GAME OVER", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (400 // 2, 600 // 2)
            score = font_s.render("SCORE: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (35, 25)
            font_f = pygame.font.Font("freesansbold.ttf", 35)
            final_s = font_f.render("FINAL SCORE: " + str(points), True, (255, 255, 255))
            finalRect = final_s.get_rect()
            finalRect.center = (400 // 2, 600 // 2 + 40)
            SCREEN.blit(text, textRect)
            SCREEN.blit(score, scoreRect)
            SCREEN.blit(final_s, finalRect)
            # restart
            font_r = pygame.font.Font("freesansbold.ttf", 20)
            restart = font_r.render("Too restart game press spacebar", True, (255, 255, 255))
            restartRect = restart.get_rect()
            restartRect.center = (400 // 2, 400)
            SCREEN.blit(restart, restartRect)
            if MOVE[pygame.K_SPACE]:
                BOY_X = 175
                BOY_Y = 500

                BOY_SPEED = 0.5

                BALL_WIDTH = 50
                BALL_HEIGHT = 50

                BALL_X1 = 150
                BALL_Y1 = 10
                BALL_DIRECTION1 = random.randint(1, 10) / 10

                BALL_X2 = 150
                BALL_Y2 = 10
                BALL_DIRECTION2 = random.randint(1, 10) / 10

                BALL_X3 = 150
                BALL_Y3 = 10
                BALL_DIRECTION3 = random.randint(1, 10) / 10

                BALL_X4 = 150
                BALL_Y4 = 10
                BALL_DIRECTION4 = random.randint(1, 10) / 10

                BALL_X5 = 150
                BALL_Y5 = 10
                BALL_DIRECTION5 = random.randint(1, 10) / 10

                points = 0
                life = 3
                counter = 500

        else:
            life = life - 1
            BOY_X = 175
            BOY_Y = 500
            invincible = 150

    counter = counter - 1
    if counter == 0:
        BOY_SPEED = BOY_SPEED + 0.01
        counter = 100

    pygame.display.update()
