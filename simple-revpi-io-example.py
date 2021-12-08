#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Simple Revpi IO Example 
# Uses revpimodio library https://revpimodio.org by Sven Sager
#
# Prerequisites:
# - Use a RevPi Core or Connect and attach and configure a DIO Module
#
# Note: revpimodio2 comes already pre-installed on the official revolution pi raspbian os images

# Import the python library for revolution pi
import revpimodio2

# Create an instance of revpimodio
rpi = revpimodio2.RevPiModIO(autorefresh=True)

# Read the value from input 1
I_1 = rpi.io.I_1.value
print("Input I_1 has value: " + str(I_1))

# Activate the output O_1
rpi.io.O_1.value = 1
print("Output O_1 was set to value 1")