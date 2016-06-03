import sys
import pygame
from pygame.locals import *

EVENTMAP = {
	QUIT : "equit",
	ACTIVEEVENT : "eactiveevent",
	KEYDOWN : "ekeydown",
	KEYUP : "ekeyup",
	MOUSEMOTION : "emousemotion",
}

def createScreen(width, height, caption):
		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption(caption)
		return screen
	
def imgLoad(path):
	return pygame.image.load(path).convert()

def equit(paras):
	print "equit"
	sys.exit(0)

def eactiveevent(paras):
	print "eactiveevent"
	pass

def ekeydown(paras):
	print "ekeydown"
	pass

def ekeyup(paras):
	print "ekeyup"
	pass

def emousemotion(paras):
	print "emousemotion"
	x,y = pygame.mouse.get_pos()
	print x,y

def refresh(paras):
	screen = paras['screen']
	backgroup = paras['bg']
	screen.blit(backgroup, (0,0))
	pygame.display.update()
	

def main():
	img_path = "jaan.jpg"
	screen = createScreen(640, 400, "Hello World")
	imgBg = imgLoad(img_path)
	while True:
		paras = {
			'screen' : 	screen,
			'bg' : imgBg,
		}
		for event in pygame.event.get():
			func = getattr(sys.modules[__name__], EVENTMAP[event.type])
			func(paras)
		
		refresh(paras)

if __name__ == "__main__":
		pygame.init()
		main()


