import time
from player import HumanPlayer, RandomComputerPlayer

class TickTacToe:
    def __init__(self):
        # We will use a single list to represent our board
        self.board = [" " for _ in range(9)]
        self.current_winner = None # This keeps track of the winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| ", " | ".join(row), " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 and the other numbers that each correspond with a box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| ", " | ".join(row), " |")

    def available_moves(self):
        # return []
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves
       
    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")
    
    def make_move(self, square, letter):
        # if a valid move, make the move and return True
        # else: return False
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner = three in any shape
        # let's first check for rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # let's check the column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Let's check the diagonals
        # this will happen only if the move is an even number...
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True
        
        # if all of the checks fail
        return False

    
def play(game, x_player, o_player, print_game=True):
    # Rerturn winner(its letter) or in case of a tie None.
    if print_game:
        game.print_board_nums()

    letter = "X" # the start letter for the game
    # Now let's iterate until there are no available spots for continuing
    # don't worry about winning, we will break out of the loop then
    while game.empty_squares():
        # Get the move from the appropriate player.

        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # A function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("") # an empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            # After making the move we should alternate letters
            letter = "O" if letter == "X" else "X"

        # a tiny break
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")
    
if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TickTacToe()
    play(t, x_player, o_player, print_game=True)