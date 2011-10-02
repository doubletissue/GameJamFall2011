import pygame

#Start at red, go right to the one before red.
colorwheel = [pygame.Color(255, 0, 0), pygame.Color(255, 102, 0), pygame.Color(255, 148, 0),
              pygame.Color(254, 197, 0), pygame.Color(255, 255, 0), pygame.Color(140, 199, 0),
              pygame.Color(15, 173, 0), pygame.Color(0, 163, 199), pygame.Color(0, 100, 181),
              pygame.Color(0, 16, 165), pygame.Color(99, 0, 165), pygame.Color(197, 0, 124)]

red = 0
yellow = 4
blue = 8
white = -1

def translate_color( color_id ):
  if 0 <= self.color < 12:
    return colorwheel[self.color]
  else:
    return pygame.Color( 255, 255, 255 )

class Color( object ):
  def __init__( self, color=None ):
    if( color == None ):
      color = -1
    self.color = color

  def __add__( self, other ):
    if other.color == -1:
      return self.color
    elif self.color == -1:
      return other.color
    difference = other.color - self.color
    print "Difference: ", difference
    if abs(difference) == 6:
      return white
    elif difference > 0:
      if difference < 6:
        return (other.color - (difference / 2)) % 12
      else:
        return (other.color + ((12 - difference) / 2)) % 12
    else:
      return other + self