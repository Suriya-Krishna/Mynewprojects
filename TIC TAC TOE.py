import random
print("Welcome to Tic Tac Toe,Let's start the game")
user_name = input("Enter your name")
game_board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
selections = {}
i = 1
available_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_game_board(board):
    print('----+----+----\n |   ' + board[1] + '|   ' + board[2] + '|   ' + board[3] + '|\n ----+----+----\n |   ' +
          board[4] + '|   ' + board[5] + '|   ' + board[6] + '|')
    print('----+----+----\n |   ' + board[7] + '|   ' + board[8] + '|   ' + board[9] + '| \n ----+----+----')


def winning_options(board, mk):
    count = 0
    mn = 0
    win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for mn in range(len(win_list)):
        if board[win_list[mn][0]] == mk and board[win_list[mn][1]] == mk and board[win_list[mn][2]] == mk:
           count = 1
    return count




def board_full(board):
    for m in range(1, 10):
        if board[m] != '':
            continue
        else:
            return False
    return True


def user_selection(board):
    user_place = int(input("Your selection"))
    if user_place <= 9:
        if board[user_place] == '':
            board[user_place] = user_turn
        else:
            print("Place is already occupied, enter another selection")
            user_selection(board)
    elif board_full(board):
        return 0
    return user_place


def comptr_selection(board):
    comptr_place = random.choice(available_options)
    if board[comptr_place] == '':
        board[comptr_place] = comptr_turn
        print(f"computer selection:{comptr_place}")
    elif board_full(board):
        return 0
    else:
        comptr_selection(board)
    return comptr_place


print_game_board(game_board)
print(f"You can choose your sign from ['X','O'] and available empty spaces [1-9],{user_name}")

user_turn = input("Select your sign")
if user_turn == 'X':
    comptr_turn = 'O'
else:
    comptr_turn = 'X'



storing = []
game_in = []
while i <= 10:
    game_board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    j = 1
    print(f"game{i}")
    winner = {}
    while not board_full(game_board):
        print(f"Round{j}")
        use_in = user_selection(game_board)
        comp_in = comptr_selection(game_board)
        print_game_board(game_board)
        if winning_options(game_board, user_turn):
            winner[i] = 'user'
        elif winning_options(game_board, comptr_turn):
            winner[i] = 'computer'
        selections[j] = [use_in, comp_in]
        j = j + 1
    game_in.append(game_board)
    storing.append(winner[i])
    print(F"winner is {winner[i]}")
    i = i + 1
c = 'y'
while (c == 'y'):
    try:
        value = int(input("Enter the game you want to find:"))
        print(storing[value - 1])
        print(f"The {value} gameboard is:\n ")
        print(print_game_board(game_in[value - 1]))
    except:
        print("round doesn't exist")
    c = input("Do you want to continue: y/n")
