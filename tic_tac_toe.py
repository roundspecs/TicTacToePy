import os

board  = list(range(1,10))
user = '❌'
win_lines = [
    [0, 1, 2], [0, 3, 6],
    [3, 4, 5], [1, 4, 7],
    [6, 7, 8], [2, 5, 8],
    [3, 5, 7], [0, 4, 8]
]

for i in range(9):
    board[i] = str(board[i]) + " "

def show_board():
    print("┌──┬──┬──┐")
    for i in range(3):
        print(f"│{board[i*3]}│{board[i*3+1]}│{board[i*3+2]}│")
        if (i != 2):
            print("├──┼──┼──┤")
    print("└──┴──┴──┘")

def prompt():
    answer = int(input('Position: '))
    while (1 > answer or answer > 9):
        answer = int(input('Try again: '))
    return answer-1

def set_board(index):
    if board[index]!='❌' and board[index]!='⭕':
        board[index]=user
        return True
    else:
        return False

def changeTurn(user):
    return '⭕' if user=='❌' else "❌"

def did_win(user, board, win_lines):
    for line in win_lines:
        if board[line[0]]== user and board[line[1]]== user and board[line[2]]== user:
            return True
    return False

turns = 0
while(True):
    os.system('cls')
    print('Turn: ' + user)
    show_board()
    if turns >= 9:
        print("It's a draw. Both of you suck!")
        break
    if(set_board(prompt()) == True):
        if (did_win(user, board, win_lines)):
            print(user + ' won!')
            break
        user = changeTurn(user)
        turns += 1