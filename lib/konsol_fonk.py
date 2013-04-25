#!/usr/bin/env python
#-*-coding:utf-8-*-

import os


def addToClipBoard(text):
    #  Panoya kopyala
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)