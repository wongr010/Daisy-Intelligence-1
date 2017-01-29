#check if our robot needs to start a game on a new board
def choose_new_board(game_status):
    #second_num = str(game_status)
    if game_staus[1] == '9' :
        return True
    else:
        return False
    
"""this function ONLY checks the small board that we are currently playing on
it returns False if it does not see two opponent's marks that would lead to the opponent's victory
in the next round anywhere"""

def is_opponent_winning(game_status):
    small_board_array = [];
    #game_status = str(game_status)
    
    if game_status[0] == 1:
        opponent_mark = '2'
    else: 
        opponent_mark = '1'
    
    if choose_new_board(game_status == True):
        return False
    else: 
        board_using = int (game_status[1])
        small_board_array = game_status [board_using * 9 + 2: (board_using + 1) * 9 + 2]
        
        #check diagonally
        if (small_board_array[4] == '0'):
            if (small_board_array[0] == opponent_mark and small_board_array[8] == opponent_mark): # " \ " direction
                return True 
            if (small_board_array[2] == opponent_mark and small_board_array[6] == opponent_mark): # " / " direction
                return True
        elif (small_board_array[4] == opponent_mark):
        	if (small_board_array[2] == opponent_mark or small_board_array[6] == opponent_mark or small_board_array[0] == opponent_mark or small_board_array[8] == opponent_mark): 
				return True
				
        for row in range (3):
            opp_sum_v = 0;
            opp_sum_h = 0;
            
            for clm in range (3): 
                if small_board_array[row * 3 + clm] == opponent_mark:#check each row to see if there are two opp's marks
                    opp_sum_h = opp_sum_h + 1
                if small_board_array [clm * 3 + row] == opponent_mark:
                    opp_sum_v = opp_sum_v + 1
                    
            if (opp_sum_h== 2 or opp_sum_v == 2):
                return True
        
        return False
        
         
            
#this is a test case
print (is_opponent_winning (100010100005))
