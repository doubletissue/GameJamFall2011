from __future__ import division
import math, random, os
import pygame

colors = range(12)

images = [ [ pygame.image.load(os.path.join("Art","Items", str(j) + "_" + str(i) + ".png")) for i in range(4) ] for j in range(12) ]

class Item:
  
  def __init__(self, type_id):
    self.color = colors[type_id]
    self.image = images[type_id]
    self.health = 3
  
  def draw(self,screen,pos):
    screen.blit(self.image[self.health],pos)
    
  def hit(self):
    if self.health == 0:
      return False
    self.health -= 1
    if self.health == 0:
      return True
    return False    