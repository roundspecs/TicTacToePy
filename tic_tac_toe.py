import os

board  = list(range(1,10))
def show_board():
    print("┌─┬─┬─┐")
    for i in range(3):
        print(f"│{board[i*3]}│{board[i*3+1]}│{board[i*3+2]}│")
        if (i != 2):
            print("├─┼─┼─┤")
    print("└─┴─┴─┘")

def prompt():
    os.system('cls')
    show_board()
    return int(input('Position: '))

prompt()