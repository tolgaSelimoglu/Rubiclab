import twophase.solver as sv
from collections import Counter
import os


def print_exp(path):
    """
        Prints moves with explanations

        Arguments:
            path : string, path to move explanations

        Prints:
            Move explanations line by line

        Returns:
            None
    """

    with open(path, "r") as f:
        for line in f:
            print("\n" + line.strip())


def moves_to_b_format(moves, target_path):
    """
        Convert moves to b'*' format

        Arguments:
            moves : List, list that contains moves as string
            target_path : string, path for encoded moves

        Prints:
            None

        Returns:
            None
    """

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



def moves_to_hand(moves, target_path):
    """
        Convert moves to explained versions

        Arguments:
            moves : List, list that contains moves as string
            target_path : string, path for explained moves

        Prints:
            None

        Returns:
            None
    """

    encoded_lines = []

    dict = {
        'U1': "Turn Upper Face 1 time clockwise",
        'U2': "Turn Upper Face 2 times clockwise or counterclockwise",
        'U3': "Turn Upper Face 1 times counterclockwise",
        'D1': "Turn Down Face 1 time clockwise",
        'D2': "Turn Down Face 2 times clockwise or counterclockwise",
        'D3': "Turn Down Face 1 times counterclockwise",
        'L1': "Turn Left Face 1 time clockwise",
        'L2': "Turn Left Face 2 times clockwise or counterclockwise",
        'L3': "Turn Left Face 1 times counterclockwise",
        'R1': "Turn Right Face 1 time clockwise",
        'R2': "Turn Right Face 2 times clockwise or counterclockwise",
        'R3': "Turn Right Face 1 times counterclockwise",
        'F1': "Turn Front Face 1 time clockwise",
        'F2': "Turn Front Face 2 times clockwise or counterclockwise",
        'F3': "Turn Front Face 1 times counterclockwise",
        'B1': "Turn Back Face 1 time clockwise",
        'B2': "Turn Back Face 2 times clockwise or counterclockwise",
        'B3': "Turn Back Face 1 times counterclockwise"
    }



    for move in moves:
        encoded_lines.append(dict[move[:2]])

    with open(target_path, 'w') as f:
        for line in encoded_lines:
            f.write(f'{line}\n')


def predict_moves(cubestring, moves = 0, time = 5):
    """
        Predict moves to solve cube using twophasesolver

        Arguments:
            cubestring : string,
            moves : int, expected number of moves to solve cube
            time : int, expected time to solve cube

        Prints:
            None

        Returns:
            sol_moves : List, moves list to solve the cube
    """

    solution = sv.solve(cubestring, moves, time)

    sol_moves = solution.split(" ")

    move_count = len(sol_moves) - 1

    return sol_moves[:move_count]


def count_letters(cubestring):
    """
        Count every letter to determine if the cube is solvable

        Arguments:
            cubestring : string, string that contains cube colours as letters

        Prints:
            None

        Returns:
            letter_count : List, letter counts
    """

    letter_count = Counter(char.lower() for char in cubestring if char.isalpha())
    return letter_count


def get_string(path):
    """
        Reads and returns cubes colours as string from txt file

        Arguments:
            path : string, path for cube colours

        Prints:
            None

        Returns:
            cubestring : string, string that contains cube colours
    """

    cubestring = ''
    with open(path, 'r') as f:
        cubestring = f.read()

    return cubestring[0:54]


def check_letter_counts(dict):
    """
        Checks that are all colours have 9 of each

        Arguments:
            dict : dictionary, dict that contains letter counts

        Prints:
            None

        Returns:
            cubestring : string, string that contains cube colours
    """

    letters = ['b', 'f', 'd', 'u', 'l', 'r']
    for letter in letters:
        assert dict[letter] == 9, \
            f'\nThere must be exactly 9 pieces of each color.' \
            f'\nThere are {dict[letter]} numbers labeled {letter}.'

def solve(path, target_path1, target_path2):
    """
        Calls necessary functions to solve

        Arguments:


        Prints:
            None

        Returns:
            
    """


    cubestring = get_string(path)
    counts = count_letters(cubestring)
    check_letter_counts(counts)
    moves = predict_moves(cubestring)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(moves)
    assert isinstance(moves, list), \
        f'\nSolving moves should be a list.\nMoves : {moves}'
    assert moves[0] != 'Error:', \
        f'\nCube is unsolvable\nText : {moves}'
    moves_to_b_format(moves, target_path1)
    moves_to_hand(moves, target_path2)
