import sys
import os
from src.code.modules import solve
from src.code.picStuff import take_pic
from src.code.masking import moves_to_urfdlb
from src.code.serialPort import serial_stuff

def main():

    take_pic("src/data/")
    moves_to_urfdlb("src/data/", "src/data/cube_colours.txt")
    solve("src/data/cube_colours.txt", "src/data/moves_encoded.txt")
    serial_stuff("src/data/moves_encoded.txt")

if __name__ == "__main__":
    main()
