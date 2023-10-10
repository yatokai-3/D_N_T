from tkinter import *
import serial
from PIL import Image, ImageTk
import time

root=Tk()
root.geometry("800x500")


# Label_Update..................
p1=Image.open("dash_board.png")

resize_dash=p1.resize((300,300),Image.LANCZOS)
put_dash= ImageTk.PhotoImage(resize_dash)

# DATA
label_dash=Label(root,image=put_dash,text="data")
label_dash.pack()


label_dash=Label(root,text="58").place(x=300,y=250)

sdata=serial.Serial('/dev/ttyUSB0', 9600,timeout=1.0)
time.sleep(2)

sdata.reset_input_buffer()
print("arduino connected")
# only one at a time...to catch serial output either through arduino or rspi

def update_label():
    sensor_value=sdata.readline().decode('utf-8').rstrip()
    label_dash.config(text="Sensor_value: "+sensor_value)
    root.after(100,update_label)

update_label()
root.mainloop()





