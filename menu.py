from __future__ import division
import math, random, os
import pygame

class Menu:
  
  def __init__(self):
    self.images = [
                    pygame.image.load(os.path.join("Art","Main Menu","1.png")),
                    pygame.image.load(os.path.join("Art","Main Menu","2.png")),
                    pygame.image.load(os.path.join("Art","Main Menu","3.png")),
                    pygame.image.load(os.path.join("Art","Main Menu","4.png"))
                  ]
    self.state = 0
    
  def move(self,direction):
    if direction == 1:
      self.state += 1
    if direction == -1:
      self.state -= 1
    if self.state < 0:
      self.state = 3
    if self.state > 3:
      self.state = 0
  
  def draw(self,screen):
    screen.blit(self.images[self.state],(0,0))
  
  def select(self):
    if self.state == 0:
      return 1
    if self.state == 3:
      return -1