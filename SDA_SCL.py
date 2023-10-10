# CREATED ON 8/4/23
# @AUTHOR -> ARYA

from tkinter import*
import smbus2
import serial
from PIL import Image, ImageTk
import time
from datetime import datetime
import pytz
import requests
import threading
root=Tk()
root.geometry("800x500")
root.resizable(False,False) 
root.title("DASHBOARD")
# removing the title bar
root.overrideredirect(True)
def move_app(e):
        root.geometry(f'+{e.x_root}+{e.y_root}')

IST= pytz.timezone('Asia/Kolkata')
p1=Image.open("/home/rem/Desktop/dash_board.png")

resize_dash=p1.resize((800,500),Image.LANCZOS)
put_dash= ImageTk.PhotoImage(resize_dash)

#...........DASH BOARD..............................
label_dash=Label(root,image=put_dash)
label_dash.place(x=0,y=0)

# .........PERFORM ANY LABELLING BUTTONS ETC OVER DASH BOARD IMAGE.....

# button to close the window coz we dont have title bar to close it
my_button=Button(root,text="X",font=("Helvetica,10"),command=root.quit)
my_button.place(x=755,y=5)

# .......................S P E E D O M E T E R......................
label_for_speed=Label(root,text="distance",font="valera 23",width=5,height=2)
label_for_speed.place(x=127,y=244)
bus =smbus2.SMBus(1)

i2c_1=0x08
print("arduino connected")                                       

def update_label_speed():
    data = bus.read_i2c_block_data(i2c_1,0,2)
    # print(data[0])

    label_for_speed.config(text=data[0],fg="#ffffff",bg="#000000")
    root.after(800,update_label_speed)
update_label_speed()

# .................................................................
# TIME & DATE
label_date = Label(text="Current Date", font = 'Fjalla 22',bg="#000000", fg="#ffffff")
label_date.place(x=120, y=32)

label_time = Label(text="Current Time", font = 'Fjalla 18',bg="#000000", fg="#ffffff")
label_time.place(x=120, y=68)

# ..........................................................

def update_clock():
            raw_TS = datetime.now(IST)
            date_now = raw_TS.strftime("%d %b %Y")
            time_now = raw_TS.strftime("%H:%M:%S %p")
            formatted_now = raw_TS.strftime("%d-%m-%Y")
            label_date.config(text = date_now)
            label_time.config(text = time_now)
            label_time.after(1000, update_clock)
            return formatted_now
update_clock()

# # >>>>>>>>>>>>>>>>>S E N D I N G     D A T A    BY    S D A   AND   S C L   PINS<<<<<<<<<<<<<<<<<<<<
# ADDRESS FOR I2C
I2C_ADDRESS=9


haz1=Image.open("/home/rem/Desktop/hazard.png")
haz2=haz1.resize((95,95),Image.LANCZOS)
haz3=ImageTk.PhotoImage(haz2)

wiper1=Image.open("/home/rem/Desktop/wi.png")
wiper2=wiper1.resize((75,45),Image.LANCZOS)
wiper3=ImageTk.PhotoImage(wiper2)

hl_1=Image.open("/home/rem/Desktop/head.png")
hl_2=hl_1.resize((70,65),Image.LANCZOS)
hl_3=ImageTk.PhotoImage(hl_2)

left=Image.open("/home/rem/Desktop/l.png")
right=Image.open("/home/rem/Desktop/r.png")
neutral=Image.open("/home/rem/Desktop/wi.png")

re_left=left.resize((45,45),Image.LANCZOS)
re_right=right.resize((45,45),Image.LANCZOS)
re_neutral=neutral.resize((45,45),Image.LANCZOS)

left_ready=ImageTk.PhotoImage(re_left)
right_ready=ImageTk.PhotoImage(re_right)
neutral_ready=ImageTk.PhotoImage(re_neutral)

label_haz=Label(root,text="haz")
label_haz.place(x=3420,y=3100)

label_indi=Label(root, image=neutral_ready)
label_indi.place(x=4370,y=3400)

label_head_light=Label(root,text="head")
label_head_light.place(x=5420,y=3250)

label_wiper=Label(root,text="wi")
label_wiper.place(x=5400,y=4500)

# time.sleep(5)
# head_data.reset_input_buffer()
print("done connected headlight")


def update_label_head():
    data=bus.read_i2c_block_data(I2C_ADDRESS,0,2)
    mydata=(data[0]*256)+data[1]
    print(mydata)
    if mydata==0:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=neutral_ready,background="black")
        label_indi.place(x=3420,y=1000) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500) 


    elif mydata==1:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=342,y=10)
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=neutral_ready,background="black")
        label_indi.place(x=3420,y=1000) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500) 

    elif mydata==10:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=left_ready,background="black")
        label_indi.place(x=437,y=340) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500)

    elif mydata==100:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=neutral_ready,background="black")
        label_indi.place(x=3420,y=1000) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)

    elif mydata==1000:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=neutral_ready,background="black")
        label_indi.place(x=3420,y=1000) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500)

    elif mydata==1001:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=342,y=10)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=neutral_ready,background="black")
        label_indi.place(x=3420,y=1000) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500)
    elif mydata==1010:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=left_ready,background="black")
        label_indi.place(x=437,y=340) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500)
    elif mydata==1100:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=right_ready,background="black")
        label_indi.place(x=6640,y=3400) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)
    elif mydata==1101:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=342,y=10)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=right_ready,background="black")
        label_indi.place(x=6640,y=3400) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)
    elif mydata==1110:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=left_ready,background="black")
        label_indi.place(x=437,y=340)  
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)

    elif mydata==101:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=342,y=10)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=left_ready,background="black")
        label_indi.place(x=4370,y=3400)  
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)
    elif mydata==20:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=right_ready,background="black")
        label_indi.place(x=664,y=340) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500)
    elif mydata==1020:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=right_ready,background="black")
        label_indi.place(x=664,y=340) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=5400,y=4500)
    elif mydata==120:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=right_ready,background="black")
        label_indi.place(x=664,y=340) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)
    elif mydata==1120:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=542,y=325) 
        label_indi.config(image=right_ready,background="black")
        label_indi.place(x=664,y=340) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)
    elif mydata==110:
        label_haz.config(image=haz3,background="black")
        label_haz.place(x=3420,y=1000)   #no haz
        label_head_light.config(image=hl_3,background="black")
        label_head_light.place(x=5420,y=3250) 
        label_indi.config(image=left_ready,background="black")
        label_indi.place(x=437,y=340) 
        label_wiper.config(image=wiper3,background="black")
        label_wiper.place(x=540,y=410)
        
    root.after(500,update_label_head)

update_label_head()

root.mainloop()
