import os
import pygame
from pygame.locals import *
import traceback
import sys

CHESSDIRS2 = "../chess/s2/"
CHESSDIRS3 = "../chess/s3/"
CHESSDIRS4 = "../chess/s4/"

def RK_compare(n1, n2):
	return BK_compare(n1, n2)

def BK_compare(n1, n2):
	map2Num = {
		'P' : 2,
		'N' : 0,
		'R' : 0,
		'B' : 0,
		'A' : 0,
		'K' : 1,
		'C' : 0,
	}
	if map2Num[n1[1]] >= map2Num[n2[1]]:
		return True
	return False

def RP_compare(n1, n2):
	return BP_compare(n1, n2)

def BP_compare(n1, n2):
	map2Num = {
		'P' : 1,
		'N' : 2,
		'R' : 2,
		'B' : 2,
		'A' : 2,
		'K' : 0,
		'C' : 2,
	}
	if map2Num[n1[1]] >= map2Num[n2[1]]:
		return True
	return False

def RC_compare(n1, n2):
	return BC_compare(n1, n2)

def BC_compare(n1, n2):
	print "BC_compare"
	map2Num = {
		'P' : 0,
		'N' : 0,
		'R' : 0,
		'B' : 0,
		'A' : 0,
		'K' : 0,
		'C' : 1,
	}
	if map2Num[n1[1]] >= map2Num[n2[1]]:
		return True
	return False

def Other_compare(n1, n2):
	print "other_compare"
	map2Num = {
		'P' : 1,
		'C' : 2,
		'N' : 3,
		'R' : 4,
		'B' : 5,
		'A' : 6,
		'K' : 7,
	}
	if map2Num[n1[1]] >= map2Num[n2[1]]:
		return True
	return False


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
		self.s3path = CHESSDIRS3 + self.name + "S" + ".GIF"
		self.s4path = CHESSDIRS4 + self.name + "M" + ".GIF"
		self.s1Img = None
		self.s2Img = None
		self.s3Img = None
		self.s4Img = None

	def getImg(self):
		img = {
			0 : None,
			1 : self.s1Img,
			2 : self.s2Img,
			3 : self.s3Img,
			4 : self.s4Img,
		}[self.state]
		return  img

	def loadImg(self, loadFunc):
		self.s2Img = loadFunc(self.s2path)
		self.s3Img = loadFunc(self.s3path)
		if os.path.exists(self.s4path):
			self.s4Img = loadFunc(self.s4path)
	
	def setImg(self, backImg):
		self.s1Img = backImg
	
	def setState(self, state):
		self.state = state

	def setXY(self, x, y):
		self.x = x
		self.y = y

	def getXY(self):
		return (self.x, self.y)

	def showInfo(self):
		print self.name
	
	def __ge__(self, other):
		n1 = self.name
		n2 = other.name
		print n1,n2
		if n1[0] != n2[0]:	# same color
			try:
				func = getattr(sys.modules[__name__], n1 + "_compare")
				return func(n1, n2)
			except:
				print traceback.format_exc()
				return Other_compare(n1, n2)
		return False

	
def test_initAllChess():
	all = initAllChess()
	for c in all:
		c.showInfo()

def main():
	test_initAllChess()

if __name__ == "__main__":
	pygame.init()
	main()
