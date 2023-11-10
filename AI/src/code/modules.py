import twophase.solver as sv
from collections import Counter


def moves_to_binary(moves, target_path):

    encoded_lines = []

    dict = {
            'U1' : b'a', 'U2' : b'b', 'U3' : b'c',
            'D1' : b'd', 'D2' : b'e', 'D3' : b'f',
            'L1' : b'g', 'L2' : b'h', 'L3' : b'i',
            'R1' : b'j', 'R2' : b'k', 'R3' : b'l',
            'F1' : b'm', 'F2' : b'n', 'F3' : b'o',
            'B1' : b'p', 'B2' : b'q', 'B3' : b'r'
            }


    for move in moves:
        encoded_lines.append(dict[move[:2]])

    with open(target_path, 'w') as f:
        for move in encoded_lines:
            f.write(f'{move}\n')


def predict_moves(cubestring, moves = 0, time = 5):

    solution = sv.solve(cubestring, moves, time)

    sol_moves = solution.split(" ")

    move_count = len(sol_moves) - 1

    return sol_moves[:move_count]


def count_letters(string):
    letter_count = Counter(char.lower() for char in string if char.isalpha())
    return letter_count


def get_string(path):

    string = ''
    with open(path, 'r') as f:
        string = f.read()

    return string[0:54]

def check_letter_counts(dict):
    letters = ['b', 'f', 'd', 'u', 'l', 'r']
    for letter in letters:
        assert dict[letter] == 9, \
            f'\nThere must be exactly 9 pieces of each color.' \
            f'\nThere are {dict[letter]} numbers labeled {letter}.'

def solve(path, target_path):

    cubestring = get_string(path)
    counts = count_letters(cubestring)
    check_letter_counts(counts)
    moves = predict_moves(cubestring)
    assert isinstance(moves, list), \
        f'\nSolving moves should be a list.\nMoves : {moves}'
    assert moves[0] != 'Error:', \
        f'\nCube is unsolvable\nText : {moves}'
    moves_to_binary(moves, target_path)
