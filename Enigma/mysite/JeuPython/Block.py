from Square import Square


class Block:

    def __init__(self,squares,horizontal):
        self.squares=squares
        self.horizontal=horizontal



    def moveNeg(self):
    	if(horizontal):
    		if(self.squares[0].isEmpty):
    			for i in range(len(self.squares)):
    				self.squares[i]=self.squares[i].squareLeft
    	else:
    		if(self.squares[0].isEmpty):
    			for i in range(len(self.squares)):
    				self.squares[i]=self.squares[i].squareUp
    def movePos(self):
    	if(horizontal):
    		if(self.squares[0].isEmpty):
    			for i in range(len(self.squares)):
    				self.squares[i]=self.squares[i].squareRight
    	else:
    		if(self.squares[0].isEmpty):
    			for i in range(len(self.squares)):
    				self.squares[i]=self.squares[i].squareDown

   	def getSquares(self):
   		return self.squares

    def __str__(self):
    	res="\n"
    	for i in range(len(self.squares)):
    		res+=str(self.squares[i])+"\n"
        return "\nblock : "+res
