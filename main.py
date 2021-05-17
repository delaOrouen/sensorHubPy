#!/usr/bin/python
'''
Developer: Rouen de la O
Purpose: This is a program designed to operate a raspberry pi as a SPI master.
This master will read from a SPI slave which is connected to a variety of
sensors. This program will use a defined encoding to read a series of data from
the SPI device.
'''

import sys
import smbus2 as smbus  # smbus2
import time

I2C_SLAVE_ADDRESS = 26 # 0x1a
MESSAGE = "Hello World!"



def main():
    I2Cbus = smbus.SMBus(1)
    slaveSelect = 1
    slaveAddress = I2C_SLAVE_ADDRESS
    bytesToSend = createSendingMessage(MESSAGE)
    sending = False
    
    while True:
        if (sending):
            I2Cbus.write_i2c_block_data(slaveAddress, 0x00, bytesToSend)
            print("sent data:", MESSAGE)
        else:
            try:
                data = I2Cbus.read_i2c_block_data(slaveAddress, 0x00, 16)
                print("data received: ")
                print(data)
            except:
                print("remote i/o error")
                time.sleep(0.5)
    


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
                  
