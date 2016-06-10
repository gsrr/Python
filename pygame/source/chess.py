import os
import pygame
from pygame.locals import *

CHESSDIRS2 = "../chess/s2/"
CHESSDIRS3 = "../chess/s3/"

def initAllChess():
	chessNum = {
		'BK' : 1,
		'BA' : 2,
		'BB' : 2,
		'BR' : 2,
		'BN' : 2,
		'BC' : 2,
		'BP' : 5,
		'RK' : 1,
		'RA' : 2,
		'RB' : 2,
		'RR' : 2,
		'RN' : 2,
		'RC' : 2,
		'RP' : 5,
	}
	allChess = []
	chessImg = os.listdir(CHESSDIRS2)
	for img in chessImg:
			role = os.path.splitext(img)[0]
			for i in range(chessNum[role]):
				allChess.append(Chess(img))

	return allChess

# 4 states : notExist, back, front, dead
class Chess:
	def __init__(self, img):
		self.x = 0
		self.y = 0
		self.state = 0
		self.name = os.path.splitext(img)[0]
		self.s2path = CHESSDIRS2 + img
		print self.s2path
		self.s3path = CHESSDIRS3 + self.name + "S" + ".GIF"
		self.s1Img = None
		self.s2Img = None
		self.s3Img = None

	def getImg(self):
		img = {
			0 : None,
			1 : self.s1Img,
			2 : self.s2Img,
			3 : self.s3Img,
		}[self.state]
		return  img

	def loadImg(self, loadFunc):
		self.s2Img = loadFunc(self.s2path)
		self.s3Img = loadFunc(self.s3path)
	
	def setImg(self, backImg):
		self.s1Img = backImg
	
	def setState(self, state):
		self.state = state

	def setXY(self, x, y):
		self.x = x
		self.y = y

	def showInfo(self):
		print self.name
	
def test_initAllChess():
	all = initAllChess()
	for c in all:
		c.showInfo()

def main():
	test_initAllChess()

if __name__ == "__main__":
	pygame.init()
	main()
