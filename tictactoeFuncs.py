


def pickLetter():
    letter = input("Choose X or O: ")
    while True:    
       if letter == "X" or letter == "O":
           break
       else:
           letter = input("Re-enter X or O: ")
    return letter

# it is used to detect input and see whether the input place is suitable or not 
def getInput(letter,board):
    while True:
        location = int(input("Where would you like to place your letter(pick in range 1-9):")) - 1
        if (location < 0 or location > 8 ) or board[location] != " " :
            print("Invalid Move! Location is already taken. Please try again.")
            else : 
                break
            board.pop(location)
            board.insert(location,letter)
            return board






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

#to check the cols to detect whether the player wins or no 
def checkCols(board):
    if board[0] == board[3] == board[6] and board[0] !=" ":
        return True,board[0]
    elif board[1] == board[4] == board[7] and board[1] !=" ":
        return true,board[1]
    else board[2] == board[5] == board[8] and board[2] !=" ":
        return true,board[2]
    else:
        return False,board[0]



  

