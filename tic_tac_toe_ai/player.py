import math
import random

class Player:
    def __init__(self, letter):
        # letter is either x or o
        self.letter = letter

    # We want the players to make their first move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # We ought to find a vlid spot for our next move.
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            # we should check to be first an int and then a valid move.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid input, please try again.")

        return val
 
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # choose a move randomly
        else:
             # choose a move thoughtfully, based on minimax algorithm
            square = self.minimax(game, self.letter)["position"]
        return square
    
    def minimax(self, state, player):
        max_player = self.letter # yourself!
        other_player = "O" if player == "X" else "X"

        # we first want to check if the previous move was a winnder.
        # so this is our base case
        if state.current_winner == other_player:
            # we need to return position AND score because we need to keep track of the socre
            # for minimax to work
            return {"position": None,
                    "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares(): # no empty squares and no winner
            return {"position": None, "score": 0}
        
        if player == max_player:
            best = {"position": None, "score": -math.inf} # each score should be maximized (be larger)
        else:
            best = {"position": None, "score": math.inf} # each score should be minimized
        
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to stimulate a game after making that move
            sim_score = self.minimax(state, other_player) # Now, we alternate players

            # step 3: undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move # otherwise this will get messed up from the recursion

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score # replace score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score # replace score

        return best
