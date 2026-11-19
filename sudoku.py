game_board = [[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
              [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
              [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]]
            
player_move = input("Enter your move: ")
print("Selected move: " + player_move)

def display_game_board(game_board):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    for i in game_board:
        print(end="||")
        for j in range(len(i)): 
            print("", i[j], end=" |")
            if ((j+1) % 3 == 0): print(end="|")
        print("\n")
        print("---------------------------------------")
            


display_game_board(game_board)