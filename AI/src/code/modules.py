import twophase.solver as sv


def moves_to_binary(moves, target_path):

    encoded_lines = []

    dict = {
            'U1' : '00001', 'U2' : '00010', 'U3' : '00011',
            'D1' : '00101', 'D2' : '00110', 'D3' : '00111',
            'L1' : '01001', 'L2' : '01010', 'L3' : '01011',
            'R1' : '01101', 'R2' : '01110', 'R3' : '01111',
            'F1' : '10001', 'F2' : '10010', 'F3' : '10011',
            'B1' : '11001', 'B2' : '11010', 'B3' : '11011'
            }


    for move in moves:
        encoded_lines.append(dict[move[:2]])

    with open(target_path, 'w') as f:
        for move in encoded_lines:
            f.write(f'{move}\n')


def predict_moves(path, moves = 0, time = 5):

    cubestring = ''
    with open(path, 'r') as f:
        cubestring = f.read()

    cubestring = cubestring[0:54]

    solution = sv.solve(cubestring, moves, time)

    sol_moves = solution.split(" ")

    move_count = len(sol_moves) - 1

    return sol_moves[:move_count]


def solve(path, target_path):

    moves = predict_moves(path)
    print(moves)
    moves_to_binary(moves, target_path)
