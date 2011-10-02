from __future__ import division
import pygame
from pygame.locals import *
import math, random
import sys,os

from map import Map
from character import Character
from menu import Menu

winScreen = pygame.image.load(os.path.join("Art","Main Menu", "winscreen.png"))
pauseScreen = pygame.image.load(os.path.join("Art","Main Menu", "winscreen.png"))

def main():
  pygame.init()
  screen = pygame.display.set_mode((1000, 1000))
  clock = pygame.time.Clock()
  
  game_map = Map(0)
  player = Character( game_map, 23, 1 )
  
  prevKeys = {}
  
  menu = Menu()
  while True:
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
        pygame.quit()
        return
    key = pygame.key.get_pressed()
    
    if key[K_DOWN] and not prevKeys[K_DOWN]:
      menu.move(1)
    if key[K_UP] and not prevKeys[K_UP]:
      menu.move(-1)
    if key[K_RETURN] and not prevKeys[K_RETURN]:
      r = menu.select()
      if r == -1:
        pygame.quit()
        return
      elif r == 1:
        break
        
    prevKeys = key
    
    menu.draw(screen)
    pygame.display.flip()
    
  
  while True:
    
    clock.tick(30)
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
        pygame.quit()
        return
    key = pygame.key.get_pressed()
    
    if key[K_LSHIFT]:
      if key[K_UP] and not prevKeys[K_UP]:
        player.attack_up()
      elif key[K_DOWN] and not prevKeys[K_DOWN]:
        player.attack_down()
      elif key[K_LEFT] and not prevKeys[K_LEFT]:
        player.attack_left()
      elif key[K_RIGHT] and not prevKeys[K_RIGHT]:
        player.attack_right()
    else:
      if key[K_UP] and not prevKeys[K_UP]:
        player.move_up()
      elif key[K_DOWN] and not prevKeys[K_DOWN]:
        player.move_down()
      elif key[K_LEFT] and not prevKeys[K_LEFT]:
        player.move_left()
      elif key[K_RIGHT] and not prevKeys[K_RIGHT]:
        player.move_right()
    
    while game_map.isWin(player.position.real, player.position.imag):
      screen.blit(winScreen,(0,0))
      pygame.display.flip()
      for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
          pygame.quit()
          return
    
    prevKeys = key
    game_map.draw(screen)
    player.draw(screen)
    
    
    
    pygame.display.flip()


main()  