
class Square:
#classe Square (Case) : comporte la grille principale ainsi que les valeurs x et y
	def __init__(self,grille,x,y):
		self.grille=grille
		self.x=x
		self.y=y


	def squareUp(self):
	#methode squareUp
	#renvoie la case presente au dessus dans la grille
		return self.grille.get(self.x,self.y-1)

	def squareDown(self):
	#methode squareDown
	#renvoie la case presente en dessous dans la grille
		return self.grille.get(self.x,self.y+1)

	def squareLeft(self):
	#methode squareLeft
	#renvoie la case presente a gauche dans la grille
		return self.grille.get(self.x-1,self.y)

	def squareRight(self):
	#methode squareRight
	#renvoie la case presente a droite dans la grille
		return self.grille.get(self.x+1,self.y)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def isEmpty(self):
	#methode isEmpty
	#permet de verifier si une case est vide
  		if(self.x<0 or self.y<0 or self.x>=self.grille.long() or self.y>=self.grille.larg()):
  			return True

  		self.grille.nbBlocks()
  		for i in range(self.grille.nbBlocks()):
  			if (self in self.grille.getBlock(i).getSquares()):
  				return False
		return True

	def __str__(self):
		if self.isEmpty():
			return "[ ]" 
		else:
			return "[X]"
