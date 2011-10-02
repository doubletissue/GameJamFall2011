from __future__ import division
import math, random, os
import pygame

from item import Item
from gate import Gate


corner_image          = pygame.image.load(os.path.join("Art","walls and gates", "wallcorner.png"))
wall_chart_image      = pygame.image.load(os.path.join("Art","walls and gates", "wallchart.png"))
wall_clock_image      = pygame.image.load(os.path.join("Art","walls and gates", "wallclock.png"))
wall_plain_image      = pygame.image.load(os.path.join("Art","walls and gates", "wallplain.png"))
wall_sale_image       = pygame.image.load(os.path.join("Art","walls and gates", "wallsale.png"))
floor_image           = pygame.image.load(os.path.join("Art","floortile.png"))
shelf_image           = pygame.image.load(os.path.join("Art","shelf.png"))
red_floor_image       = pygame.image.load(os.path.join("Art","walls and gates","tile.png"))
green_floor_image     = pygame.image.load(os.path.join("Art","walls and gates","tile.png"))
blue_floor_image      = pygame.image.load(os.path.join("Art","walls and gates","tile.png"))
purple_floor_image    = pygame.image.load(os.path.join("Art","walls and gates","tile.png"))
yellow_floor_image    = pygame.image.load(os.path.join("Art","walls and gates","tile.png"))
zot_image             = pygame.image.load(os.path.join("Art","ZOT.png"))


wall_dist = [1,1,1,1,1,1,1,1,1,1,1,2,3,3,4,4]

images = {
          2 :                          corner_image,
          3 : pygame.transform.rotate( corner_image, 90  ),
          4 : pygame.transform.rotate( corner_image, 180 ),
          1 : pygame.transform.rotate( corner_image, 270 ),
          
          141 :                          wall_plain_image,
          111 : pygame.transform.rotate( wall_plain_image, 90  ),
          121 : pygame.transform.rotate( wall_plain_image, 180 ),
          131 : pygame.transform.rotate( wall_plain_image, 270 ),
          
          142 :                          wall_clock_image,
          112 : pygame.transform.rotate( wall_clock_image, 90  ),
          122 : pygame.transform.rotate( wall_clock_image, 180 ),
          132 : pygame.transform.rotate( wall_clock_image, 270 ),
          
          143 :                          wall_chart_image,
          113 : pygame.transform.rotate( wall_chart_image, 90  ),
          123 : pygame.transform.rotate( wall_chart_image, 180 ),
          133 : pygame.transform.rotate( wall_chart_image, 270 ),
          
          144 :                          wall_sale_image,
          114 : pygame.transform.rotate( wall_sale_image, 90  ),
          124 : pygame.transform.rotate( wall_sale_image, 180 ),
          134 : pygame.transform.rotate( wall_sale_image, 270 ),
          
          21 : green_floor_image,
          22 : red_floor_image,
          23 : blue_floor_image,
          24 : yellow_floor_image,
          25 : purple_floor_image,
          
          30 : shelf_image
        }
        
shelf_maps = [
              [
                [ 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ],
                [ 00, 00, 00, 00, 00, 00, 00, 00, 00, 50, 00, 00 ,54 ,00 ,00 ,00 ,00 ,00 ,52 ,00 ,00 ,54 ,00 ,00 ,00 ],
                [ 00, 00, 00, 00, 00, 00, 00, 00, 00, 70, 00, 00 ,74 ,00 ,00 ,00 ,00 ,00 ,72 ,00 ,00 ,74 ,00 ,00 ,00 ],
                [ 00, 63, 83, 30, 60, 80, 30, 00, 00, 30, 61, 81 ,30 ,00 ,00 ,37 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,42 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 34, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 34, 00, 00, 30, 00, 00, 30, 00, 00 ,31 ,00 ,00 ,39 ,00 ,00 ,41 ,00 ,00 ,33 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 31, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 37, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,40 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,38 ,00 ,00 ,00 ],
                [ 00, 00, 00, 39, 00, 00, 30, 61, 81, 30, 00, 00 ,30 ,00 ,00 ,30 ,64 ,84 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 30, 00, 00 ,39 ,00 ,00 ,30 ,00 ,00 ,31 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 32, 00, 00 ,30 ,00 ,00 ,42 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 40, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 35, 00, 00, 30, 00, 00, 30, 00, 00 ,36 ,00 ,00 ,30 ,00 ,00 ,36 ,00 ,00 ,39 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 33, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 35, 00, 00, 30, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,39 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 41, 00, 00, 30, 00, 00, 30, 00, 00 ,32 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 35, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,38 ,00 ,00 ,31 ,00 ,00 ,00 ],
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],  # 5 = down, 6 right, 7 up, 8 left
                [ 00, 00, 00, 30, 00, 00, 30, 00, 00, 30, 00, 00 ,30 ,00 ,00 ,34 ,00 ,00 ,30 ,00 ,00 ,30 ,00 ,00 ,00 ],  # color is number multiplied by 2
                [ 00, 00, 00, 50, 00, 00, 00, 00, 00, 00, 00, 00 ,53 ,00 ,00 ,00 ,00 ,00 ,55 ,00 ,00 ,52 ,00 ,00 ,00 ],
                [ 00, 00, 00, 70, 00, 00, 00, 00, 00, 00, 00, 00 ,73 ,00 ,00 ,00 ,00 ,00 ,75 ,00 ,00 ,72 ,00 ,00 ,00 ],
                [ 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ,00 ]
              ]
            ]
          
    
def generateFloor(num_points,xLim,yLim):
  m = {}
  queue = []
  pos = 0
  for i in range(num_points):
    p = (random.randint(0,xLim-1),random.randint(0,yLim-1) )
    while p in queue:
      p = (random.randint(0,xLim-1),random.randint(0,yLim-1) )
    queue.append( (p,i) )
  while pos < len(queue):
    (x,y),c = queue[pos]
    if (x,y) in m:
      pos += 1
      continue
    m[ (x,y) ] = c
    if (x+1,y) not in queue and (x+1,y) not in m and x+1 < xLim:
      queue.append( ((x+1,y), c) )
    if (x-1,y) not in queue and (x-1,y) not in m and x-1 >= 0:
      queue.append( ((x-1,y), c) )
    if (x,y+1) not in queue and (x,y+1) not in m and y+1 < yLim:
      queue.append( ((x,y+1), c) )
    if (x,y-1) not in queue and (x,y-1) not in m and y-1 >= 0:
      queue.append( ((x,y-1), c) )
  return m

def floorPatternToKey(n):
  if n == 0:
    return 21
  if n == 1:
    return 22
  if n == 2:
    return 23
  if n == 3:
    return 24
  if n == 4:
    return 25



class Map:
  
  def __init__(self, level):
    self.shelves = shelf_maps[level]
    self.tiles = {}
    self.gate = {}
    floor_pattern = generateFloor(20,25,25)
    for x in range(25):
      self.tiles[x]={}
      for y in range(25):
        
        if   x is 0 and y is 0:
          self.tiles[x][y] = 01
        elif x is 0 and y is 24:
          self.tiles[x][y] = 02
        elif x is 0:
          r = 110 + random.choice(wall_dist)
          self.tiles[x][y] = r
        
        elif x is 24 and y is 0:
          self.tiles[x][y] = 04
        elif x is 24 and y is 24:
          self.tiles[x][y] = 03
        elif x is 24:
          r = 130 + random.choice(wall_dist)
          self.tiles[x][y] = r
        
        elif y is 0:
          r = 140 + random.choice(wall_dist)
          self.tiles[x][y] = r
        elif y is 24:
          r = 120 + random.choice(wall_dist)
          self.tiles[x][y] = r
        else:
          self.tiles[x][y] = floorPatternToKey(floor_pattern[ (x,y) ]%5 ) 
        
    
    
    self.items = {}
    for x in range(25):
      for y in range(25):
        if   self.shelves[x][y] > 30 and self.shelves[x][y] < 50:
          self.items[ (x,y) ] = Item(self.shelves[x][y]-31)
        
        if self.shelves[x][y] >= 50 and self.shelves[x][y] < 100:
            
          self.gate[ (x,y) ] = Gate((x*40,y*40),(self.shelves[x][y]%10) * 2, (self.shelves[x][y]-50)//10)
  
  def isWin(self,x,y):
    return x==23 and y==23
  
  def walkable(self,x,y,color):
    if (x,y) in self.gate and self.gate[ (x,y) ].check_color(color):
      return True
    elif (x,y) in self.gate:
      self.screen.blit(pygame.image.load(os.path.join("Art","Main Menu","losescreen.png")), (0,0))
      pygame.display.flip()
      while True:
        for e in pygame.event.get():
          if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            pygame.quit()
            return
    return self.tiles[x][y] >= 20 and self.tiles[x][y] < 30 and self.shelves[x][y] == 0
  
  def hit(self,x,y):
    if not (x,y) in self.items:
      return -1
    dead = self.items[ (x,y) ].hit()
    if not dead:
      return -1
    return self.items[ (x,y) ].color
        
  
  def getShelfImage(self,x,y):
    if self.shelves[x][y] >= 30 and self.shelves[x][y] < 50:
      return images[30]
    return None
    
  def getTileImage(self,x,y):
    return images[self.tiles[x][y]]
    
  def getDrawPos(self,x,y):
    return (x*40,y*40)
    
  def draw(self,screen):
    self.screen = screen
    for x in range(25):
      for y in range(25):
        screen.blit(self.getTileImage(x,y),self.getDrawPos(x,y))
        shelf_image = self.getShelfImage(x,y)
        if shelf_image:
          screen.blit(shelf_image,self.getDrawPos(x,y))
        if (x,y) in self.items:
          self.items[ (x,y) ].draw(screen, (x*40,y*40) )
        if (x,y) in self.gate:
          self.gate[ (x,y) ].draw(screen)
    screen.blit(zot_image,(23*40,23*40))
          
  