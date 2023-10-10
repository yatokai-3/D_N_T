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

#      ...  . . . . . . .... ......... ........ ..... . . . . . . . 
#....................... PLACEMENTS........................
# # RIGHT_INDICATOR....
# p1=Image.open("r.png")
# img_resize1=p1.resize((45,45),Image.LANCZOS)
# img1=ImageTk.PhotoImage(img_resize1)
# right_label=Label(root,image=img1,width=45,height=45,background="black")
# # right_label.pack()
# # right_label.place(x=664,y=340)

# # LEFT INDICATOR..................................
# p2=Image.open("l.png")
# img_resize2=p2.resize((45,45),Image.LANCZOS)
# img2=ImageTk.PhotoImage(img_resize2)
# left_label=Label(root,image=img2,width=45,height=45,background="black")
# # left_label.pack()
# # left_label.place(x=437,y=340)

# WIPER INDICATOR.................................
# p3=Image.open("wi.png")
# img_resize3=p3.resize((50,50),Image.LANCZOS)
# img3=ImageTk.PhotoImage(img_resize3)
# wiper_label=Label(root,image=img3,width=74,height=53,background="black")
# wiper_label.pack()
# wiper_label.place(x=540,y=405)

# # HEAD_LIGHT.......................................
# p4=Image.open("head.png")
# img_resize4=p4.resize((50,50),Image.LANCZOS)
# img4=ImageTk.PhotoImage(img_resize4)
# head_label=Label(root,image=img4,width=70,height=53,background="black")
# # head_label.pack()
# # head_label.place(x=540,y=335)

# ..........SERIAL COMMUNICATION...............
def update_label_speed():
    sensor_value=speed_data.readline().decode('utf-8').rstrip()
    label_for_speed.config(text=sensor_value,fg="#ffffff",bg="#000000")
    root.after(100,update_label_speed)

update_label_speed()
# >>>>>>>>>>>>>>>>>>>> INDICATOR <<<<<<<<<<<<<<<<<<<<<<<<<
left=Image.open("l.png")
right=Image.open("r.png")
neutral=Image.open("wi.png")

re_left=left.resize((45,45),Image.LANCZOS)
re_right=right.resize((45,45),Image.LANCZOS)
re_neutral=neutral.resize((45,45),Image.LANCZOS)

left_ready=ImageTk.PhotoImage(re_left)

right_ready=ImageTk.PhotoImage(re_right)
neutral_ready=ImageTk.PhotoImage(re_neutral)

label_indi=Label(root, image=neutral_ready)
label_indi.place(x=43700,y=34000)

indicator_data=serial.Serial('/dev/ttyUSB0',9600,timeout=1.0)
time.sleep(5)
indicator_data.reset_input_buffer()
print("done connected indicator")

def update_label_indi():
    while True:
        mydata=indicator_data.readline().decode('utf-8').rstrip()
        if mydata=="10":
            # l1.config(text='|  <  |')
            label_indi.config(image=left_ready,background="black")
            label_indi.place(x=437,y=340)
        elif mydata=="1":
            # l1.config(text='|  >  |')
            label_indi.config(image=right_ready,background="black")
            label_indi.place(x=664,y=340)
        else:
            # l1.config(text='|     |') 
            label_indi.config(image=neutral_ready)
            label_indi.place(x=9000,y=9000)

 

# >>>>>>>>>>>>>>>>>>>>> HEAD LIGHT + WIPER INDICATION <<<<<<<<<<<<<<<<<<<<<<<<<<<<
hl_1=Image.open("head.png")
wi_1=Image.open("wi.png")

hl_2=hl_1.resize((70,65),Image.LANCZOS)
wi_2=wi_1.resize((70,60),Image.LANCZOS)

wi_3=ImageTk.PhotoImage(wi_2)
hl_3=ImageTk.PhotoImage(hl_2)


label_head_light=Label(root,text="head")
label_head_light.place(x=54000,y=33500)

label_wiper=Label(root,text="wiper")
label_wiper.place(x=1000,y=1000)

head_data=serial.Serial('/dev/ttyACM0',9600,timeout=1.0)
time.sleep(5)
head_data.reset_input_buffer()
print("done connected headlight")

def update_label_head():
    while True:
        mydata=head_data.readline().decode('utf-8').rstrip()
        if mydata=="0":
            # l1.config(text='|  <  |')
            label_head_light.config(image=hl_3,background="black")
            label_wiper.config(image=wi_3,background="black")

            label_head_light.place(x=542,y=325)
            label_wiper.place(x=540,y=405)

        elif mydata=="1":
            label_head_light.config(image=hl_3,background="black")
            label_wiper.config(image=wi_3,background="black")

            label_head_light.place(x=54200,y=32500)
            label_wiper.place(x=540,y=405)
        
        elif mydata=="10":
            label_head_light.config(image=hl_3,background="black")
            label_wiper.config(image=wi_3,background="black")

            label_head_light.place(x=542,y=325)
            label_wiper.place(x=54000,y=45000)
        elif mydata=="11":
            label_head_light.config(image=hl_3,background="black")
            label_wiper.config(image=wi_3,background="black")

            label_head_light.place(x=54200,y=32500)
            label_wiper.place(x=54000,y=45000)

i2c_thread=threading.Thread(target=update_label_head)
i2c_thread.daemon=True
i2c_thread.start()

i2c_thread_1=threading.Thread(target=update_label_indi)
i2c_thread_1.daemon=True
i2c_thread_1.start() 