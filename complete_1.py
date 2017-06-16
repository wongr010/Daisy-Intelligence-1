### original code
import copy
from random import choice

class square:
    def __init__(self,ID,val):
        self.ID = ID
        self.value = val
        self.bigSq = self._getbigSq() #board number
        self.smallSq = self._getsmallSq() #ID with a board
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
                if isBoardWon(getBigBoard(squares,squares[i].bigSq))==0: #Can't play in a won board; ==0 means not win yet
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




def get_move(timeout,data):
   
    PLAYER=int(data[0])
    # assign OPPONENT
    if PLAYER == 1:
        OPPONENT = 2
    else:
        OPPONENT = 1
        
        
    nextsquare=int(data[1])
    squares = []
    
    # a = data[17]
    # print(""a)
    
    for i in range(2,83): 
        squares.append(square(i-2,int(data[i])))  #create current board
    
    move = Strategy(nextsquare, squares, OPPONENT, PLAYER)
    
    #print(move)
    
    return move
    
    # #play first move on a new board
    #if playFirst_newboard(nextsquare)==1:
    #     return newBoardMove(nestsquare, squares)
    # 
    # #play first move on a playing board or play second move
    # if not playFirst_newboard(nextsquare):
    #     #play first
    #     if countFilledSquares(nextsquare, squares)%2 == 0: #count is an even number
    #         
        
    
    
    #validMoves=findValidMoves(squares,nextsquare)
    #return choice(validMoves)
    
    #test:
    #square = []




###strategy part

def Strategy(nextsquare, squares, OPPONENT, PLAYER):
    corner = [0, 2, 6, 8]
    edge = [1, 3, 5, 7]
    
    ### play on a empty board
    if playFirst_newboard(nextsquare):
        move = newBoardMove(nextsquare, squares, corner, edge, OPPONENT)
        return move
    
    #generate a little square
    littleSquare = [];
    for i in range(81):
        if squares[i].bigSq == nextsquare: #when it is the current board we are playing on
            littleSquare.append(square(i,squares[i].value))
    

    

    
    ### play on a non empty board
    if not playFirst_newboard(nextsquare):
        # check if you already win
        #if ifWin(littleSquare, nextsquare, PLAYER):
            
        # block the opponent
        
        # other cases
        move_in_littleSquare = determineMove(nextsquare, littleSquare, OPPONENT, corner, edge)
        move = convertSquareID_to_BoardID(nextsquare,move_in_littleSquare)
        return move
        
        """
        count = countFilledSquares(nextsquare, littleSquare);
        # print("count:")
        # print(count)
        #play first
        if count%2 == 0: #count is an even number
            #for the second move
            if(count == 2):
                
                # print(OPPONENT)
                # print(littleSquare[4])
                #check if O is at center or not
                if(littleSquare[4].value == OPPONENT): #O is at centre
                    #current board: 100 020 000
                    #two strategies: diagonal or edge
                    #here uses diagonal: place at 8
                    
                    return convertSquareID_to_BoardID(nextsquare,8)
                    
                else: #O is not at center
                    #place at any corner that has one space between the first X
                    #if O is on the corner
                    
                    for i in range(4):
                        
                        if littleSquare[corner[i]].value == OPPONENT:
                            for i in range(4):
                                #when it's empty append it
                                if littleSquare[i] == 0:
                                    convertSquareID_to_BoardID(nextsquare,i)
                                    return convertSquareID_to_BoardID(nextsquare,i)
                        else: #if O is on the edge
                            if littleSquare[edge[i]].value == OPPONENT:
                                n = edge[i]
                                # print(i)
                                # print(n)
                                if n == 1 or n == 5:
                                    return convertSquareID_to_BoardID(nextsquare,6)
                                if n == 3 or n == 7:
                                    return convertSquareID_to_BoardID(nextsquare,2)
                                    """
                                    
# outputs the id on littleSquare
def determineMove(nextsquare, littleSquare, OPPONENT, corner, edge):
        count = countFilledSquares(nextsquare, littleSquare);
        # print("count:")
        # print(count)
        
        ################### play first
        if count%2 == 0: #count is an even number
            #------------------for the first move
            if(count == 0):
                
                return 0
                
                
            #------------------for the second move
            if(count == 2):
                
                # print(OPPONENT)
                # print(littleSquare[4])
                #check if O is at center or not
                if(littleSquare[4].value == OPPONENT): #O is at centre
                    #current board: 100 020 000
                    #two strategies: diagonal or edge
                    #here uses diagonal: place at 8
                    if littleSquare[8].value == 0: #when it's empty
                        return 8
                    
                else: #O is not at center
                    #place at any corner that has one space between the first X
                    
                    
                    for i in range(4):
                        
                        if littleSquare[corner[i]].value == OPPONENT: #if O is on the corner
    
                            for l in range(4):
                                #when it's empty append it
                                if littleSquare[corner[l]].value == 0:
                                    return corner[l]
                        else: #if O is on the edge
                            if littleSquare[edge[i]].value == OPPONENT:
                                
                                n = edge[i]
                                    
                                #print(n)
                                if n == 1 or n == 5:
                                    if littleSquare[6].value == 0:
                                        return 6
                                if n == 3 or n == 7:
                                    if littleSquare[2].value == 0:
                                        return 2
            
            #------------------for the third move and above
            if(count > 2):  
                if(count == 4):
                    if(littleSquare[4].value == OPPONENT): #1: O is at centre
                        
                        for i in range (4):
                            if littleSquare[corner[i]].value == OPPONENT:#2: O on the corner
                                for l in range(4):
                                    if littleSquare[corner[l]].value == 0:
                                        return corner[l]
                            else:
                                #ROS
                                pass
                            
                    
                #ROS
                
            else:
                #ROS
                pass
            
                                    
        ####################### play second
        else: #count is an odd number
            #------------------for the first move
            if(count == 1):
                for i in range (4):
                    if littleSquare[edge[i]].value == OPPONENT: #when opponent plays at the edge node
                        #print("lala")
                        n = edge[i]
                        if n == 1 or n == 3:
                            #if littleSquare[0].value == 0:
                                return 0
                        if n == 1 or n == 5:
                            #if littleSquare[2].value == 0:
                                return 2
                        if n == 3 or n == 7:
                            #if littleSquare[6].value == 0:
                                return 6
                        if n == 5 or n == 7:
                            #if littleSquare[8].value == 0:
                                return 8
                        
                    elif littleSquare[corner[i]].value == OPPONENT: #when opponent plays at corner
                        return 4;
                    elif littleSquare[4].value == OPPONENT: #when opponent plays at center
                        return 0; #returns one of the corner nodes
                    else:
                        #ROS
                        pass
                        
                
            #------------------for the second move
            elif(count == 3):
                for i in range (4):
                    if littleSquare[edge[i]].value == OPPONENT: #when opponent plays at the edge node
                        if littleSquare[4].value == 0: # when opponent does not play at center
                            return 4;
                        else:
                            #ROS
                            pass
                            
                    elif littleSquare[corner[i]].value == OPPONENT: #when opponent plays at corner
                        # we should play at the edge
                        for l in range(4):
                            if littleSquare[edge[l]].value == 0:
                                #print("lala")
                                return edge[l]
                            else:
                                #ROS
                                pass
                    else:
                        #ROS
                        pass
            
            #------------------for the third move and above
            else:
                #ROS
                pass
                    
                
      
    

#check if you are playing first or second
def playFirst_newboard(nextsquare):
    if nextsquare == 9:
        return True
        
def newBoardMove(nextsquare, squares, corner, move, OPPONENT):
        #pick an empty board
        #generate the little board using boardwon output
        littleSquare = []
        for i in range(9):
            sq = getBigBoard(squares,i)
            winner = isBoardWon(sq)
            littleSquare.append(square(i, winner))
            # determineMove gives which littleSquare to play
        move = determineMove(0, littleSquare, OPPONENT,corner, move)*9 #the first square in the littleSquare 
    
        return move
        
            
            
        
    
def countFilledSquares(nextsquare, littleSquare):
    count = 0
    for i in range(9):
        if littleSquare[i].value != 0: 
                count += 1
    return count


def convertSquareID_to_BoardID(nextsquare, squareID):
    #print(squareID)
    ID = squareID+9*nextsquare
    # print(ID)
    return ID
    
    
    
# check if you already win

        
# block the opponent
        
# other cases
    
    
    
########### minmax


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


#testing function
def test():
    data_ = input("data is: ")
    
    data = str(data_).replace(" ","")
    
    # player = "1"
    # board = "0"
    # board0 = input("board0 is: ")
    # # # board1 = input("board1 is: ")
    # # # board2 = input("board2 is: ")
    # # # board3 = input("board3 is: ")
    # # # board4 = input("board4 is: ")
    # # # board5 = input("board5 is: ")
    # # # board6 = input("board6 is: ")
    # # # board7 = input("board7 is: ")
    # # # board8 = input("board8 is: ")
    # # 
    # # #board0 = "000000000"
    # board1 = "000000000"
    # board2 = "000000000"
    # board3 = "000000000"
    # board4 = "000000000"
    # board5 = "000000000"
    # board6 = "000000000"
    # board7 = "000000000"
    # board8 = "000000000"

    #data = player + board + str(board0) + str(board1) + str(board2) + str(board3) + str(board4) + str(board5) + str(board6) + str(board7) + str(board8)
    # # print(data)
    #print(len(data))
    
    
    print("move sould be:")
    return get_move(10, data)
    
    



   
