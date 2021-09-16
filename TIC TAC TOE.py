import random

print("Welcome to Tic Tac Toe,Let's start the game")
user_name = input("Enter your name")
game_board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
selections = {}
i = 1
available_options = []
for key in game_board:
    available_options.append(key)


def print_game_board(board):
    print('----+----+----')
    print('|   ' + board[1] + '|   ' + board[2] + '|   ' + board[3] + '|')
    print('----+----+----')
    print('|   ' + board[4] + '|   ' + board[5] + '|   ' + board[6] + '|')
    print('----+----+----')
    print('|   ' + board[7] + '|   ' + board[8] + '|   ' + board[9] + '|')
    print('----+----+----')


def winning_options(board, mk):
    return ((board[1] == mk and board[2] == mk and board[3] == mk) or (
                board[4] == mk and board[5] == mk and board[6] == mk) or (
                        board[7] == mk and board[8] == mk and board[9] == mk) or (
                        board[1] == mk and board[4] == mk and board[7] == mk) or (
                        board[2] == mk and board[5] == mk and board[8] == mk) or (
                        board[3] == mk and board[6] == mk and board[9] == mk) or (
                        board[1] == mk and board[5] == mk and board[9] == mk) or (
                        board[3] == mk and board[5] == mk and board[7] == mk))


# for k in range(1, 4):
# if k == 1 or k == 4 or k == 7:
#   if board[k] == board[k + 1] == board[k + 2] == mk:
#      return True
# elif k == 1 or k == 2 or k == 3:
#   if board[k] == board[k + 3] == board[k + 6] == mk:
# return True
# elif k == 1:
# if board[k] == board[k + 4] == board[k + 8] == mk:
#   return True
# elif k == 3:
# if board[k] == board[k + 2] == board[k + 4] == mk:
#   return True
# else:
# return False


def board_full(board):
    for m in range(1, 10):
        if board[m] != '':
            continue
        else:
            return False
    return True


def user_selection():
    user_place = int(input("Your selection"))
    if user_place == 'X' or 'O':
        if game_board[user_place] == '':
            game_board[user_place] = user_turn
        else:
            print("Place is already occupied, enter another selection")
            user_selection()
    elif board_full(game_board):
        return 0
    else:
        user_selection()
    return user_place


def comptr_selection():
    comptr_place = random.choice(available_options)
    if game_board[comptr_place] == '':
        game_board[comptr_place] = comptr_turn
        print(f"computer selection:{comptr_place}")
    elif board_full(game_board):
        return 0
    else:
        comptr_selection()
    return comptr_place


print_game_board(game_board)
print(f"You can choose your sign from ['X','O'] and available empty spaces [1-9],{user_name}")
user_turn = input("Select your sign")

if user_turn == 'X':
    comptr_turn = 'O'
else:
    comptr_turn = 'X'
storing = {}
while i <= 10:
    game_board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    j = 1
    print(f"game{i}")
    winner = {}
    while not board_full(game_board):
        print(f"Round{j}")
        use_in = user_selection()
        comp_in = comptr_selection()
        if winning_options(game_board, user_turn):
            winner[i] = 'user'
        elif winning_options(game_board, comptr_turn):
            winner[i] = 'computer'

        print_game_board(game_board)
        # if board_full(game_board):
        # print("Game Over.")
        selections[j] = [use_in, comp_in]
        print(selections[j])
        j = j + 1
    storing[i] = [selections, winner[i]]
    i = i + 1
value = int(input("Enter the game you want to find:"))
if value > 1 and value < 10:
    print(storing[value])
