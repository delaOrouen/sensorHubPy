#!/usr/bin/python
'''
Developer: Rouen de la O
Purpose: This is a program designed to operate a raspberry pi as a SPI master.
This master will read from a SPI slave which is connected to a variety of
sensors. This program will use a defined encoding to read a series of data from
the SPI device.
'''

import spidev
import time

CONST_SPI_BUS = 0
CONST_SPI_DEVICE = 0  # we will probably only have 1 device, the stm32
CONST_FIRST_DATA_LENGTH = 12


def main():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 15600000
#     spi.cshigh = False # default false
    spi.lsbfirst = False # default false
    spi.mode = 0
    spi.threewire = False # default false
    
    sensor_hub_data = []  # empty list of different data types
    sensor_hub_data.insert(0,'H' * 12)  # empty array
    #sensor_hub_data = ['-1'] * 4
    print("sanity check:")
    print('Expecting sensor_hub_data[0] to be: [HHHHHHHHHHHH]')
    print("sensor_hub_data[0] = ", sensor_hub_data)

    print("\n beginning while loop in 1 second")
    time.sleep(1)
    recievedMessage = []
    sendingMessage = createSendingMessage("Hello world!")
    while True:
        #sensor_hub_data.insert(0, spi.readbytes(CONST_FIRST_DATA_LENGTH))
#         print(listToString(spi.readbytes(CONST_FIRST_DATA_LENGTH)))
#         spi.writebytes(['*'])
#         spi.writebytes()
        spi.writebytes(sendingMessage)
#         recievedMessage = spi.readbytes(12)
#         print("recieved message: ", recievedMessage)
#         for message in recievedMessage:
#             if (message == 40 or message == 20):
#                 print("Recieved Character: ", chr(message)),
#                 time.sleep(.3)  
        #print("sensor_hub_data = :", str(sensor_hub_data[0]))
#         time.sleep(.2)  # wait one second


def listToString(myList):
    newString = ""
    for character in myList:
        newString += chr(character)
    return newString

def createSendingMessage(sendingMessage):
    messageList = []
    for character in sendingMessage:
       messageList.append(ord(character)) 
    return messageList

main()
                  
