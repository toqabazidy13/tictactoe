


def pickLetter():
    letter = input("Choose X or O: ")
    while True:    
       if letter == "X" or letter == "O":
           break
       else:
           letter = input("Re-enter X or O: ")
    return letter







def checkDiags(board):
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True, board[0]
    elif board[2] == board[4] == board[6] and board[2] != " ":
        return True, board[2]
    else: 
        return False, board[0]

def checkRows(board):
    if board[0] == board[1] == board[2] and board[2] !=" ":
       return True,board[0]
    elif board[3]==board[4] == board[5] and board[5] !=" " :
        return True,board[3]
    elif board[6]==board[7]==board[8] and board[8] != " " :
        return True,board[6]
    else:
        return False,board[0]



  

