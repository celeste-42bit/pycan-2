# --------------------------------------------
# PyCan 2.0.0 [X]
# This is the main class!
# Copyright (C) 2023 celeste-42bit (Caeleste) & hayleyInSpace (Hayley Silver)
# REPO: https://github.com/celeste-42bit/pycan-2
# REPO: https://github.com/celeste-42bit/pycan-2/docs.md
# Firmware version : rp2-pico-20220618-v1.19.1.uf2
# --------------------------------------------

from machine import Pin, I2C
from logger import log
import utime

#sda = Pin(0)
#scl = Pin(1)
led = Pin(25, Pin.OUT) ; led.off()


i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 1000000)
devices = I2C.scan(i2c)
print("I2C scan : ", devices)
if len(devices) == 2:
    log(log, "All devices recognized")
else:
    log(log, "device error!")
print("Done")