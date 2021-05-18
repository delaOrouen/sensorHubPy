#!/usr/bin/python
'''
Developer: Rouen de la O


pin configuration is enabled/disabled at /boot/config.txt
'''

#import sys
#import smbus2 as smbus  # smbus2
import time
import serial
from gpiozero import LED

# I2C_SLAVE_ADDRESS = 0x1a # 0x1a, 26
MESSAGE = "Hello World!"



def main():
    ser = serial.Serial("/dev/ttyS0", baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
    interrupt = LED(16)
    while True:
        interrupt.on()
        # consider adding a small delay?
        rdata = ser.read(50)
        print(rdata)
        interrupt.off()
        time.sleep(.010)
        


def listToString(myList):
    newString = ""
    for character in myList:
        newString += chr(character)
    return newString

def createSendingMessage(sendingMessage):
    byteList = []
    for character in sendingMessage:
       byteList.append(ord(character))
    return byteList

main()

# i2c main
# def main():
#     I2Cbus = smbus.SMBus(1)
#     time.sleep(1)
#     slaveSelect = 1
#     slaveAddress = I2C_SLAVE_ADDRESS
#     bytesToSend = createSendingMessage(MESSAGE)
#     sending = False
#     convertedData = ""
#     
#     while True:
#         if (sending):
#             I2Cbus.write_i2c_block_data(slaveAddress, 0x00, bytesToSend)
#             print("sent data:", MESSAGE)
#         else:
#             try:
#                 data = I2Cbus.read_i2c_block_data(slaveAddress, 0x00, 12)
#                 if (data[0] != 211):
#                     print("data received: ", data)
#                     convertedData = listToString(data)
#                     print("               ", convertedData)
#                     time.sleep(0.1)
#             except:
#                 print("remote i/o error")
#                 time.sleep(0.5)
                  
