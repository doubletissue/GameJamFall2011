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
    
    if key[K_up]:
      pass
    elif key[K_down]:
      pass
    elif key[K_left]:
      pass
    elif key[K_right]:
      pass
    
    game_map.draw(screen)
    
    
    
    pygame.display.flip()


main()  