import pygame
from color import Color
from map import Map

up = complex(0,-1)
down = complex(0,1)
right = complex(1,0)
left = complex(-1,0)
model_up = pygame.image.load(os.path.join("Art","player_up.png"))
model_down = pygame.image.load(os.path.join("Art","player_down.png"))
model_right= pygame.image.load(os.path.join("Art","player_right.png"))
model_left = pygame.image.load(os.path.join("Art","player_left.png"))
models = {up:model_up, down:model_down, left:model_right, right:model_left}

class Character(object):
  def __init__( self, world, x, y ):
    self.world = world
    self.position = complex( x, y )
    self.color = Color()
    self.model = model_down

  def draw( self, screen ):
    screen.blit( self.image, (self.position.real*25, self.position.imag*25) )

  def move( self, direction ):
    self.model = models[direction]
    new_position = self.position + direction
    if world.walkable( new_position.real, new_position.imag, self.color ):
      self.position = new_position

  def attack( self, direction ):
    attack_position = self.position + direction
    self.color = world.hit( attack_position.re, attack_position.im, self.color ) + self.color

  def move_up( self ):
    self.move( self, up )

  def move_down( self ):
    self.move( self, down )

  def move_left( self ):
    self.move( self, left )

  def move_right( self ):
    self.move( self, right )

  def attack_up( self ):
    self.attack( self, up )

  def attack_down( self ):
    self.attack( self, down )

  def attack_left( self ):
    self.attack( self, left )

  def attack_right( self ):
    self.attack( self, right )