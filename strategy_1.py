### original code

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
    #data = [1,8,0,0,0,0,0000000000000200000000000000000001000000000000000000000000000000000000000000]
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
    
    move = Strategy(nextsquare, squares, OPPONENT)
    
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

def Strategy(nextsquare, squares, OPPONENT):
    #play first move on a new board
    if playFirst_newboard(nextsquare):
        move = newBoardMove(nextsquare, squares)
        return move
    
    #generate a little square
    littleSquare = [];
    for i in range(81):
        if squares[i].bigSq == nextsquare: #when it is the current board we are playing on
            littleSquare.append(square(i,square[i].value))
    
    corner = [0, 2, 6, 8]
    edge = [1, 3, 5, 7]
    
    #play first move on a playing board or play second move
    #when the board is not empty
    if not playFirst_newboard(nextsquare):
        count = countFilledSquares(nextsquare, squares);
        #play first
        if count%2 == 0: #count is an even number
            #for the second move
            if(count == 2):
                
                #check if O is at center or not
                if(littleSquare[4] == OPPONENT): #O is at centre
                    #current board: 100 020 000
                    #two strategies: diagonal or edge
                    #here uses diagonal: place at 8
                    return convertSquareID_to_BoardID(nextsquare,8)
                    
                else: #O is not at center
                    #place at any corner that has one space between the first X
                    #if O is on the corner
                    for i in range(4):
                        if littleSquare[corner[i]] == OPPONENT:
                            for i in range(4):
                                #when it's empty append it
                                if littleSquare[i] == 0:
                                    return convertSquareID_to_BoardID(nextsquare,i)
                        else: #if O is on the edge
                            if littleSquare[corner[i]] == OPPONENT:
                                if i == 1 or i == 5:
                                    return convertSquareID_to_BoardID(nextsquare,6)
                                if i == 3 or i == 7:
                                    return convertSquareID_to_BoardID(nextsquare,2)
                                    
            
                                    
                            
                        
                        
                        
                    
                    
                
		else: #count%2 != 0
            if (count == 1): #checking if we are playing for the first time as Player2
            	if (littleSquare[4] == OPPONENT): #this is case 2 of Krystal's diagram
                    return convertSquareID_to_BoardID (nextsquare, 0) #place our thing on index 0
                elif (littleSquare[0] == OPPONENT or littleSquare[2] == OPPONENT or littleSquare[6] == OPPONENT or littleSquare[8] == OPPONENT): #case 1    
					 return convertSquareID_to_BoardID (nextsquare, 4)
            
				else:
                    return convertSquareID_to_BoardID (nextsquare, 0) #place our thing on index 0
                       
    

#check if you are playing first or second
def playFirst_newboard(nextsquare):
    if nextsquare == 9:
        return True
        
def newBoardMove(nextsquare, squares):
        #pick an empty board
        validMoves = findValidMoves(squares,nextsquare)
        #corner: 0,2,6,8
        #we choose 0
        for i in range (len(validMoves)):
            if validMoves[i]%9 == 0: #place at the top left 
                return validMoves[i]
    
def countFilledSquares(nextsquare, squares):
    for i in range(81):
        if squares[i].bigSq == nextsquare: #this id is in the square we are playing
            if squares[i].value != 0:
                count += 1
    return count


def convertSquareID_to_BoardID(nextsquare, squareID):
        return squareID+9*nextsquare
    
    



   
