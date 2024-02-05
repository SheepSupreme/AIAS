import pygame
import sys

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

class Sim:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.RESIZABLE)
    self.clock = pygame.time.Clock() 
    self.slider = pygame.Rect(50,50,400,50)
    self.dimension = (0,0)

  def run(self):
    while True:
      self.screen.fill(('#13070c'))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      
      self.slider = pygame.Rect(50,50,self.dimension[0]-100,50)
      pygame.draw.rect(self.screen,("#86A5D9"),self.slider)
      pygame.display.update()
      self.dimension = pygame.display.get_window_size()
      self.clock.tick(60)  

Sim().run()

