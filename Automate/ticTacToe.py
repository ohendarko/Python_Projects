"""
This code models a tic-tac-toe game.
Requires basic knowledge in:
1. Flow control; if, while, else loops
2. Dictionaries data structure
3. Functions
4. Print formatting
Adapted from AUTOMATE THE BORING STUFF WITH PYTHON by Al Sweigart,
page 116

Original Code:
theBoard = {'tL': ' ', 'tM': ' ', 'tR': ' ',
            'mL': ' ', 'mM': ' ', 'mR': ' ',
            'lL': ' ', 'lM': ' ', 'lR': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

ISSUES
1. Both players had only 9 chances leaving no space for mistakes.
   After those nine chances are exhausted, program will exit
   regardless of fair play.
2. No code to confirm if move is valid
3. Input switches to next player without confirming whether
   input is valid or not

FIXES and additions: included as comments
Left to add: Code to declare winner.
"""

theBoard = {'tL': ' ', 'tM': ' ', 'tR': ' ',
            'mL': ' ', 'mM': ' ', 'mR': ' ',
            'lL': ' ', 'lM': ' ', 'lR': ' '}

def printBoard(board):
    print(board['tL'] + '|' + board['tM'] + '|' + board['tR'])
    print('-+-+-')
    print(board['mL'] + '|' + board['mM'] + '|' + board['mR'])
    print('-+-+-')
    print(board['lL'] + '|' + board['lM'] + '|' + board['lR'])

turn = 'X'


while ' ' in theBoard.values(): # loop continues (game runs) as
    # long as there is an empty space(value)
    print("moves available: ")
    for k, v in theBoard.items(): # loop through keys and values
        if v == ' ':
            # if the value for this looped key is empty
            # in other words if there is a space available
            print("{} ".format(k), end="") # print only the keys with empty values(moves available)
    print()
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if move in list(theBoard.keys()): # checks whether move is valid
        theBoard[move] = turn
    else:
        print("Move not recognized")
    if turn == 'X' and move in list(theBoard.keys()):
        # "and move in list..." checks if code is valid before
        # switching to next player
        turn = 'O'
    elif turn == 'O' and move in list(theBoard.keys()):
        turn = 'X'
printBoard(theBoard)
print('Game Completed')