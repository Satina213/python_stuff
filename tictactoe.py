import random


player_letter = ""
cpu_letter = ""
moveset = {
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

def main():
    explanation()
    player_letter = getXorO()
    # determine_first()
    gameloop()

def board():
    top_row()
    middle_row()
    bottom_row()
    print("" * 3)

def top_row():
    print("    " + " | " + "   " + " | " + "    ")
    print(f"  {moveset["TL"]} " + " | " + f" {moveset["TM"]} " + " | " + f"  {moveset["TR"]} ")
    print("____" + "_|_" + "___" + "_|_" + "____")

def middle_row():
        print("    " + " | " + "   " + " | " + "    ")
        print(f" {moveset["ML"]}  " + " | " + f" {moveset["MM"]} " + " | " + f" {moveset["MR"]}  ")
        print("____" + "_|_" + "___" + "_|_" + "____")

def bottom_row():
     print("    " + " | " + "   " + " | " + "    ")
     print(f" {moveset["BL"]}  " + " | " + f" {moveset["BM"]} " + " | " + f"  {moveset["BR"]} ")
     print("    " + " | " + "   " + " | " + "    ")

def explanation():
     print("\n" * 28)
     print("Hello! Thank you for playing Tic-Tac-Toe with me :D")
     print("")
     print("In order to make a move you will enter a two digit code where the first letter is the row:")
     print("\t'T' or 't' for top row, 'M' or 'm' for the middle row, and 'B' or 'b' for the bottom row")
     print("The second letter will then be 'L' or 'l', 'M' or 'm', or 'R' or 'r' for left, middle, right:")
     print("\t'TL' would print top left, 'mM' would print in the very middle, 'Br' in the bottom right, etc.")
     print("The player who is 'X' will move first.")
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

# def determine_first():
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
        if moveset[move] == " ":
            return False
    print("Cat got the game! Oh well\n")
    return True
    
def checkforwin():
    # TOP ROW
    if moveset["TL"] == moveset["TM"] == moveset["TR"] and moveset["TL"] != " ":
         print(f"{moveset['TL']} is the winner")
         return True
    # MIDDLE ROW
    if moveset["ML"] == moveset["MM"] == moveset["MR"] and moveset["ML"] != " ":
        print(f"{moveset['ML']} is the winner")
        return True
    # BOTTOM ROW
    if moveset["BL"] == moveset["BM"] == moveset["BR"] and moveset["BL"] != " ":
        print(f"{moveset['BL']} is the winner")
        return True
    # LEFT COLUMN
    if moveset["TL"] == moveset["ML"] == moveset["BL"] and moveset["TL"] != " ":
         print(f"{moveset['TL']} is the winner")
         return True
    # MIDDLE COLUMN
    if moveset["TM"] == moveset["MM"] == moveset["BM"] and moveset["TM"] != " ":
        print(f"{moveset['TM']} is the winner")
        return True
    # RIGHT COLUMN
    if moveset["TR"] == moveset["MR"] == moveset["BR"] and moveset["TR"] != " ":
         print(f"{moveset['TR']} is the winner")
         return True
    # TOP LEFT DIAGONAL
    if moveset["TL"] == moveset["MM"] == moveset["BR"] and moveset["TL"] != " ":
         print(f"{moveset['TL']} is the winner")
         return True
    # TOP RIGHT DIAGONAL
    if moveset["TR"] == moveset["MM"] == moveset["BL"] and moveset["TR"] != " ":
         print(f"{moveset['TR']} is the winner")
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
    if moveset[user_move] != " ":
         print("That square is already taken")
         return get_input()
    moveset[user_move] = player_letter
    #checkforwin()
         
def cpu_move():
    available_moves = [move for move in valid_moves if moveset[move] == " "]

    if not available_moves:
         return
    move = random.choice(available_moves)
    moveset[move] = cpu_letter
    # checkforwin()
     








if __name__ == '__main__':
    main()
     


