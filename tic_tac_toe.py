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
    os.system('cls')
    print('Turn: ' + user)
    show_board()
    return int(input('Position: '))

def set_board(index):
    board[index-1]=user

while(True):
    set_board(prompt())
    user = '⭕' if user=='❌' else "❌"