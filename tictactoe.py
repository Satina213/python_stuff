import random


player_letter = ""
cpu_letter = ""
boardstate = {
     "TL": " ",
     "TM": " ",
     "TR": " ",
     "ML": " ",
     "MM": " ",
     "MR": " ",
     "BL": " ",
     "BM": " ",
     "BR": " ",
}

valid_moves = ["TL","TM","TR","ML","MM","MR","BL","BM","BR"]
winning_positions = [
    ["TL", "TM", "TR"],  # Top row
    ["ML", "MM", "MR"],  # Middle row
    ["BL", "BM", "BR"],  # Bottom row
    ["TL", "ML", "BL"],  # Left column
    ["TM", "MM", "BM"],  # Middle column
    ["TR", "MR", "BR"],  # Right column
    ["TL", "MM", "BR"],  # Diagonal from top-left to bottom-right
    ["TR", "MM", "BL"]   # Diagonal from top-right to bottom-left
]

def main():
    explanation()
    player_letter = getXorO()
    gameloop()

def board():
    top_row()
    middle_row()
    bottom_row()
    print("" * 3)

def top_row():
    print("    " + " | " + "   " + " | " + "    ")
    print(f"  {boardstate["TL"]} " + " | " + f" {boardstate["TM"]} " + " | " + f"  {boardstate["TR"]} ")
    print("____" + "_|_" + "___" + "_|_" + "____")

def middle_row():
        print("    " + " | " + "   " + " | " + "    ")
        print(f" {boardstate["ML"]}  " + " | " + f" {boardstate["MM"]} " + " | " + f" {boardstate["MR"]}  ")
        print("____" + "_|_" + "___" + "_|_" + "____")

def bottom_row():
     print("    " + " | " + "   " + " | " + "    ")
     print(f" {boardstate["BL"]}  " + " | " + f" {boardstate["BM"]} " + " | " + f"  {boardstate["BR"]} ")
     print("    " + " | " + "   " + " | " + "    ")

def explanation():
    print("\n" * 28)
    print("Hello! Thank you for playing Tic-Tac-Toe with me :D")
    print("")
    print("In order to make a move you will enter a two digit code where the first letter is the row and the second letter is the column")
    print("\tThe rows are \"T\", \"M\", \"B\" for top, middle, and bottom")
    print("\tThe columns are \"L\", \"M\", \"R\" for left, middle, and right")
    print("\t'TR', 'mm', 'Tl', 'bL' are all valid moves.")
    print("")
    print("The player who is 'X' will move first.")
    print("")
    if player_letter == "X" or player_letter == "O":
        print(f"You are {player_letter} this game")
        print("")

def getXorO():
    global player_letter
    global cpu_letter
    player_letter = input("Do you want to be X or O\n").upper().strip()
    if player_letter not in ["X", "O"]:  
        print("You must select X or O")
        return getXorO()  # Recursive call must be returned
    print(f"You are {player_letter} this match!")
    if player_letter == "X":
         cpu_letter = "O"
    else:
         cpu_letter = "X"
    return player_letter  

def gameloop():
    global player_letter
    global cpu_letter
    if player_letter == "X":
        for _ in range(9):
            print(f"{player_letter}'s turn!")
            get_input()
            if checkforwin() or checkforcat():
                break
            cpu_move()
            if checkforwin() or checkforcat():
                break
    else:
        for _ in range(9):
            print(f"{cpu_letter}'s turn!")
            cpu_move()
            if checkforwin() or checkforcat():
                break
            get_input()
            if checkforwin() or checkforcat():
                break
    board()

def checkforcat():
    for move in valid_moves:
        if boardstate[move] == " ":
            return False
    print("Cat got the game! Oh well\n")
    return True
    
def checkforwin():
    # TOP ROW
    if boardstate["TL"] == boardstate["TM"] == boardstate["TR"] and boardstate["TL"] != " ":
         print(f"{boardstate['TL']} is the winner")
         return True
    # MIDDLE ROW
    if boardstate["ML"] == boardstate["MM"] == boardstate["MR"] and boardstate["ML"] != " ":
        print(f"{boardstate['ML']} is the winner")
        return True
    # BOTTOM ROW
    if boardstate["BL"] == boardstate["BM"] == boardstate["BR"] and boardstate["BL"] != " ":
        print(f"{boardstate['BL']} is the winner")
        return True
    # LEFT COLUMN
    if boardstate["TL"] == boardstate["ML"] == boardstate["BL"] and boardstate["TL"] != " ":
         print(f"{boardstate['TL']} is the winner")
         return True
    # MIDDLE COLUMN
    if boardstate["TM"] == boardstate["MM"] == boardstate["BM"] and boardstate["TM"] != " ":
        print(f"{boardstate['TM']} is the winner")
        return True
    # RIGHT COLUMN
    if boardstate["TR"] == boardstate["MR"] == boardstate["BR"] and boardstate["TR"] != " ":
         print(f"{boardstate['TR']} is the winner")
         return True
    # TOP LEFT DIAGONAL
    if boardstate["TL"] == boardstate["MM"] == boardstate["BR"] and boardstate["TL"] != " ":
         print(f"{boardstate['TL']} is the winner")
         return True
    # TOP RIGHT DIAGONAL
    if boardstate["TR"] == boardstate["MM"] == boardstate["BL"] and boardstate["TR"] != " ":
         print(f"{boardstate['TR']} is the winner")
         return True
    return False

def get_input():
    global valid_moves
    board()
    user_move = input("Select your move\n").upper().strip()
    if user_move == "EXPLANATION":
        explanation()
        return get_input()
    if user_move not in valid_moves:
        print("\nInvalid Move. You can type 'Explanation' for help.")
        return get_input()
    if boardstate[user_move] != " ":
         print("That square is already taken")
         print("You can type 'explanation' for help!")
         return get_input()
    boardstate[user_move] = player_letter
    #checkforwin()
         
def aimfortwo():
    cornerPositions = ["TL", "TR", "BL", "BR"]
    for positions in winning_positions:
        values = [boardstate[pos] for pos in positions]  # Get the current board values
        if values.count(cpu_letter) == 1 and values.count(" ") == 2:
            for pos in positions:
                if pos in cornerPositions and boardstate[pos] == " ":
                    boardstate[pos] = cpu_letter
                    return True
    return False  # No winning move found


def trytowin():
    for positions in winning_positions:
        values = [boardstate[pos] for pos in positions]  # Get the current board values
        if values.count(cpu_letter) == 2 and values.count(" ") == 1:
            empty_index = values.index(" ")  # Find the empty spot
            boardstate[positions[empty_index]] = cpu_letter
            return True  # Move was made, return early
    return False  # No winning move found

def trytoblock():
    for positions in winning_positions:
        values = [boardstate[pos] for pos in positions]  # Get the current board values
        if values.count(player_letter) == 2 and values.count(" ") == 1:
            empty_index = values.index(" ")  # Find the empty spot
            boardstate[positions[empty_index]] = cpu_letter
            return True  # Move was made, return early
    return False  # No winning move found


def cpu_move():
    available_moves = [move for move in valid_moves if boardstate[move] == " "]
    #Going first, 1st move, take top left
    if len(available_moves) == 9 and boardstate["TL"] == " ":
        boardstate["TL"] = cpu_letter
        return
    #Going second, 1st move, take mid
    if len(available_moves) == 8 and boardstate["MM"] == " ":
        boardstate["MM"] = cpu_letter
        return
    if trytowin():
        return
    if trytoblock():
        return
    if aimfortwo():
        return
    #if no moves, bail out
    if not available_moves:
         return
    #Take a random move if no heuristic found
    move = random.choice(available_moves)
    boardstate[move] = cpu_letter
    
     








if __name__ == '__main__':
    main()
     


