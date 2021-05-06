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
    spi.open(CONST_SPI_BUS, CONST_SPI_DEVICE)
    spi.max_speed_hz = 976000  # somewhat conservative value
    sensor_hub_data = []  # empty array of arrays
    sensor_hub_data[0] = ['H'] * CONST_FIRST_DATA_LENGTH  # empty array
    sensor_hub_data[1] = ['-1'] * 4

    while True:
        sensor_hub_data[0] = spi.read(CONST_FIRST_DATA_LENGTH)
        print(str(sensor_hub_data[0]))
        time.sleep(1)  # wait one second


main()
