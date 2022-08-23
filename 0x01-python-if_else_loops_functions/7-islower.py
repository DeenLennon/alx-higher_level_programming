#!/usr/bin/python3
# Author: Abu Abdulwahab aka Deen Lennon
"""function that check for lower character"""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
