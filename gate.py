from color import mix_colors
import pygame
import os

#models_up_down = [pygame.image.load(os.path.join("Art","gate_ud_" + str(i) + ".png")) for i in range(0,12,2) ]
#models_left_right = [pygame.image.load(os.path.join("Art","gate_lr_" + str(i) + ".png")) for i in range(0,12,2)]

models_up_down = [pygame.image.load(os.path.join("Art","player_up.png")) for i in range(0,12,2) ]
models_left_right = [pygame.image.load(os.path.join("Art","player_left.png")) for i in range(0,12,2)]

models = {"ud":models_up_down, "lr":models_left_right}

class Gate( object ):
  def __init__( self, color, x, y, orientation ):
    self.color = color
    self.position = complex( x, y )
    self.orientation = orientation
    self.model = self.get_model()

  def get_model( self ):
    self.model = models[self.orientation][self.color / 2]

  def none_shall_pass( self, color ):
    return mix_colors( self.color, color ) == color

  def draw( screen ):
    screen.blit( self.model, (self.position.real*40, self.position.imag*40) )