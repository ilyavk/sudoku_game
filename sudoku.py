import curses # used for capturing keyboard input 

# update this later with a puzzle generator
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
                    [7,6,4,1,2,9,5,3,8]]

player_game_board = [[0 for _ in range(9)] for _ in range(9)]

fixed_cells = [[False for _ in range (9)] for _ in range(9)]

def set_up_game_board(answer_board, player_board):
    for i in range(9):
        for j in range(9):
            if (i + j) % 2 == 0: # change this to adjust the number of pre-filled cells
                player_board[i][j] = answer_board[i][j]
                fixed_cells[i][j] = True
    return player_board

def display_game_board(stdscr, game_board, user_row, user_col):
    stdscr.clear()

    stdscr.addstr(0, 0, "SUDOKU")
    stdscr.addstr(1, 0, "Arrow keys: Move | 1-9: Enter")
    stdscr.addstr(2, 0, "0: Clear | Q: Quit")

    for i in range(9):

        y = 4 + i + (i // 3)

        if i % 3 == 0:
            stdscr.addstr(y - 1, 0, "+-------+-------+-------+")

        for j in range(9):

            x = 2 + j * 2 + (j // 3) * 2

            if j % 3 == 0:
                stdscr.addstr(y, x - 2, "|")

            value = game_board[i][j]

            display_value = str(value) if value != 0 else "."

            if i == user_row and j == user_col:

                stdscr.addstr(
                    y, x, display_value, curses.A_REVERSE
                )

            elif fixed_cells[i][j]:

                stdscr.addstr(
                    y, x, display_value, curses.A_BOLD
                )

            else:
                stdscr.addstr(y, x, display_value)

        stdscr.addstr(y, 24, "|")

    stdscr.addstr(15, 0, "+-------+-------+-------+")

    stdscr.refresh()

def main(stdscr): # stdscr is the default screen object provided by curses.wrapper
    # initialize curses settings
    curses.curs_set(0)
    stdscr.keypad(True)

    set_up_game_board(answer_game_board, player_game_board)

    user_row, user_col = 0, 0
    
    display_game_board(stdscr, player_game_board, user_row, user_col)

    # main game loop
    while True:

        display_game_board(
            stdscr,
            player_game_board,
            user_row,
            user_col
        )

        key = stdscr.getch()

        if key == curses.KEY_UP:
            user_row = max(0, user_row - 1)

        elif key == curses.KEY_DOWN:
            user_row = min(8, user_row + 1)

        elif key == curses.KEY_LEFT:
            user_col = max(0, user_col - 1)

        elif key == curses.KEY_RIGHT:
            user_col = min(8, user_col + 1)

        elif ord("1") <= key <= ord("9"):

            if not fixed_cells[user_row][user_col]:

                player_game_board[user_row][user_col] = (
                    int(chr(key))
                )

        elif key in (ord("0"), curses.KEY_BACKSPACE, 127):

            if not fixed_cells[user_row][user_col]:

                player_game_board[user_row][user_col] = 0

        elif key in (ord("q"), ord("Q")):
            break

        if player_game_board == answer_game_board:

            display_game_board(
                stdscr,
                player_game_board,
                user_row,
                user_col
            )

            stdscr.addstr(17, 0, "Congratulations! You won!")
            stdscr.addstr(18, 0, "Press any key to exit.")
            stdscr.refresh()
            stdscr.getch()

            break
    

if __name__ == "__main__":
    curses.wrapper(main)