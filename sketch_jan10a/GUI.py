import pygame
import sys

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

class Sim:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.screen.fill(('#13070c'))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            print(pygame.display.get_window_size())


Sim().run() 