game_board = [[8,7,1,2,9,6,3,4,5], 
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
            
player_move = input("Enter your move: ")
print("Selected move: " + player_move)

def display_game_board(game_board):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    for i, row in enumerate(game_board):
        print(end="||")
        for j in range(len(row)): 
            print("", row[j], end=" |")
            if ((j+1) % 3 == 0): print(end="|")
        print("\n")
        if ((i+1) % 3 == 0): print("-----------------------------------------  ")
            


display_game_board(game_board)