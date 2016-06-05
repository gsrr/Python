import sys
import copy
import pygame
from pygame.locals import *
import chess
import random

EVENTMAP = {
	QUIT : "equit",
	ACTIVEEVENT : "eactiveevent",
	KEYDOWN : "ekeydown",
	KEYUP : "ekeyup",
	MOUSEMOTION : "emousemotion",
	MOUSEBUTTONUP : "emousebtnup",
	MOUSEBUTTONDOWN : "emousebtndown",
}

BOARDX = 34
BOARDY = 51

def imgLoad(path):
	return pygame.image.load(path).convert()

class ChessBoard:
	def __init__(self, boardX, boardY):
		self.board = []
		self.x = boardX
		self.y = boardY
		self.backImg = imgLoad("../chess/back.gif")
	
	def init(self):
		allChess = chess.initAllChess()
		random.shuffle(allChess)
		for i in range(0,4):
			row = []
			starty = BOARDY + i * self.backImg.get_height()
			for j in range(0,8):
				startx = BOARDX + j * self.backImg.get_width()
				chs = allChess.pop()
				chs.loadImg(imgLoad)
				chs.setImg(self.backImg)
				chs.setXY(startx, starty)
				chs.setState(1)
				row.append(chs)
			self.board.append(copy.deepcopy(row))

	def show(self, screen):	
		for i in range(0,4):
			for j in range(0,8):
				chs = self.board[i][j]
				print chs
				print chs.x
				print chs.y
				#screen.blit(chs.getImg(), (chs.x, chs.y))
				
def createScreen(width, height, caption):
		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption(caption)
		return screen
	
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

def emousebtnup(paras):
	print "emousebtnup"
	x,y = pygame.mouse.get_pos()
	print x,y

def emousebtndown(paras):
	print "emousebtndown"
	x,y = pygame.mouse.get_pos()
	print x,y


def refresh(chessBoard, paras):
	screen = paras['screen']
	backgroup = paras['bg']
	screen.blit(backgroup, (0,0))
	chessBoard.show(screen)
	pygame.display.update()
	

def main():
	img_path = "../SHEET.gif"
	screen = createScreen(521, 313, "Chinese Chess Game")
	imgBg = imgLoad(img_path)
	chess_board = ChessBoard(BOARDX, BOARDY)
	chess_board.init()
	while True:
		paras = {
			'screen' : 	screen,
			'bg' : imgBg,
		}
		for event in pygame.event.get():
			print event.type
			func = getattr(sys.modules[__name__], EVENTMAP[event.type])
			func(paras)
		
		refresh(chess_board, paras)

if __name__ == "__main__":
		pygame.init()
		main()


