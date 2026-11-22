answer_game_board = [[8,7,1,2,9,6,3,4,5], 
                    [3,4,9,5,8,1,7,2,6], 
                    [2,5,6,7,4,3,8,9,1],
                    # top and middle rows
                    [4,2,7,6,5,8,9,1,3], 
                    [9,1,5,4,3,2,6,8,7], 
                    [6,8,3,9,1,7,2,5,4],
                    # bottom rows
                    [1,3,2,8,6,5,4,7,9], 
                    [5,9,8,3,7,4,1,6,2], 
                    [7,6,4,1,2,8,5,3,8]]

player_game_board = [[0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0]]

def set_up_game_board(answer_game_board, player_game_board):
    for i in range(len(answer_game_board)):
        for j in range(len(answer_game_board[i])):
            if (i+j) % 2 == 0:  # change this to adjust the number of pre-filled cells
                player_game_board[i][j] = answer_game_board[i][j]
    return player_game_board

def display_game_board(game_board):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    for i, row in enumerate(game_board):
        print(end="||")
        for j in range(len(row)):
            if (row[j] == 0): print(" x", end=" |")
            else: print("", row[j], end=" |")
            if ((j+1) % 3 == 0): print(end="|")
        print("\n")
        if ((i+1) % 3 == 0): print("-----------------------------------------  ")


player_game_board = set_up_game_board(answer_game_board, player_game_board)
# loop here to allow the player to make moves and check for win condition
display_game_board(player_game_board)