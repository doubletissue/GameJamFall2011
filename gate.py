from color import mix_colors
import pygame
import os

animation_scale = 100

def load_gate( color, position, phase ):
  return pygame.image.load(os.path.join("Art","Gates","gate_" + str(color) +  "_" + str(position) + str(phase) + ".png"))

models_left = [[load_gate(color, "L", phase) for phase in range(1,4)] for color in range(0,12,2) ]
models_right = [[load_gate(color, "R", phase) for phase in range(1,4)] for color in range(0,12,2) ]
models_up = [[pygame.transform.rotate( load_gate(color, "L", phase), -90 ) for phase in range(1,4)] for color in range(0,12,2) ]
models_down = [[pygame.transform.rotate( load_gate(color, "R", phase), -90 ) for phase in range(1,4)] for color in range(0,12,2) ]

models = [models_left, models_up, models_right, models_down]

class Gate( object ):
  def __init__( self, position, color, orientation ):
    self.position = position
    self.color = color
    self.phase = 0
    self.model = models[orientation][color / 2]

  def check_color( self, color ):
    return mix_colors( self.color, color ) == color

  def draw( self, screen ):
    screen.blit( self.model[phase/animation_scale], self.position )
    self.phase = (self.phase + 1) % 3*animation_scale