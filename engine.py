import sys
import pygame

class Engine():
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.running = True
    
    def start(self):
        self.running = True

    def stop(self):
        self.running = False
        
    def run(self):
        while self.running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

        pygame.display.flip()