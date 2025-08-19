import sys

symbols = {
    0: '_',
    1: 'X',
    2: 'O'
}

grid = [[0,0,0], [0,0,0], [0,0,0]]

def main():
    current_player = 1
    while True:
        print_grid()
        player_go(current_player)
        if we_have_a_winner():
            break
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

    if current_player == 1:
        print("Hooray, Player One is victorious!")
    else:
        print("Hoorah, Player Two is victorious!")

def player_go(player):
    while True:
        try:
            move = input(f"Player {player} Enter a row and column like \"A1\": ").strip().lower()
        except IndexError:
            continue
        except EOFError:
            sys.exit("Game cancelled.")
        if move[0] not in ['a', 'b', 'c']:
            continue 
        try:
            row_number = int(move[1])
        except ValueError:
            continue
        if row_number < 1 or row_number > 3:
            continue
        
        # convert row and column input to index numbers
        if move[0] == 'a':
            column = 0
        elif move[0] == 'b':
            column = 1
        else:
            column = 2
        row = row_number - 1
        
        # check that the row / column aren't taken already
        if grid[row][column] != 0:
            print("That move is taken")
            continue

        # update the grid
        grid[row][column] = player
        
        return


def print_grid():
    r_number = 1
    print("  A B C")
    for row in grid:
        print(f"{r_number} {symbols[row[0]]} {symbols[row[1]]} {symbols[row[2]]} ")
        r_number = r_number + 1

def we_have_a_winner():
    # there are 8 possible wins for each player
    # all the As
    if grid[0][0] != 0 and (grid[0][0] == grid[1][0] == grid[2][0]):
        return True
    # all the Bs
    if grid[0][1] != 0 and (grid[0][1] == grid[1][1] == grid[2][1]):
        return True
    # all the Cs
    if grid[0][2] != 0 and (grid[0][2] == grid[1][2] == grid[2][2]):
        return True
    # all the 1s
    if grid[0][0] != 0 and (grid[0][0] == grid[0][1] == grid[0][2]):
        return True
    # all the 2s
    if grid[1][0] != 0 and (grid[1][0] == grid[1][1] == grid[1][2]):
        return True
    # all the 3s
    if grid[2][0] != 0 and (grid[2][0] == grid[2][1] == grid[2][2]):
        return True
    # diagonal left to right
    if grid[0][0] != 0 and (grid[0][0] == grid[1][1] == grid[2][2]):
        return True
    # diagonal right to left 
    if grid[0][2] != 0 and (grid[0][2] == grid[1][1] == grid[2][0]):
        return True
    return False

main()    