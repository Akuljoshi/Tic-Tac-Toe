def display_board(board):

    print("             |            |")
    print(" "          +       board[7] + "           |  " +       board[8] + "         |  " +      board[9])
    print("             |            |")
    print(" --------------------------------------")
    print("             |            |")
    print(" "          +       board[4] + "           |  " +       board[5] + "         |  " +      board[6])
    print("             |            |")
    print(" --------------------------------------") 
    print("             |            |")
    print(" "          +       board[1] + "           |  " +       board[2] + "         |  " +      board[3])
    print("             |            |")


test_board = ["f","x","0","x","0","x","0","x","0","x"]




def player_input():      
    
      marker = " "
        
      while marker != "x" and marker != "0":
          marker = input("\nPlayer 1: choose x or 0:")
          if  marker == "x" :
              return("x" ,"0")
          else:
              return("0" ,"x")
player1_marker ,player2_marker = player_input()

def place_marker(board, marker, position):

    board[position] = marker





def win_check(board , mark):
 
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[3] == mark and board[6] == mark and board[9] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[3] == mark and board[5] == mark and board[7] == mark))

display_board(test_board)
win_check(test_board, "x")





import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return "player 1"
    else:
        return "player 2"



def space_check(board, position):
    
      return board[position] == " "


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True


def player_choice(board):
    
    position = 0 
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("choose a position: (1-9) "))
    
    return position


def replay():
    
    choice = input("Play again: Yes or No")
    
    return choice == "Yes"



print("Welcome to TIC TAC TOE")

while True:
    the_board = [" "]*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + "will go first")
    
    play_game = input("Ready to play? yes or no ")
    
    if play_game == "yes":
        game_on = True
    else:
        game_on = False
    
    
    while game_on:
        if turn == "Player 1": 
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!!")
                game_on = False
            
            else:
                
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                
                else:
                    turn = "Player 2"
        else:
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!!")
                game_on = False
            
            else:
                
                if full_board_check(the_board):
                    dsiplay_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                
                else:
                    turn = "Player 1"
                    
                    
    if not replay():
        break
            
                    
                


