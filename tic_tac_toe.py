import os

board  = list(range(1,10))
user = '❌'

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
    return int(input('Position: '))-1

def set_board(index):
    if board[index]!='❌' and board[index]!='⭕':
        board[index]=user
        return True
    else:
        return False

def changeTurn(user):
    return '⭕' if user=='❌' else "❌"

while(True):
    os.system('cls')
    print('Turn: ' + user)
    show_board()
    if(set_board(prompt()) == True):
        user = changeTurn(user)