from __future__ import division
import math, random, os
import pygame

colors = range(12)

images = [
            pygame.image.load(os.path.join("Art","apple.png")),
            pygame.image.load(os.path.join("Art","circlebanana.png")),
            pygame.image.load(os.path.join("Art","giantblueberry.png"))
         ]

class Item:
  
  def __init__(self, type_id):
    self.color = colors[type_id]
    self.image = images[type_id]
  
  def draw(self,screen,pos):
    screen.blit(self.image,pos)
  