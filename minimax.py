class square:
	def __init__(self,ID,val):
		self.ID = ID
		self.value = val
		self.bigSq = self._getbigSq()
		self.smallSq = self._getsmallSq()
	def _getbigSq(self):
		#return 3*int(self.ID/27) + int((self.ID%9)/3)
		return int(self.ID/9)
	def _getsmallSq(self):
		return self.ID%9

def findValidMoves(squares,nextsquare):
	vm = []
	for i in range(81):
		if squares[i].bigSq==nextsquare or nextsquare>8:  #Have to play in the next square, unless you can play anywhere
			if squares[i].value == 0: #Square must be empty
				if isBoardWon(getBigBoard(squares,squares[i].bigSq))==0: #Can't play in a won board
					if not isBoardFull(getBigBoard(squares,squares[i].bigSq)): #Can't play in a full board
						vm.append(i)
	return vm


def isBoardWon(squares):
	#Input: squares = 8 item list of squares 
	#Output: 0 if not win, 1 if 1 won, 2 if 2 won
	def compareSquares(squares,s1,s2,s3,v):
		if squares[s1]==squares[s2] and squares[s1]==squares[s3] and squares[s1]==v:
			return True
		else:
			return False
	if compareSquares(squares,0,1,2,1): return 1
	if compareSquares(squares,0,1,2,2): return 2
	if compareSquares(squares,3,4,5,1): return 1
	if compareSquares(squares,3,4,5,2): return 2
	if compareSquares(squares,6,7,8,1): return 1
	if compareSquares(squares,6,7,8,2): return 2
	if compareSquares(squares,0,3,6,1): return 1
	if compareSquares(squares,0,3,6,2): return 2
	if compareSquares(squares,1,4,7,1): return 1
	if compareSquares(squares,1,4,7,2): return 2
	if compareSquares(squares,2,5,8,1): return 1
	if compareSquares(squares,2,5,8,2): return 2
	if compareSquares(squares,0,4,8,1): return 1
	if compareSquares(squares,0,4,8,2): return 2
	if compareSquares(squares,2,4,6,1): return 1
	if compareSquares(squares,2,4,6,2): return 2
	return 0

def isBoardFull(squares):
	for i in range(9):
		if squares[i]==0:
			return False
	return True

def getBigBoard(squares,bigSq):
	sq = []
	for i in range(81):
		if squares[i].bigSq == bigSq:
			sq.append(squares[i].value)
	return sq

#def get_move(timeout,data):
#	PLAYER=int(data[0])
#	nextsquare=int(data[1])
#	squares = []
#	for i in range(2,83): 
#		squares.append(square(i-2,int(data[i])))
#	validMoves=findValidMoves(squares,nextsquare)
#	return choice(validMoves)*/

def choose(current_state, data):
		moves=[]
		moves=findValidMoves(temp_board, int(data[1]))
		for i in range(0, nummoves):
			temp_board=current_state
			new_state=change_state(temp_board, moves[i], 1)
			score=MyMove(current_state, data)
			if (score==10): return moves[i]
		

def change_state(current_state, move, player):
	current_state[move]=player
	return current_state

	
def MyMove(current_state, data):
	
	if isBoardFull(new_state) or (isBoardWon(new_state) != 0):
		if isBoardWon(new_state)==1:
			return 10
		elif isBoardWon(current_state)==2:
			return -10
		else: 
			return 0
	
	moves=[]
	temp_board=current_state
	moves=findValidMoves(temp_board, int(data[1]))
	nummoves=len(i)
	best=-1000
	
	for i in range(0, nummoves):
		new_state=change_state(temp_board, moves[i], 1)
		boardeval=YourMove(new_state, data, move)
		
		if boardeval>best:
			best=boardeval
			optimum=moves[i]
	
	return best
	
def YourMove(current_state, data, bestmove):
	
	if isBoardFull(current_state) or (isBoardWon(current_state) != 0):
		if isBoardWon(cuurent_state)==1:
			return 10
		elif isBoardWon(current_state)==2:
			return -10
		else: 
			return 0
			
	if isBoardFull(current_state) or (isBoardWon(current_state) != 0):
		return Score(current_state)
	moves=[]
	temp_board=current_state
	moves=findValidMoves(temp_board, int(data[1]))
	nummoves=len(i)
	best=1000
	
	for i in range(0, nummoves):
		new_state=change_state(temp_board, moves[i], 2)
		boardeval=MyMove(new_state, data, move)
		
		if boardeval<best:
			best=boardeval
			optimum=moves[i]
	
	return best
	