# --------------------------------------------
# PyCan 2.0.0 [X]
# This file handles everything related to writing stuff down
# Copyright (C) 2023 celeste-42bit (Caeleste) & hayleyInSpace (Hayley Silver)
# REPO: https://github.com/celeste-42bit/pycan-2
# REPO: https://github.com/celeste-42bit/pycan-2/docs.md
# Firmware version : rp2-pico-20220618-v1.19.1.uf2
# --------------------------------------------

def log(logtype, content):
    if logtype == "log":
        with open("log.txt", "a+") as log:
            log.write(content + "\n")
    elif logtype == "data":
        with open("data.txt", "a+") as data:
            data.write(content + "\n")