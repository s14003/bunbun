import random,pygame,sys
from pygame.locals import *

FPS = 25
windowWidth =640
windowHeight = 480
boxsize = 20
boadwidth = 10
boadheight = 20
blank='.'

movesidewaysfreq = 0.15
movedownfreq = 0.1

xmargin = int((windowWidth - boadwidth * boxsize)/2)
topmargin = windowHeight - (boadheight*boxsize)-5

white = (255,255,255)
gray = (185,185,185)
black = (  0, 0, 0)
red = (255, 0, 0)
lightred = (175,20,20)
green = (0,255, 0)
lightgreen = (20, 175, 20)
blue = ( 0, 0,255)
lightblue = (20, 20, 175)
yellow = (255, 255, 0)
lightyellow = (175,175,20)

boadercolor = blue
bgcolor = black
textcolor = white
textshadowcolor = gray
colors = (blue, green, red, yellow)
lightcolors=(lightblue,lightgreen,lightred,lightyellow)
assert len(colors) == len(lightcolors)

templateWidth = 5
templateHeight = 5

s_shape_template = [['.....',
                     '.....',
                     '..○○.',
                     '.○○..',
                     '.....'],
                    ['.....',
                     '..○..',
                     '..○○.',
                     '...○.',
                     '.....']]

z_shape_template = [['.....',
                     '.....',
                     '.○○..',
                     '..○○..',
                     '.....'],
                    ['.....',
                     '..○..',
                     '.○○..',
                     '.○...',
                     '.....']]

i_shape_template = [['..○..',
                     '..○..',
                     '..○..',
                     '..○..',
                     '.....'],
                    ['.....',
                     '.....',
                     '○○○○.',
                     '.....',
                     '.....']]

o_shape_template = [['.....',
                     '.....',
                     '.○○..',
                     '.○○..',
                     '.....']]

j_shape_template = [['.....',
                     '.○...',
                     '.○○○.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..○○.',
                     '..○..',
                     '..○..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.○○○.',
                     '...○.',
                     '.....'],
                    ['.....',
                     '..○..',
                     '..○..',
                     '.○○..',
                     '.....']]

t_shape_template = [['.....',
                     '..○..',
                     '.○○○.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..○..',
                     '..○○.',
                     '..○..',
                     '.....'],
                    ['.....',
                     '.○○○.',
                     '..○..',
                     '.....'],
                    ['.....',
                     '..○..',
                     '.○○..',
                     '..○..',
                     '.....']]

l_shape_template = [['.....',
                     '...○.',
                     '.○○○.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..○..',
                     '..○..',
                     '..○○.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.○○○.',
                     '.○...',
                     '.....'],
                    ['.....',
                     '.○○..',
                     '..○..',
                     '..○..',
                     '.....']]

shapes = {'S':s_shape_template,
          'Z':z_shape_template,
          'L':l_shape_template,
          'I':i_shape_template,
          'O':o_shape_template,
          'T':t_shape_template}

def main():
    global fpsclock,displaysurf,basicfont,bigfont
    pygame.init()
    fpsclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((windowWidth,windowHeight))
    basicfont = pygame.font.Font('freesansbold.ttf',18)
    bigfont = pygame.font.Font('freesansbold.ttf',100)
    pygame.display.set_caption('Tetromino')

def runGame():
    movingDown = False
    movingLeft = False
    score = 0


    