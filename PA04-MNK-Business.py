#!/usr/bin/python3
# -*- coding: utf-8 -*-

# do NOT change the next two lines of code...
import sys
assert ('linux' in sys.platform), "This code should be run on Linux, just a reminder to follow instructions..."
import random
from typing import List, Tuple


def draw_board(board: List[List[str]], rows: int, cols: int) -> None:


    '''
    Test:       01_draw_board_test.py >01_draw_board_output.txt
    Purpose:    draws the board to std out
    Parameters: board list of list of strings,
                int number of rows (m),
                and int number of columns (n)
    User Input: none
    Prints:     game board on the screen with X, O,
                or Space, at respective positions
    Returns:    nothing
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    rowarray = [' ']
    if rows == 3:
        for i in range(rows):
            rowarray.append(str(i))
    else:
        for i in range(rows+1):
            rowarray.append(str(i))
    print(' '.join(rowarray))
    for i in range(len(board)):
        x = '|'.join(board[i])
        print(str(i) + '|'+x+'|')


def input_player_letter() -> List[str]:
    '''
    Test:       00_input_player_letter.py <00_input_player_letter.txt
    Purpose:    choose who is X and who is O
    Parameters: none
    User Input: yes
    Prints:     asks the player type which letter they want to be.
    Returns:    a list af strings with the player's letter as the first item,
                and the computer's letter as the second,
                where the first element in the list is the player's letter,
                the second is the computer's letter.
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    playerchar = str(input("Do you want to be X or O?\n"))
    if playerchar == 'x':
        return ["X", "O"]
    elif playerchar == 'o':
        return ["O", "X"]


def who_goes_first() -> str:
    random.seed(0)
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "human player"


def make_move(board: List[List[str]], letter: str, row: int, col: int) -> None:
    '''
    Test:       04_make_move_test.py
    Purpose:    places player's letter or computer's letter at the specified
                position i.e. move. Very simple function
    Parameters: board as a list of list of strings, letter as a string,
                row and col as ints.
    User Input: none
    Prints:     nothing
    Returns:    nothing
    Modifies:   board itself which is a mutable passed in!
    Calls:      none of our functions (standard python ok)
    '''
    move = letter[0]
    board[row][col] = move
    return board

def check_across(board: List[List[str]], letter: str, rows: int, cols: int, matches: int, i: int, j: int) -> bool:
    '''
    Test:       06_check_across_test.py
    Purpose:    checks if player's letter is in all the adjacent k
                (number_of_matches) across the row from left to right.
    Parameters: board, letter of player, num of rows, num of cols,
                num of matches, position as i, j
    User Input: none
    Prints:     nothing
    Returns:    True if k-match pattern is found for player's letter across
                the row (corresponding to i,j, and
                False otherwise.
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    match = 1
    for num in range(rows):
        if j+num+1 >= cols:
            break
        if board[i][j+num+1] == letter:
            match = match + 1
        else:
            break
    if match >= matches:
        return True
    else:
        return False


def check_down(board: List[List[str]],
               letter: str,
               rows: int,
               cols: int,
               matches: int,
               i: int,
               j: int) -> bool:
    '''
    Test:       07_check_down_test.py
    Purpose:    checks if player's letter is in all the adjacent k
                (number_of_matches)
                positions across the col from top to bottom
    Parameters: board, letter of player, num of rows, num of cols,
                num of matches, position as i, j
    User Input: none
    Prints:     nothing
    Returns:    True if k-match pattern is found for player's letter across
                the col (corresponding to i,j, and
                False otherwise.
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    match = 1
    for num in range(cols):
        if i+num+1 >= rows:
            break
        if board[i+num+1][j] == letter:
            match = match + 1
        else:
            break
    if match >= matches:
        return True
    else:
        return False


def check_diagonal_right(board: List[List[str]],
                         letter: str,
                         rows: int,
                         cols: int,
                         matches: int,
                         i: int,
                         j: int) -> bool:
    '''
    Test:       09_check_diagonal_right.py
    Purpose:    checks if player's letter is in all the adjacent k
                (number_of_matches)
                positions across right leaning diagonals.
    Parameters: board, letter of player, num of rows, num of cols,
                num of matches, position as i, j
    User Input: none
    Prints:     nothing
    Returns:    True if k-match pattern is found for player's letter across
                the right diagonal (corresponding to i,j, and
                False otherwise.
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    match = 1
    for num in range(matches):
        if num+i+1 < rows and j+num+1 < cols:
            if board[i+num+1][j+num+1] == letter:
                match = match + 1
            if board[i+num+1][j+num+1] != letter:
                break
    if match >= matches:
        return True
    else:
        return False


def check_diagonal_left(board: List[List[str]], letter: str, rows: int,cols: int, matches: int, i: int, j: int) -> bool:
    '''
    Test:       08_check_diagonal_left.py
    Purpose:    checks if player's letter is in all the adjacent k
                (number_of_matches)
                positions across right leaning diagonals.
    Parameters: board, letter of player, num of rows, num of cols,
                num of matches, position as i, j
    User Input: none
    Prints:     nothing
    Returns:    True if k-match pattern is found for player's letter across
                the left diagonal (corresponding to i,j, and
                False otherwise.
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    match = 1
    for num in range(matches):
        if i+num+1 < rows and j-num-1 >= 0:
            if board[i+num+1][j-num-1] == letter:
                match = match +1
            if board[i+num+1][j-num-1] != letter:
                break
    if match >= matches:
        return True
    else:
        return False


def is_winner(board: List[List[str]], letter: str, rows: int, cols: int, matches: int) -> bool:
    '''
    Test:       We give you this one.
    Purpose:    determines if the player has won or not,
    Parameters: given a board, a player's letter, number of rows in board,
                number of columns in board,
                and number of matches needed for player's letter to win.
    User Input: none
    Prints:     nothing
    Returns:    True if k-matches for player's letter were found across any
                of the directions, and
                False otherwise.
    Modifies:   nothing
    Calls:      check_across, check_down,
                check_diagonal_right, check_diagonal_left
    '''
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == letter:
                if check_across(board, letter, rows, cols, matches, i, j):
                    return True
                if check_down(board, letter, rows, cols, matches, i, j):
                    return True
                if check_diagonal_right(board, letter, rows, cols, matches, i, j):
                    return True
                if check_diagonal_left(board, letter, rows, cols, matches, i, j):
                    return True
    return False


def get_board_copy(board: List[List[str]]) -> List[List[str]]:
    '''
    Test:       We give you this one.
    Purpose:    makes a copy of the board list and returns it.
    Parameters: board as list of list of strings
    User Input: none
    Prints:     nothing
    Returns:    a deep copy of the board!
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    board_copy: List[List[str]] = [[board[i][j] for j in range(len(board[i]))] for i in range(len(board))]
    return board_copy


def is_space_free(board: List[List[str]], row: int, col: int) -> bool:
    '''
    Test:       02_is_space_free_test.py
    Purpose:    can you make a move at the position of row, col?
    Parameters: board, candidate row and col
    User Input: none
    Prints:     nothing
    Returns:    True if the passed move is free on the passed board, and
                False otherwise.
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    return board[row][col] == ' '


def get_player_move(board: List[List[str]], rows: int, cols: int) -> Tuple[int, int]:
    '''
    Test:       03_get_player_move_test.py
    Purpose:    prompts for a valid player's move
    Parameters: board, num of rows, cols
                Take integer input on one row with spaces, eg., 1 2
    User Input: yes
    Prints:     "What is your next move? (0-rows, 0-cols)"
                where rows and cols are the size of your game.
                See test for formatting
    Returns:    tuple of 2 ints (the move)
    Modifies:   nothing
    Calls:      none of our functions (standard python ok)
    '''
    while True:
        print('What is your next move? (0-{}, 0-{})\n'.format(rows-1, cols-1))
        move = input().split()
        r, c = int(move[0]), int(move[1])
        if (0 <= r <= int(rows-1)) and (0 <= c <= int(cols - 1)) and (board[r][c] == ' '):
            return r, c


def choose_random_move_from_list(board: List[List[str]], moves_list: List[List[int]]) -> Tuple[int, int]:
    '''
    Test:       We give you this one, because it's seeded.
    Purpose:    pick random valid move
    Parameters: board, list of possible moves.
    User Input: none
    Prints:     nothing
    Returns:    a random computer move from the available moves
                as a tuplel of 2 ints.
    Modifies:   nothing
    '''
    random.seed(0)
    move = random.choice(moves_list)
    return move[0], move[1]


def get_empty_spaces(board: List[List[str]], rows: int, cols: int) -> List[List[int]]:
    '''
    Test:       05_get_empty_spaces_test.py
    Purpose:    Gets possible moves
    Parameters: board, number of rows and cols.
    User Input: none
    Prints:     nothing
    Returns:    List of possible moves where the cell is a space, where
                spaces should be in order of reading them out, e.g.,
                [[0, 0], [1, 1], [1, 2]]
    Modifies:   nothing
    '''
    spaces = []
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == ' ':
                spaces.append([i,j])
    return spaces


def get_computer_move(board: List[List[str]], computerletter: str, rows: int, cols: int, matches: int) -> Tuple[int, int]:
    '''
    Test:       None, relies on other functions and std-testing.
    Purpose:    Determines the computer's move using the following
                short-sighted algorithm:
                First, check if we can win in the next move,
                and if so, then win,
                Check if the player could win on next move,
                and if so, then block them,
                and if neither of those apply, retreive all empty spaces,
                and choose one at random as your move.
    Parameters: the computer's letter, number of rows of the board,
                the number of columns of the board, and number of matches.
    User Input: none
    Prints:     nothing
    Returns:    a computer's move.
    Modifies:   nothing
    '''
    playerletter = ''
    if computerletter == "X":
        playerletter = "O"
    else:
        playerletter = "X"
    for row in range(rows):
        for col in range(cols):
            boardcopy = get_board_copy(board)
            if is_space_free(board, row, col):
                make_move(boardcopy, computerletter, row, col)
                if is_winner(boardcopy, computerletter, rows, cols, matches):
                    return row, col
    for row in range(rows):
        for col in range(cols):
            boardcopy = get_board_copy(board)
            if is_space_free(board, row, col):
                make_move(boardcopy, playerletter, row, col)
                if is_winner(boardcopy, playerletter, rows, cols, matches):
                    return row, col
    spaces = get_empty_spaces(board, rows, cols)
    return choose_random_move_from_list(board, spaces)

def is_board_full(board: List[List[str]], rows: int, cols: int) -> bool:
    '''
    Test:       10_is_board_full_test.py
    Purpose:    checks if every space on the board has been taken.
    Parameters: board, number of rows, cols
    User Input: none
    Prints:     nothing
    Returns:    True if the board is full, and otherwise returns False.
    Modifies:   nothing
    '''
    for row in range(rows):
        for col in range(cols):
            if is_space_free(board, row, col):
                return False
    return True

def main() -> None:
    print("Welcome to m-n-k game!")

    while True:
        m: int = int(input("\nEnter number of rows, m: "))
        n: int = int(input("\nEnter number of columns, n: "))
        k: int = 0
        print("\nWhere k should be greater than 2 and should not be greater than m or n,")
        while k <= 2 or k > m or k > n:
            k = int(input("enter run length to win, k: \n"))
        the_board: List[List[str]] = [[" "] * n for i in range(m)]
        player_letter, computer_letter = input_player_letter()
        turn: str = who_goes_first()
        print("The " + turn + " will go first.\n")
        game_is_playing: bool = True

        while game_is_playing:
            if turn == "human player":
                draw_board(the_board, m, n)
                row: int
                col: int
                row, col = get_player_move(the_board, m, n)
                make_move(the_board, player_letter, row, col)

                if is_winner(the_board, player_letter, m, n, k):
                    draw_board(the_board, m, n)
                    print("Hooray! You have won the game!\n")
                    game_is_playing = False
                else:
                    if is_board_full(the_board, m, n):
                        draw_board(the_board, m, n)
                        print("The game is a tie!\n")
                        break
                    else:
                        turn = "computer"
            else:
                row, col = get_computer_move(the_board,
                                             computer_letter,
                                             m, n, k)
                make_move(the_board, computer_letter, row, col)

                if is_winner(the_board, computer_letter, m, n, k):
                    draw_board(the_board, m, n)
                    print("The computer has beaten you! You lose.")
                    game_is_playing = False
                else:
                    if is_board_full(the_board, m, n):
                        draw_board(the_board, m, n)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "human player"

        print("Do you want to play again? (y or n)")
        if not input().lower().startswith("y"):
            break


if __name__ == '__main__':
    main()
