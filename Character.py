from Color import Color

class Character(object):
  def __init__( self, world, x, y ):
    self.world = world
    self.position = complex( x, y )
    self.color = Color()

  def move( self, direction ):
    new_position = self.position + direction
    if world.walkable( new_position.re, new_position.im, self.color ):
      self.position = new_position

  def move_up( self ):
    self.move( self, complex(0,-1) )

  def move_down( self ):
    self.move( self, complex(0,1) )

  def move_left( self ):
    self.move( self, complex(1,0) )

  def move_right( self ):
    self.move( self, complex(-1,0) )