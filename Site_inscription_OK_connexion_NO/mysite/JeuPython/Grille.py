
from Square import Square
from Block import Block
from RedBlock import RedBlock

class Grille:
#classe Grille : comporte le Damier et la liste des blocks


	def __init__(self):
	#methode d'instance
	# prend en parametre x et y
		x=6
		y=6
	   	self.damier =[[Square(i,j,self) for i in range(x)] for j in range(y)]

		for j in range(y):
			for i in range(x):
				self.damier[i][j]=Square(self,i,j)

		self.blocks=[]
		self.initialize()

	def initialize(self):
	#methode initialize
	#permet d'ajouter les differents blocs	
		self.blocks.append(Block([self.damier[0][0],self.damier[1][0]],True))
		self.blocks.append(Block([self.damier[0][1],self.damier[1][1]],True))
		self.blocks.append(Block([self.damier[2][0],self.damier[2][1]],False))
		self.blocks.append(Block([self.damier[3][0],self.damier[4][0]],True))
		self.blocks.append(Block([self.damier[0][2],self.damier[0][3],self.damier[0][4]],False))
		self.blocks.append(Block([self.damier[0][5],self.damier[1][5]],True))
		self.blocks.append(Block([self.damier[1][3],self.damier[2][3],self.damier[3][3]],True))
		self.blocks.append(Block([self.damier[3][4],self.damier[3][5]],False))
		self.blocks.append(Block([self.damier[4][1],self.damier[4][2],self.damier[4][3]],False))
		self.blocks.append(Block([self.damier[5][2],self.damier[5][3]],False))
		self.blocks.append(Block([self.damier[4][4],self.damier[5][4]],True))
		self.blocks.append(Block([self.damier[4][5],self.damier[5][5]],True))

		self.blocks.append(RedBlock([self.damier[1][2],self.damier[2][2]],self))

	def __str__(self):
	#redefinition de str()
		res=""
		for i in range(self.nbBlocks()):
			res+=str(self.getBlock(i))+"\n"
		res+="\n"
		for j in range(self.larg()):	
			for i in range(self.long()):
				res+=str(self.damier[i][j])
			res+="\n"


		return res
	#Accesseurs
	def get(self,x,y):
		if(x<0 or x>=self.long() or y<0 or y>=self.larg()):
			return Square(self,x,y)
		else:
			return self.damier[x][y]

	def getBlock(self,x):
		return self.blocks[x]

	def long(self):
		return len(self.damier[0])

	def larg(self):
		return len(self.damier)

	def nbBlocks(self):
		return len(self.blocks)


#grille = Grille(6,6)
#print str(grille)

#grille.getBlock(11).moveNeg()
#grille.getBlock(11).moveNeg()
#grille.getBlock(11).moveNeg()
#grille.getBlock(11).movePos()

#grille.getBlock(11).movePos()
#grille.getBlock(11).moveNeg()
#grille.getBlock(11).moveNeg()
#print grille

