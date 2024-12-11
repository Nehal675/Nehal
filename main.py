game_board=[[""for cell in range(3)]for row in range(3)]
def display_board(board):
    for row in board:
        print(" | ".join(cell if cell else " " for cell in row))
        print("-"*10)

def player_moves(board,current_player):
    while True:
        try:
            location = input(
                f"player {current_player} take your place by the number of row(0->2) and column(0->2) with space between them ")
            row, col = map(int, location.split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                return row, col
            else:
                print('Invalid entry This place is already occupied,try again.')
        except ValueError:
            print('Please make space between row and column number ')


def who_is_win(board,current_player):
        for row in board:
            if all(cell ==current_player for cell in row ):
                 return True
        for col in range(3):
            if all(board[row][col]==current_player for row in range(3)):
                 return True
        if all(board[i][i]==current_player for i in range(3)) or all(board[i][2-i]==current_player for i in range(3)):
            return True
        else:
            return False
def is_tie(board):
    if all(cell for row in board for cell in row):
        return True

def play_game(board):
    current_player="X"
    while True:
        display_board(board)
        row,col=player_moves(board,current_player)
        board[row][col]=current_player
        if who_is_win(board,current_player):
            display_board(board)
            print(f"player {current_player} win.")
            break
        if is_tie(board):
            display_board(board)
            print(f"No one won and tried again.")
            break
        current_player="O"if current_player=="X" else "X"
play_game(game_board)