import sys
import pygame

class Engine():
    def __init__(self, screenWidth, screenHeight):
        pygame.init()

        size = screenWidth, screenHeight
        speed = 3
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)

        ball = pygame.image.load("ayy.png")
        ballrect = ball.get_rect()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                
                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_LEFT:
                        #ballrect = ballrect.move([-1,0])
                    #if event.key == pygame.K_RIGHT:
                        #ballrect = ballrect.move([1,0])

            keys = pygame.key.get_pressed()  #checking pressed keys
            if keys[pygame.K_LEFT]:
                if ballrect.left > 0:
                    ballrect = ballrect.move([-speed,0])
            elif keys[pygame.K_RIGHT]:
                if ballrect.right < screenWidth:
                    ballrect = ballrect.move([speed,0])
            elif keys[pygame.K_UP]:
                if ballrect.top > 0:
                    ballrect = ballrect.move([0,-speed])
            elif keys[pygame.K_DOWN]:
                if ballrect.bottom < screenHeight:
                    ballrect = ballrect.move([0,speed])
            else: 
                print: "no key"

            #ballrect = ballrect.move(speed)
            #if ballrect.left < 0 or ballrect.right > screenWidth:
                #speed[0] = -speed[0]
            #if ballrect.top < 0 or ballrect.bottom > screenHeight:
                #speed[1] = -speed[1]

            screen.fill(black)
            screen.blit(ball, ballrect)
            pygame.display.flip()
