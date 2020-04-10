from os import system
#from time import sleep

# main variables
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#winner = None

def display_board(board):
    system('cls')
    print(' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3)
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ')
    print(' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3)
    print('-' * 11)
    print(' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3)
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print(' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3)
    print('-' * 11)
    print(' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3)
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ')
    print(' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 3)

def player_input(board, mark):
    position = 0
    while not ((position >= 1) and (position <= 9)) or (board[position] != ' '):
        try:
            position = int(input(f'\nPlease "{mark}" put your move: '))
        except ValueError:
            print('You have put wrong move key, please press 1..9')
            continue
        if not ((position >= 1) and (position <= 9)):
            print('You have put position out of range, please press 1..9')
            continue
        if board[position] == ' ':
            board[position] = mark
            return board
        else:
            print('This field has been already chosen, please select empty field.')

def is_winner(board):
    win_pattern = {'w1': [1, 2, 3], 'w2': [4, 5, 6], 'w3': [7, 8, 9], 'w4': [1, 4, 7], 'w5': [2, 5, 8], 'w6': [3, 6, 9],
                   'w7': [1, 5, 9], 'w8': [3, 5, 7]}
    win_string = ''

    for pattern in win_pattern.values():
        for element in pattern:
            win_string += board[element]
            #print('win_string: ', win_string)
            if win_string == 'XXX':
                return 'X'
            elif win_string == 'OOO':
                return 'O'
            else:
                pass
        win_string = ''
    return None

def main(board):
    # main part
    # intro
    print('Welcome to Tic Tac Toe!')
    # choosing mark sign
    player1_mark = input('Do you want to be "X" or "O"? ').upper()
    if player1_mark.upper() == 'X':
        player2_mark = 'O'
    else:
        player1_mark = 'O'
        player2_mark = 'X'

    # main logic
    for x in range(9):
        #system('cls')
        display_board(board)
        if x % 2 == 0:
            mark = player1_mark
        else:
            mark = player2_mark
        board = player_input(board, mark)
        winner = is_winner(board)
        if winner:
            #system('cls')
            display_board(board)
            print(f'\n"{winner}" you have won!')
            break

# star the program
main(board)