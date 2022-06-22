# -------- Global variables -------------

# --- Game board
board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

# If game still going
game_still_going = True

# while won or tie
winner = None

# Who turn is it
current_player = "X"

# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe
def play_game():

    # Display inital board
    display_board()

    # While game is still going
    while game_still_going:

        # handle  a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player 
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")

# Handle single turn an arbitrary player
def handle_turn(player):

    print(player + "'s turn.'")
    position = input("Chose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1" , "2" ,"3" , "4" , "5" , "6", "7" , "8" , "9"]:
            position = input("Invalid input. Chose a position from 1-9: ")

        position = int(position)- 1

        if board[position] == "-":
            valid = True
        else:
            print("You are go there. Go again")


    board[position] = player
    display_board()

def check_if_game_over():
    check_for_win()
    check_if_tie()

def check_for_win():

    # Global variables
    global winner

    # check rows
    row_winner = check_rows()

    # check colum
    colum_winner = check_colum()

    # check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif colum_winner:
        winner = colum_winner

    elif diagonals_winner:
        winner = diagonals_winner

    else:
        winner = None

    return

def check_rows():

    # setup global variables
    global game_still_going

    # check if any of the all the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # if any row does have a match, flag that is a win

    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return



def check_colum():
     # setup global variables
    global game_still_going

    # check if any of the all the same value and is not empty
    colum_1 = board[0] == board[3] == board[6] != "-"
    colum_2 = board[1] == board[4] == board[7] != "-"
    colum_3 = board[2] == board[5] == board[8] != "-"

    # if any row does have a match, flag that is a win

    if colum_1 or colum_2 or colum_3:
        game_still_going = False

    # Return the winner (X or O)
    if colum_1:
        return board[0]
    elif colum_2:
        return board[1]
    elif colum_3:
        return board[2]
    return

def check_diagonals():
    # setup global variables
    global game_still_going

    # check if any of the all the same value and is not empty
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    # if any row does have a match, flag that is a win

    if diagonals_1 or diagonals_2:
        game_still_going = False

    # Return the winner (X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return

def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    
    # global Variable we need
    global current_player

    # if the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
    
    # If the current player was 0, then change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()   