from tkinter import *
import threading
import serial
from PIL import Image, ImageTk
import time
import pytz

root=Tk()
root.geometry("800x500")
root.resizable(False,False)

IST= pytz.timezone('Asia/Kolkata')
p1=Image.open("dash_board.png")

resize_dash=p1.resize((800,500),Image.LANCZOS)
put_dash= ImageTk.PhotoImage(resize_dash)

#...........DASH BOARD..............................
label_dash=Label(root,image=put_dash)
label_dash.place(x=0,y=0)

# root=Tk()
# root.geometry("800x500")

left=Image.open("l.png")
right=Image.open("r.png")
neutral=Image.open("wi.png")

re_left=left.resize((45,45),Image.LANCZOS)
re_right=right.resize((45,45),Image.LANCZOS)
re_neutral=neutral.resize((45,45),Image.LANCZOS)

left_ready=ImageTk.PhotoImage(re_left)
right_ready=ImageTk.PhotoImage(re_right)
neutral_ready=ImageTk.PhotoImage(re_neutral)

l1=Label(root, image=neutral_ready)
# l1.place(x=150,y=150)
# l1.config(image=neutral)
# l1.pack()

sdata=serial.Serial('/dev/ttyACM0',9600,timeout=1.0)
time.sleep(5)
sdata.reset_input_buffer()
print("done connected")

def update_label():
    while True:
        mydata=sdata.readline().decode('utf-8').rstrip()
        if mydata=="10":
            # l1.config(text='|  <  |')
            l1.config(image=left_ready)
            l1.place(x=150,y=150)
        elif mydata=="1":
            # l1.config(text='|  >  |')
            l1.config(image=right_ready)
            l1.place(x=150,y=150)
        else:
            # l1.config(text='|     |')
            l1.config(image=neutral_ready)
            l1.place(x=900,y=900)

i2c_thread=threading.Thread(target=update_label)
i2c_thread.daemon=True
i2c_thread.start()

root.mainloop()




