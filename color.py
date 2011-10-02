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
  if 0 <= color_id < 12:
    return colorwheel[color_id]
  else:
    return pygame.Color( 255, 255, 255 )

def mix_colors( first, second ):
  if second == -1 or first == second:
    return first
  elif first == -1:
    return second
  else:
    difference = second - first
    if abs(difference) in [1,11]:
      return second
    if abs(difference) == 6:
      return white
    elif difference > 0:
      if difference < 6:
        return (second - (difference / 2)) % 12
      else:
        return (second + ((12 - difference) / 2)) % 12
    else:
      return mix_colors( second, first )