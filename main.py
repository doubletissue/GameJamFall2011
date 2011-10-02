from __future__ import division
import pygame
from pygame.locals import *
import math, random
import sys

from map import Map


def main():
  pygame.init()
  screen = pygame.display.set_mode((1000, 1000))
  clock = pygame.time.Clock()
  
  game_map = Map(0)
  
  while True:
    clock.tick(60)
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
        pygame.quit()
        return
    key = pygame.key.get_pressed()
    
    game_map.draw(screen)
    
    
    
    pygame.display.flip()
    
    
    #if key[K_1]:
      #Bird.difficulty = 3
    #if key[K_2]:
      #Bird.difficulty = 2.25
    #if key[K_3]:
      #Bird.difficulty = 1.5
    #if key[K_4]:
      #Bird.difficulty = 1
    #if key[K_5]:
      #Bird.difficulty = .5
    
    #if key[K_m]:


main()  