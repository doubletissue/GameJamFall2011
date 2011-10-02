from __future__ import division
import pygame
from pygame.locals import *
import math, random
import sys

from map import Map
from character import Character

def main():
  pygame.init()
  screen = pygame.display.set_mode((1000, 1000))
  clock = pygame.time.Clock()
  
  game_map = Map()
  player = character( game_map, 0, 0 )
  
  while True:
    clock.tick(60)
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
        pygame.quit()
        return
    key = pygame.key.get_pressed()
    
    if key[K_UP]:
      pass
    elif key[K_DOWN]:
      pass
    elif key[K_LEFT]:
      pass
    elif key[K_RIGHT]:
      pass
    
    game_map.draw(screen)
    
    
    
    pygame.display.flip()


main()  