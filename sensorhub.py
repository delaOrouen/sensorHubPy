# TODO: verify functionality

import sys
import smbus2 as smbus  # smbus2
import time

class SensorHub():
    def __init__(self, addr):
        self.I2Cbus = smbus.SMBus(1)
        self.peripheralAddress = addr
    
    def sendBytes(self, bytesToSend):
        self.I2Cbus.write_i2c_block_data(self.peripheralAddress, 0x00, bytesToSend)
        
    def recvBytes(self):
        return self.I2Cbus.read_i2c_block_data(self.peripheralAddress, 0x00, 16)