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
      character.move_up()
    elif key[K_DOWN]:
      character.move_down()
    elif key[K_LEFT]:
      character.move_left()
    elif key[K_RIGHT]:
      character.move_right()
    
    game_map.draw(screen)
    
    
    
    pygame.display.flip()


main()  