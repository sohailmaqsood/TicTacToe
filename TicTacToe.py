board = []

for x in range(3):
    board.append(["#"]*3)
def board_fn(board):
    for i in board:
        print(" ".join(i))

def game_check(board):
    #Checking if we have winner after last move
    #for Horizontal Lines
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != "#":
        return (board[0][1])
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != "#":
        return (board[1][1])
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != "#":
        return (board[2][1])
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != "#":
        return (board[0][0])
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != "#":
        return (board[0][1])
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != "#":
        return (board[0][2])
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != "#":
        return (board[0][0])
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != "#":
        return (board[0][2])
    else:
        return False  

#Input of range check function

def oor(a1,a2,board):
    if (a1 >= 3) or (a2 >= 3) :
        print ("#####Please mark inside the playing grid#####")
        return True
    elif (board[a1][a2] != '#'):
        print ("####Already Marked Space####")
        return True
    else:
        return False

def input_fn(marker):
    #player inputs
    p1_row = int(input("Specify row :- "))
    p1_col = int(input("Specify Col :- "))

    x = oor(p1_row,p1_col,board)

    if x == False :
        #marking Player 1 inputs
        board[p1_row][p1_col] = marker
    else :
        input_fn(marker)
        
a = game_check(board)

while a == False :
    board_fn(board)
    print ("Player 1 Input Please ")
    input_fn("X")
    a = game_check(board)
    if a != False:
        break
    
    board_fn(board)
    print ("Player 2 Input Please ")
    input_fn("O")
    a = game_check(board)
    if a != False:
        break
    
print(" \n winner is " + a)