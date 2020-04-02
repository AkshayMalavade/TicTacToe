def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    marker=''
    while not (marker == 'X' or marker == 'O'):
        marker=input("Welcome to Tic Tac Toe\nPlayer 1:Choose X or O: ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    return ((board[7]==board[8]==board[9]==mark)or
    (board[7]==board[4]==board[1]==mark) or
    (board[1]==board[2]==board[3]==mark) or
    (board[3]==board[6]==board[9]==mark) or
    (board[9]==board[8]==board[7]==mark) or
    (board[7]==board[5]==board[3]==mark) or
    (board[9]==board[5]==board[1]==mark))
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for item in range(1,10):
        if space_check(board,item):
            return False
    return True

def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Choose board position: '))
    return position

def replay():
    choice=input("Do you want to play again? Please enter Yes or no:").upper()
    return choice=='YES'

while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn='Player 1'
    print('Player 1 will play first')
    play_game=input("Ready to play? Yes or no [type: y,n]")
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn=='Player 1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won')
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('it is a tie')
                    game_on=False
                else:
                    turn='Player 2'
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board, player2_marker ,position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('it is a tie')
                    break
                else:
                    turn='Player 1'

    if not replay():
        break