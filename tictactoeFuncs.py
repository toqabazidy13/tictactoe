

# user picks either X or O 
# I/O 
def pickLetter():
    letter = input("Choose X or O: ")
    while True:    
       if letter == "X" or letter == "O":
           break
       else:
           letter = input("Re-enter X or O: ")
    return letter






# checks the diagonals for a win
# list -> bool, string
def checkDiags(board):
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True, board[0]
    elif board[2] == board[4] == board[6] and board[2] != " ":
        return True, board[2]
    else: 
        return False, board[0]
  

