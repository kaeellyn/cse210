import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

"""Tic Tac Toe
    Author: Kaelyn Papa"""

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    print(f'{Fore.LIGHTWHITE_EX}Welcome to Tic-Tac-Toe!')        
    
    board = display_board()
    winner = checkWinner(board)
    draw = checkDraw(board)
        
    while winner != True or draw != True:           
        Px(board)
        display_board()            
        checkWinner(board)
        checkDraw(board)        
        if checkWinner(board) or checkDraw(board):
            break
        
        Po(board)
        display_board()
        checkWinner(board)
        checkDraw(board)
        if checkWinner(board) or checkDraw(board):
            break
        

def display_board():
    """Creates a tic-tac-toe board and prints them out"""
    
    one = board[0]
    two = board[1]
    three = board[2]
    four = board[3]
    five = board[4]
    six = board[5]
    seven = board[6]
    eight = board[7]
    nine = board[8]
    
    print('')
    print(f'{one}|{two}|{three}')
    print('-+-+-')
    print(f'{four}|{five}|{six}')
    print('-+-+-')
    print(f'{seven}|{eight}|{nine}')

    return board
        
def Px(board):
    """Player X input and display movement"""
    
    x_move = int(input(f'{Fore.RED}It\'s Player X\'s turn to choose a square (1-9): {Fore.RESET}')) 
    
    if x_move <= 0 or x_move > 9:
        print(f'That is an invalid number, try again!')
    elif x_move == board[x_move - 1] == 'x':
        print(f'That box is already taken, try another number!')
    else:
        board[x_move - 1] = 'x'
    
def Po(board):
    """Player O input and display movement"""

    o_move = int(input(f'{Fore.GREEN}It\'s Player O\'s turn to choose a square (1-9): {Fore.RESET}'))
    
    if o_move <= 0 or o_move > 9:
        print(f'That is an invalid number, try again!')
    elif o_move == board[o_move - 1] == 'o':
        print(f'That box is already taken, try another number!')
    else:
        board[o_move - 1] = 'o'
    
        
def checkDraw(board):
    """Check if it's a draw"""
    
    if (board[0]) != 1 and \
        (board[1]) != 2 and \
        (board[2]) != 3 and \
        (board[3]) != 4 and \
        (board[4]) != 5 and \
        (board[5]) != 6 and \
        (board[6]) != 7 and \
        (board[7]) != 8 and \
        (board[8]) != 9:
            print(f'{Fore.YELLOW}It\'s a draw!')
            return True

def checkWinner(board):    
    "Check if there's a winner"
    
    if board[0] == board[1] == board[2] or \
        board[0] == board[3] == board[6] or \
        board[0] == board[4] == board[8]:
        print(f"{Fore.YELLOW}Congratulations! Player '{board[0]}' won!")
        return True
    elif board[3] == board[4] == board[5]:
        print(f"{Fore.YELLOW}Congratulations! Player '{board[3]}' won!")
        return True
    elif board[6] == board[7] == board[8]:
        print(f"{Fore.YELLOW}Congratulations! Player '{board[6]}' won!")
        return True
    elif board[1] == board[4] == board[7]:
        print(f"{Fore.YELLOW}Congratulations! Player '{board[1]}' won!")
        return True
    elif board[2] == board[4] == board[6] or \
        board[2] == board[5] == board[8]:
        print(f"{Fore.YELLOW}Congratulations! Player '{board[2]}' won!")
        return True
                           
if __name__ == "__main__":
    main()