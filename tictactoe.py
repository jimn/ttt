

symbols = {
    0: '_',
    1: '❌',
    2: '⭕'
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

    declare_winner(current_player)

def player_go(player):
    while True:
        move = input(f"Player {player} Enter a row and column like \"A1\"").strip().lower()
        column = move[0]
        if column not in ['a', 'b', 'c']:
            continue 
        try:
            row = int(move[1])
        except ValueError:
            continue
        if row < 1 or row > 3:
            continue
        
        # update grid
        
        return


def print_grid():
    r_number = 1
    print("  A B C")
    for row in grid:
        print(f"{r_number} {symbols[row[0]]} {symbols[row[1]]} {symbols[row[2]]} ")
        r_number = r_number + 1

def we_have_a_winner():
    ...

def declare_winner(player):
    ...

main()    