import pygame as linx
# from std.oil import *
from pygame.locals import *

import sys

def rgb(r,g,b):
    return (r,g,b)

def hex(val):
    return "#" + val

class Hoist():
    def __init__(self, title, width, height, mods=(DOUBLEBUF)):
        self.width = width
        self.height = height
        self.title = title
        linx.init()
        self.screen = linx.display.set_mode((width,height),flags=mods)
        linx.display.set_caption(title)
        linx.event.set_allowed([QUIT])
        self.primary_surface = self.screen
        self.sprites = linx.sprite.Group()
        self.active = True

    def __call__(self):
        return self.screen
    
    def vec(self, iterable):
        return linx.sprite.Group(iterable)
    
    def nvec(self):
        return linx.sprite.Group()
    
    
    # fonts
    def font(self, filename, fontsize):
        return linx.font.Font(filename, fontsize)
    
    def systemfont(self, name, fontsize):
        return linx.font.SysFont(name, fontsize)
    
    def setprimary(self, surface):
        self.primary_surface = surface

    def color(value):
        return linx.Color(value)

    def text(self, content, font, color, x, y, antialias=True):
        text_surface = font.render(content, antialias, color)
        self.primary_surface.blit(text_surface, (x, y))

    def image(self, filename):
        return linx.image.load(filename).convert_alpha()

    def imagef(self, filename):
        return linx.image.load(filename).convert()
    
    def imageraw(self, filename):
        return linx.image.load(filename)
    
    def imagerect(self, length, width):
        return linx.Surface((length, width))
    
    def draw(self, image, pos):
        self.primary_surface.blit(image, pos)

    def drawtoscreen(self, image, pos):
        self.screen.blit(image, pos)


    
    def pricol(self, color):
        self.primary_surface.fill(color)

    def wipe(self, color):
        self.screen.fill(color)

    def quitevent(self):
        return linx.QUIT

    def mouse(self):
        return linx.mouse
    
    def onclick(self, rect):
        if rect.collidepoint(linx.mouse.get_pos()):
            if linx.mouse.get_pressed()[0]:
                return True
        return False
    
    
    def inter(self):
        return linx.event.get()
    
    def Box(self,x,y,w,h):
        return linx.rect.Rect(x,y,w,h)
    
    def drawbox(self, surface, color, box, outline=0):
        if surface == None:
            linx.draw.rect(self.screen, color, box, outline)
        else:
            linx.draw.rect(surface, color, box, outline)

    def drawcirc(self, screen, color, center, radius, outline=0):
        linx.draw.circle(screen, color, center, radius, outline)
    
    def hotkeys(self):
        return linx.key.get_pressed()

    def down(self):
        return linx.KEYDOWN
    
    def up(self):
        return linx.KEYUP

    def setfps(self, fps):
        self.fps = fps
        self.clock = linx.time.Clock()

    def runside(self):
        self.dt = self.clock.tick(self.fps)
        self.dts = self.dt / 1000.0

    def oncollision(self, rect1, rect2):
        return linx.Rect.colliderect(rect1, rect2)

    def plus(self, sprite):
        self.sprites.add(sprite)

    def cut(self):
        linx.quit()
        self.active = False

    def update(self):
            linx.display.update()
            for event in linx.event.get():
                self.onquit(event)
            

    def onquit(self, event):
        if event.type == linx.QUIT:
                    self.cut()
