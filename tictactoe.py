import random
import math


whosewho={}
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

valid_moves = ["BL", "BM", "BR", "ML", "MM", "MR", "TL", "TM", "TR"]
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
    global whosewho
    explanation()
    whosewho = getXorO()
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
    if len(whosewho) > 0:
        print(f"You are {whosewho["player"]} this game")
        print("")
    board()

def getXorO():
    while True:
        choice = input("Do you want to be X or O?\n").upper().strip()
        if choice in ["X", "O"]:
            return {"player": choice, "cpu": "O" if choice == "X" else "X"}
        print("Invalid choice. Please select X or O")

def gameloop():
    if whosewho["player"] == "X":
        for _ in range(9):
            print(f"{whosewho["player"]}'s turn!")
            get_input()
            if checkforwin() or checkforcat():
                break
            cpu_move()
            if checkforwin() or checkforcat():
                break
    else:
        for _ in range(9):
            print(f"{whosewho["cpu"]}'s turn!")
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
    while True:
        user_move = input("Select your move\n").upper().strip()
        if user_move == "HELP":
            explanation()
            continue
        try:
            user_move = int(user_move) - 1
            boardstate[valid_moves[user_move]] = whosewho["player"]
            return
        except ValueError:
            if user_move in valid_moves and boardstate[user_move] == " ":
                boardstate[user_move] = whosewho["player"]
                return
        print("Invalid move. You can type 'help' for an explanation")

def aimfortwo():
    cornerPositions = ["TL", "TR", "BL", "BR"]
    for positions in winning_positions:
        values = [boardstate[pos] for pos in positions]  # Get the current board values
        if values.count(whosewho["cpu"]) == 1 and values.count(" ") == 2:
            for pos in positions:
                if pos in cornerPositions and boardstate[pos] == " ":
                    boardstate[pos] = whosewho["cpu"]
                    return True
    return False  # No winning move found

def trytowin():
    for positions in winning_positions:
        values = [boardstate[pos] for pos in positions]  # Get the current board values
        if values.count(whosewho["cpu"]) == 2 and values.count(" ") == 1:
            empty_index = values.index(" ")  # Find the empty spot
            boardstate[positions[empty_index]] = whosewho["cpu"]
            return True  # Move was made, return early
    return False  # No winning move found

def trytoblock():
    for positions in winning_positions:
        values = [boardstate[pos] for pos in positions]  # Get the current board values
        if values.count(whosewho["player"]) == 2 and values.count(" ") == 1:
            empty_index = values.index(" ")  # Find the empty spot
            boardstate[positions[empty_index]] = whosewho["cpu"]
            return True  # Move was made, return early
    return False  # No winning move found

def findPossibleMoves(game):
    possibleMoves = []
    for square in valid_moves:
        if game[square] == " ":
            possibleMoves.append(square)
    return possibleMoves

def scoreGame(game, depth):
    winner = determineWinner(game)
    if winner == "cpu":
        return 10 - depth
    elif winner == "player":
        return depth - 10
    else:
         return 0

def determineWinner(game):
    for positions in winning_positions:
        values = [game[pos] for pos in positions]
        if values.count(whosewho["cpu"]) == 3:
            return "cpu"
        elif values.count(whosewho["player"]) == 3:
            return "player"
    return None

def minimax(game, depth, maximizingPlayer, XorO):
    # Base Case
    possibleMoves = findPossibleMoves(game)
    winner = determineWinner(game)
    if winner is not None or len(possibleMoves) == 0:
        return {"score": scoreGame(game, depth), "move": None}
    if depth == 0:
        return {"score": scoreGame(game, depth), "move": None}
    # Recursive Case
    newChar = "O" if XorO == "X" else "X"
    bestMove = {
        "score": float('-inf') if maximizingPlayer else float('inf'),
        "move": None
    }
    for move in possibleMoves:
        newGame = game.copy()
        newGame[move] = XorO
        eval = minimax(newGame, depth - 1, not maximizingPlayer, newChar)
        if maximizingPlayer:
            if eval["score"] > bestMove["score"]:
                bestMove = {"score": eval["score"], "move": move}
        else:
            if eval["score"] < bestMove["score"]:
                bestMove = {"score": eval["score"], "move": move}
    return bestMove



    
def cpu_move():
    depth = len(findPossibleMoves(boardstate))
    decision = minimax(boardstate, depth, True, whosewho["cpu"])
    if decision["move"] is not None:
        boardstate[decision["move"]] = whosewho["cpu"]
        return
    available_moves = [move for move in valid_moves if boardstate[move] == " "]
    # #Going first, 1st move, take top left
    # if len(available_moves) == 9 and boardstate["TL"] == " ":
    #     boardstate["TL"] = whosewho["cpu"]
    #     return
    # #Going second, 1st move, take mid
    # if len(available_moves) == 8 and boardstate["MM"] == " ":
    #     boardstate["MM"] = whosewho["cpu"]
    #     return
    # if trytowin():
    #     return
    # if trytoblock():
    #     return
    # if aimfortwo():
    #     return
    # #if no moves, bail out
    # if not available_moves:
    #      return
    # #Take a random move if no heuristic found
    move = random.choice(available_moves)
    boardstate[move] = whosewho["cpu"]
    return
     








if __name__ == '__main__':
    main()
     


