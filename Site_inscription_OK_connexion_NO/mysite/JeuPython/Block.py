from Square import Square


class Block:
#classe Block : comporte un boolean pour designer s'il est horizontal ou vertical 
#						les squares qui le composent
	compteur=0

	def __init__(self,squares,horizontal):
		self.squares=squares
		self.horizontal=horizontal
		self.i=Block.compteur
		Block.compteur +=1



	def moveNeg(self):
		if(self.horizontal):
			if(self.squares[0].squareLeft().isEmpty()):
				for i in range(len(self.squares)):
					self.squares[i]=self.squares[i].squareLeft()
		else:
			if(self.squares[0].squareUp().isEmpty()):
				for i in range(len(self.squares)):
					self.squares[i]=self.squares[i].squareUp()

	def movePos(self):
		if(self.horizontal):
			if(self.squares[len(self.squares)-1].squareRight().isEmpty()):
				for i in range(len(self.squares)):
					self.squares[i]=self.squares[i].squareRight()
		else:
			if(self.squares[len(self.squares)-1].squareDown().isEmpty()):
				for i in range(len(self.squares)):
					self.squares[i]=self.squares[i].squareDown()

   	def getSquares(self):
   		return self.squares

   	def getI(self):
   		alphabet="abcdefghijklmnopqrstuvwxyz"
   		return alphabet[self.i]

	def __str__(self):
		res="\n"
		for i in range(len(self.squares)):
			res+=str(self.squares[i])
			if(not self.horizontal):
				res+="\n"
		return "\nblock : "+res
