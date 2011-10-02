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
  
  game_map = Map(0)
  player = Character( game_map, 1, 1 )
  
  while True:
    clock.tick(60)
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
        pygame.quit()
        return
    key = pygame.key.get_pressed()
    
    if key[K_LSHIFT]:
      if key[K_UP]:
        player.attack_up()
      elif key[K_DOWN]:
        player.attack_down()
      elif key[K_LEFT]:
        player.attack_left()
      elif key[K_RIGHT]:
        player.attack_right()
    else:
      if key[K_UP]:
        player.move_up()
      elif key[K_DOWN]:
        player.move_down()
      elif key[K_LEFT]:
        player.move_left()
      elif key[K_RIGHT]:
        player.move_right()
      
    game_map.draw(screen)
    player.draw(screen)
    
    
    
    pygame.display.flip()


main()  