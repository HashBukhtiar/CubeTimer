from random import *

def generate_3x3_scramble(scramble_length):
    # Make a WCA-eligible scramble for the 3x3x3 Rubik's Cube
    # int -> str

    scramble = ["placeholder"]
    possible_moves = ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", "U", "U'", "U2", "D", "D'", "D2"]
    for _ in range(scramble_length):
        while True:
            next_move = possible_moves[randrange(0, len(possible_moves))]
            if next_move[0] != scramble[-1][0]:
                break
        
        if scramble[0] == "placeholder":
            scramble[0] = next_move
        else:
            scramble.append(next_move)

    return " ".join(scramble)

def get_scramble(event_type):
    # Get scramble based on chosen event type
    # str -> str

    SCRAMBLE_LENGTH_3x3 = 20

    if event_type == "3x3":
        return generate_3x3_scramble(SCRAMBLE_LENGTH_3x3)