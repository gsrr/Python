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
		self.width = self.backImg.get_width()
		self.height = self.backImg.get_height()
		self.boardState = 0		# 0 --> no select , 1 --> select
		self.selectChessPos = (0,0)		
		self.players = [None, None]
		self.role = 0
		self.myfont = pygame.font.SysFont("monospace", 15)
	
	def init(self):
		allChess = chess.initAllChess()
		random.shuffle(allChess)
		for i in range(0,4):
			row = []
			starty = BOARDY + i * self.height
			for j in range(0,8):
				startx = BOARDX + j * self.width
				chs = allChess.pop()
				chs.loadImg(imgLoad)
				chs.setImg(self.backImg)
				chs.setXY(startx, starty)
				chs.setState(1)
				row.append(chs)
			self.board.append(row)
	
	def setState(self, state):
		self.boardState = state
	
	def BCinvalid(self, i, j1, j2, row):
		midchess = 0
		for k in range(j1 + 1, j2, 1):
			chs = self.board[i][k] if row == 0 else self.board[k][i]
			if chs != None:
				midchess += 1
		return midchess

	def invalidMove(self, x2, y2):
		if (abs(x2 - x1) + abs(y2 - y1)) > 1:
			return True
		
	def invalid(self, x2, y2):
		x1 = self.selectChessPos[0]
		y1 = self.selectChessPos[1]
		selectChess = self.board[x1][y1]
		if selectChess.name == "BC" or selectChess.name == "RC":
			if abs(x2 - x1) == 0:
				midchess = 0
				if y2 > y1:
					midchess += self.BCinvalid(x1, y1, y2, x2-x1)
				else:
					midchess += self.BCinvalid(x1, y2, y1, x2-x1)
				if midchess != 1:
					return True
				return False
			elif abs(y2 - y1) == 0:
				midchess = 0
				if x2 > x1:
					midchess += self.BCinvalid(y1, x1, x2, x2-x1)
				else:
					midchess += self.BCinvalid(y1, x2, x1, x2-x1)
				if midchess != 1:
					return True
				return False
			else:
				return True
		else:
			if (abs(x2 - x1) + abs(y2 - y1)) > 1:
				print "invalid"
				return True
	
	def changeRole(self):
		self.role  = (self.role + 1) % 2

	def changeState(self, i, j):
		if self.boardState == 2:
			return
		chs = self.board[i][j]
		if chs == None:
			if self.boardState == 1:
				if self.invalidMove(i,j):
					return
				x = self.selectChessPos[0]
				y = self.selectChessPos[1]
				selectChess = self.board[x][y]
				posx = BOARDX + j * self.width
				posy = BOARDY + i * self.height
				selectChess.setXY(posx, posy)
				self.board[i][j] = selectChess
				self.board[x][y] = None 
				selectChess.setState(2)
				self.setState(0)
				self.changeRole()
			return 

		if chs.state == 1 and self.boardState == 0:
			chs.setState(2)
			if self.players[self.role] == None:
				if chs.name[0] != self.players[(self.role + 1) % 2]:
					self.players[self.role] = chs.name[0]
			self.changeRole()


		elif chs.state == 2:
			if self.boardState == 0:
					if chs.name[0] != self.players[self.role]:
						return
					chs.setState(3)
					self.setState(1)
					self.selectChessPos = (i,j)
			elif self.boardState == 1:
					x = self.selectChessPos[0]
					y = self.selectChessPos[1]
					selectChess = self.board[x][y]
					if self.invalid(i,j):
						return
					if selectChess >= chs :
						if chs.name == "BK" or chs.name == "RK":
								chs.setState(4)
								self.setState(2)
						else:
								chs.setState(0)
								selectChess.setState(2)
								posX, posY = chs.getXY()
								selectChess.setXY(posX, posY)
								self.board[i][j] = selectChess
								self.board[x][y] = None 
								self.setState(0)
						self.changeRole()

		elif chs.state == 3:
			chs.setState(2)
			self.setState(0)

	def show(self, screen):	
		for i in range(0,4):
			for j in range(0,8):
				chs = self.board[i][j]
				if chs != None:
					screen.blit(chs.getImg(), (chs.x, chs.y))

		if self.players[self.role] != None:
				color = (255,0,0) if self.players[self.role] == "R" else (0,0,0)
				label = self.myfont.render("Player-%d"%(self.role + 1), 1, color)
				screen.blit(label, (215,0))
				
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
	x,y = pygame.mouse.get_pos()
	print x,y

def emousebtnup(paras):
	print "emousebtnup"
	x,y = pygame.mouse.get_pos()
	board = paras['board']
	i = int(((y + 1) - BOARDY) / board.height ) #row
	j = int(((x + 1) - BOARDX) / board.width )	#col
	if i > 3 or j > 7:
		return
	board.changeState(i, j)

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
			'board' : chess_board,
		}
		for event in pygame.event.get():
			print event.type
			func = getattr(sys.modules[__name__], EVENTMAP[event.type])
			func(paras)
		
		refresh(chess_board, paras)

if __name__ == "__main__":
		pygame.init()
		main()


