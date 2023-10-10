# import smbus2
# import time
# bus = smbus2.SMBus(1)

# address = 0x08

# while True:
    
#     data = bus.read_byte(address)
#     print (data)
#     # data = bus.read_i2c_block_data(address, 0, 2)
#     # speed = data[0] << 8 | data[1]
#     # print(speed)
#     time.sleep(1)
# import smbus2
# from tkinter import *

# # I2C configuration
# bus = smbus2.SMBus(1)

# arduino_address = 0x09

# # Tkinter GUI setup
# root = Tk()
# root.title("Speed Display")
# label = Label(root, text="Speed: ")
# label.pack()

# def update_speed():
#     # Read the speed value from Arduino over I2C
#     try:
#         speed_bytes = bus.read_i2c_block_data(arduino_address, 0, 2)
#         speed = speed_bytes[0] << 8 | speed_bytes[1]
#         label.config(text="Speed: " + str(speed))
#     except IOError:
#         label.config(text="Error: Failed to read speed")

#     # Schedule the next update
#     root.after(1000, update_speed)

# # Start the speed update loop
# update_speed()



# # Run the Tkinter event loop
# root.mainloop()

# import smbus2

# address = 9  # Arduino I2C address
# register = 0  # Register to read from (0 = speed data)

# bus = smbus2.SMBus(1)  # Use /dev/i2c-1 for Raspberry Pi 2 or 3 (or /dev/i2c-0 for Raspberry Pi 1)

# def read_speed():
#     high_byte = bus.read_byte_data(address, register)
#     low_byte = bus.read_byte_data(address, register + 1)
#     speed = (high_byte << 8) | low_byte
#     return speed

# while True:
#     try:
#         speed = read_speed()
#         print("Received speed:", speed, "km/h")
#     except IOError:
#         print("I2C communication error")

import smbus2
import time 

i2c = 0x08
bus = smbus2.SMBus(1)  

# def read_data():

        # Read the data from Arduino
    # data = bus.read_i2c_block_data(arduino_address, 0, 2)
    # # value = struct.unpack('h', bytes(data))[0]
    # return value
while True:
    data = bus.read_i2c_block_data(i2c, 0, 2)
    # data=bus.read_byte(arduino_address)

    # value = struct.unpack('h', bytes(data))[0]
    # Read the data from Arduino
    # received_data = read_data()
    # data=bus.read_byte(i2c)
    # lb=bus.read_byte(i2c)
      
    # print("Received Data: ",(data))
    print("Received Data: ",(data[0]*256)+data[1])
    time.sleep(0.5)

