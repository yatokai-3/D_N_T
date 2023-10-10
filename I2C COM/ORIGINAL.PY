from tkinter import *
import serial
from PIL import Image, ImageTk
import time


sdata=serial.Serial('/dev/ttyUSB0',9600,timeout=1.0)
time.sleep(5)

sdata.reset_input_buffer()
print("arduino connected")

while True:
    time.sleep(0.01)
    if sdata.in_waiting>0:
        # WAY U READ YOUR DATA...........
        mydata=sdata.readline().decode('utf-8').rstrip()
        print(mydata)