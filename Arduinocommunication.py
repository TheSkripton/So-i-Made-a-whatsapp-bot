import serial
import time
global SE
SE= serial.Serial('COM5',9600)
SE.write("c".encode())
time.sleep(2)
def do(thing):
    SE.write(thing.encode())
    print(thing)


