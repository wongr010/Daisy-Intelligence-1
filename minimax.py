import copy

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
	for i in range(80):
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
	
		moves=findValidMoves(current_state, data)
		nummoves=len(moves)
		
		for i in range(0, nummoves):
			temp_board=current_state
			#print(moves[i])
			new_state=change_state(temp_board, moves[i], 1)
			score=YourMove(new_state, data)
			if (score==10): return moves[i]
			elif (score==0): nochoice=moves[i]
			
		return nochoice
		

def change_state(current_state, move, player):
	current_state[move].value=player
	return current_state

	
def MyMove(current_state, data):
	
	if isBoardFull(getBigBoard(current_state,data)) or (isBoardWon(getBigBoard(current_state,data)) != 0):
		if isBoardWon(getBigBoard(current_state, data))==1:
			return 10
		elif isBoardWon(getBigBoard(current_state, data))==2:
			return -10
		else: 
			return 0
	
	moves=[]
	temp_board=current_state
	moves=findValidMoves(temp_board, data)
	nummoves=len(moves)
	best=-1000
	
	for i in range(0, nummoves):
		new_state=change_state(temp_board, moves[i], 1)
		boardeval=YourMove(new_state, data)
		
		if boardeval>best:
			best=boardeval
	
	return best
	
def YourMove(current_state, data):
	
	if isBoardFull(getBigBoard(current_state,data)) or (isBoardWon(getBigBoard(current_state,data)) != 0):
		if isBoardWon(getBigBoard(current_state, data))==1:
			return 10
		elif isBoardWon(getBigBoard(current_state, data))==2:
			return -10
		else: 
			return 0

	moves=[]
	temp_board=current_state
	moves=findValidMoves(temp_board, data)
	nummoves=len(moves)
	best=1000
	
	for i in range(0, nummoves):
		new_state=change_state(temp_board, moves[i], 2)
		boardeval=MyMove(new_state, data)
		
		if boardeval<best:
			best=boardeval
	
	return best
	
"""	def get_move(timeout,data):
	PLAYER=int(data[0])
	nextsquare=int(data[1])
	squares = []
	for i in range(2,83): 
		squares.append(square(i-2,int(data[i])))
  return squares"""
  
time=input('Time is: ')
starter=input('starting player is ')
data=input('board is: ')
data=str(data)

PLAYER=int(data[0])
nextsquare=int(data[1])
squares = []
for i in range(2,83): 
  squares.append(square(i-2,int(data[i])))

if starter==1:
  iStart=True
  
else:
  iStart=False
		
while True:
  new_state=copy.deepcopy(squares)
  if iStart:
    move1=choose(new_state, nextsquare)
    print('move 1 is ')
    print(move1)
    new_state=change_state(squares, move1, 1)
    iStart=False
    if isBoardWon(getBigBoard(squares, nextsquare))!=0 or isBoardFull(getBigBoard(squares, nextsquare)):
      break
    
  else:
    move2=input('Your move: ')
    move2=int(move2)
    
    new_state=change_state(squares, move2, 2)
    iStart=True
    if isBoardWon(getBigBoard(squares, nextsquare))!=0 or isBoardFull(getBigBoard(squares, nextsquare)):
      break
	
print("Winner is")
if isBoardWon(getBigBoard(squares, nextsquare))==0:
  print("There is a tie")
else:
  print(isBoardWon(getBigBoard(squares, nextsquare)))