import serial
import time

def serial_stuff(moves_path):

    def yazdir():
        data = ser.readlines()

    moves = []

    with open(moves_path, 'r') as file:
        for line in file:
            moves.append(line.strip())  # Append each line without the trailing newline character
    print(moves)


    ser = serial.Serial('COM11', 9600, timeout=1, bytesize=8, parity='N', stopbits=1)
    time.sleep(2)

    for buffer in moves:
        ser.write(buffer)
        yazdir()

    ser.close()
