from Block import Block

class RedBlock(Block):
#classe RedBlock : comporte un boolean pour designer s'il est horizontal ou vertical 
#						les squares qui le composent
	def __init__(self,squares,grille):
		Block.__init__(self,squares,True)
		self.grille=grille



	def moveNeg(self):
		if(self.squares[0].isEmpty):
			for i in range(len(self.squares)):
				self.squares[i]=self.squares[i].squareLeft
		
	def movePos(self):
		if(self.grille.get(5,2) in self.squares):
			print("win!")
		if(self.squares[0].isEmpty):
			for i in range(len(self.squares)):
				self.squares[i]=self.squares[i].squareRight

   	def getSquares(self):
   		return self.squares

	def __str__(self):
		res="\n"
		for i in range(len(self.squares)):
			res+=str(self.squares[i])+"\n"
		return "\nblock : "+res
