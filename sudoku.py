game_board = [[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
              [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
              [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]]
            
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
        if ((i+1) % 3 == 0): print("-----------------------------------------")
            


display_game_board(game_board)