# User input for player 1 and player 2 #

def user_input():
    choice='Wrong'
    while choice not in ['X','O']:
        choice=input('Player 1,Enter marker X or O')
        player1=choice
        if choice not in ['X','O']:
            print('Sorry,Invalid choice')
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)

# Table display

from IPython.display import clear_output
def display_board(board):
    print('-'+'-'+'-'+'-'+'-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-'+'-'+'-'+'-'+'-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-'+'-'+'-'+'-'+'-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-'+'-'+'-'+'-'+'-')


# Win condition

def win(board,marker):
    
    
    return ((board[7]==board[8]==board[9]==marker) or 
(board[1]==board[2]==board[3]==marker) or
(board[4]==board[5]==board[6]==marker) or
(board[1]==board[4]==board[7]==marker) or
(board[2]==board[5]==board[8]==marker) or
(board[3]==board[6]==board[9]==marker) or
(board[3]==board[5]==board[7]==marker) or
(board[1]==board[5]==board[9]==marker))

# Place Marker

def place_marker(board,choice,position):
    board[position]=choice
 

#Choosing random player to start first

import random

def choose_first():
    spin=random.randint(0,1)
    
    if spin==0:
        return 'Player 1'
    else:
        return 'Player 2'


#Checking for empty space

def space_check(board,position):
    return  board[position]==' '


#To check if the board is full

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    else:
        return True

# To enter next position

def player_choice(board):
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position:(1-9)'))
        
    return position

# Replay option

def replay():
    
    choice=input("Play again? Enter Yes or No")
    return choice=='Yes'

# Game algorithm

# while loop to keep running the game
print('Welcome to tic tac toe')

while True:
    the_board=[' ']*10
    player1_marker,player2_marker=user_input()
    
    turn=choose_first()
    print(turn+'will go first')
    
    play_game=input('Ready to play? y or n')
    if play_game=='y':
        game_on= True
    else:
        game_on= False
   
    # Game Play
    
    while game_on:
        
        if turn=='Player 1':
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position=player_choice(the_board)
            # Place marker
            place_marker(the_board,player1_marker,position)
            
            #Check if they won
            if win(the_board,player1_marker):
                display_board(the_board)
                print(' Player 1 has won')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(' Tie game')
                    break
                else:
                    turn='Player 2'
        
        
        
        else:
            
              
            # Show the board
            display_board(the_board)
            # Choose a position
            position=player_choice(the_board)
            # Place marker
            place_marker(the_board,player2_marker,position)
            
            #Check if they won
            if win(the_board,player2_marker):
                display_board(the_board)
                print(' Player 2 has won')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(' Tie game')
                    break
                else:
                    turn='Player 1'
        
            


    
    

    if not replay():
        break
    


# Break out of the while loop on replay()
