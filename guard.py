import os
import pygame
from color import mix_colors, white
from map import Map

up = complex(0,-1)
down = complex(0,1)
right = complex(1,0)
left = complex(-1,0)

model_up = pygame.image.load(os.path.join("Art","player_up.png"))
model_down = pygame.image.load(os.path.join("Art","player_down.png"))
model_right= pygame.image.load(os.path.join("Art","player_right.png"))
model_left = pygame.image.load(os.path.join("Art","player_left.png"))
models = {up:model_up, down:model_down, right:model_right, left:model_left}

#models_up = [pygame.image.load(os.path.join("Art","player_u_" + str(i) + ".png")) for i in range(12) + [-1] ]
#models_down = [pygame.image.load(os.path.join("Art","player_d_" + str(i) + ".png")) for i in range(12) + [-1] ]
#models_left = [pygame.image.load(os.path.join("Art","player_l_" + str(i) + ".png")) for i in range(12) + [-1] ]
#models_right = [pygame.image.load(os.path.join("Art","player_r_" + str(i) + ".png")) for i in range(12) + [-1] ]
#models = {up:models_up, down:models_down, right:models_right, left:models_left}

class Guard(object):
  def __init__( self, world, x, y ):
    self.world = world
    self.position = complex( x, y )
    self.color = white
    self.model = model_down

  def draw( self, screen ):
    screen.blit( self.model, (self.position.real*40, self.position.imag*40) )

  def move( self, direction ):
    #self.model = models[direction][self.color]
    self.model = models[direction]
    new_position = self.position + direction
    if self.world.walkable( int(new_position.real), int(new_position.imag), self.color ):
      self.position = new_position

  def attack( self, direction ):
    #self.model = models[direction][self.color]
    self.model = models[direction]
    attack_position = self.position + direction
    self.color = mix_colors( self.color, self.world.hit( int(attack_position.real), int(attack_position.imag) ) )

  def move_up( self ):
    self.move( up )

  def move_down( self ):
    self.move( down )

  def move_left( self ):
    self.move( left )

  def move_right( self ):
    self.move( right )

  def attack_up( self ):
    self.attack( up )

  def attack_down( self ):
    self.attack( down )

  def attack_left( self ):
    self.attack( left )

  def attack_right( self ):
    self.attack( right )