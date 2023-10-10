from tkinter import *
import serial
from PIL import Image, ImageTk
import time


root=Tk()
root.geometry("800x500")

p1=Image.open("dash_board.png")

resize_dash=p1.resize((800,500),Image.LANCZOS)
put_dash= ImageTk.PhotoImage(resize_dash)

# DATA
l1=Label(root,image=put_dash)


l1.place(x=0,y=0)
l2=Label(root,text="sensor",font="valera 12",width=8,height=2)
l2.place(x=640,y=205)
# Label_Update..................
# label=Label(root,text="sensor value",width=80,height=80)
# label.pack()
# label.place(x=250,y=250)


# serial_data
sdata=serial.Serial('/dev/ttyUSB0',9600,timeout=1.0)
time.sleep(5)

sdata.reset_input_buffer()
print("arduino connected")

def update_label():
    sensor_value=sdata.readline().decode('utf-8').rstrip()
    l2.config(text=sensor_value,fg="#ffffff",bg="#000000")
    root.after(100,update_label)

update_label()




root.mainloop()
