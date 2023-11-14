import sys
import os
from src.code.modules import solve, print_exp
from src.code.picStuff import take_pic
from src.code.masking import moves_to_urfdlb
from src.code.serialPort import serial_stuff

def main():

    take_pic("src/data/")
    moves_to_urfdlb("src/data/", "src/data/cube_colours.txt")
    solve("src/data/cube_colours.txt", "src/data/moves_encoded.txt", "src/data/moves_with_exp.txt")
    # serial_stuff("src/data/moves_encoded.txt")
    print_exp("src/data/moves_with_exp.txt")

if __name__ == "__main__":
    main()
