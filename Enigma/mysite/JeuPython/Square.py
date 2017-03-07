
class Square:

    def __init__(self,grille,x,y):
        self.grille=grille
        self.x=x
        self.y=y

    def squareUp(self):
    	return self.grille.get(self.x,self.y-1)

    def squareDown(self):
    	return self.grille.get(self.x,self.y+1)

    def squareLeft(self):
    	return self.grille.get(self.x-1,self.y)

    def squareRight(self):
    	return self.grille.get(self.x+1,self.y)

    def isEmpty(self):
  		if(self.x<0 or self.y<0 or self.x>self.grille.long() or self.y>self.grille.larg()):
  			return True
  		print str(self.grille.nbBlocks())
  		for i in range(self.grille.nbBlocks()):
  			if (self in self.grille.getBlock(i).getSquares()):
  				return False
		return True

    def __str__(self):
    	if self.isEmpty:
    		return "[ ]" 
    	else:
    		return "[X]"

