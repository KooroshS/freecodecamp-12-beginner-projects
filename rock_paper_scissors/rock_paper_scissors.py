import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie."

    if is_win(user, computer):
        return "You have won!"

    return "You have lost :,)"

def is_win(player, opponent):
    # return True if play wins.
    # r>s, s>p, p>r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True
    
print(play())