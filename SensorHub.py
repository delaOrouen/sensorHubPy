
'''
Developers: Christian Lancaster, Rouen de la O

Summary of the class
'''
# TODO: verify functionality


import time
from gpiozero import LED
import serial


class SensorHub:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS, timeout=1)
        self.interrupt = LED(23)
        self.rdata = ""

    # sending bytes over uart us non-functional -- results in hardfault
    # def sendBytes(self, bytesToSend):
    #     self.I2Cbus.write_i2c_block_data(self.peripheralAddress, 0x00, bytesToSend)

    def readBytes(self, num_bytes):
        self.interrupt.on()
        # consider adding a small delay?
        newData = str(self.ser.read(num_bytes))
#         print(self.rdata)
        self.interrupt.off()
        if (self.rdata == "b\'\'"):
            return self.rdata # "-1"
        else:
            self.rdata = newData[2:-1]
            return newData

    # this function may be unused
    # def listToString(self, myList):
    #     newString = ""
    #     for character in myList:
    #         newString += chr(character)
    #     return newString

    # this function may be unused
    # def createSendingMessage(self, sendingMessage):
    #     byteList = []
    #     for character in sendingMessage:
    #         byteList.append(ord(character))
    #     return byteList
