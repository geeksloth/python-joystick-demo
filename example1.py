"""
Author: GeekSloth
This script initializes and runs an event loop to handle joystick events using the pyjoystick.sdl2 library.
It defines functions to print messages when a joystick is attached or detached, and to handle key events from the joystick.
The key_received function processes various joystick inputs such as buttons, hats (D-pad), and axes, and prints corresponding messages.
Functions:
- print_add(joy): Prints a message when a joystick is attached.
- print_remove(joy): Prints a message when a joystick is detached.
- key_received(key): Handles key events from the joystick and prints corresponding messages based on the key type and value.
The script runs the event loop with the defined functions to handle joystick events.
"""
from pyjoystick.sdl2 import Key, Joystick, run_event_loop


def print_add(joy):
    print('Attatched', joy)

def print_remove(joy):
    print('Detatched', joy)

def key_received(key):
    if key.keytype == Key.BUTTON and key.number == 0:   # A
        if key.value == 1:
            print('A pressed')
        else:
            print('A released')
    elif key.keytype == Key.BUTTON and key.number == 1:   # B
        if key.value == 1:
            print('B pressed')
        else:
            print('B released')
    elif key.keytype == Key.BUTTON and key.number == 2:   # X
        if key.value == 1:
            print('X pressed')
        else:
            print('X released')
    elif key.keytype == Key.BUTTON and key.number == 3:   # Y
        if key.value == 1:
            print('Y pressed')
        else:
            print('Y released')
    elif key.keytype == Key.BUTTON and key.number == 4:   # LB
        if key.value == 1:
            print('LB pressed')
        else:
            print('LB released')
    elif key.keytype == Key.BUTTON and key.number == 5:   # RB
        if key.value == 1:
            print('RB pressed')
        else:
            print('RB released')
    elif key.keytype == Key.BUTTON and key.number == 6:   # BACK
        if key.value == 1:
            print('BACK pressed')
        else:
            print('BACK released')
    elif key.keytype == Key.BUTTON and key.number == 7:   # START
        if key.value == 1:
            print('START pressed')
        else:
            print('START released')
    elif key.keytype == Key.BUTTON and key.number == 8:   # LSB
        if key.value == 1:
            print('LSB pressed')
        else:
            print('LSB released')
    elif key.keytype == Key.BUTTON and key.number == 9:   # RSB
        if key.value == 1:
            print('RSB pressed')
        else:
            print('RSB released')
    elif key.keytype == Key.BUTTON and key.number == 10:   # GUIDE
        if key.value == 1:
            print('GUIDE pressed')
        else:
            print('GUIDE released')
    elif key.keytype == Key.HAT and key.value == 0:     # DPAD RELEASED
        print('DPAD released')
    elif key.keytype == Key.HAT and key.value == 1:     # DPAD UP
        print('DPAD UP')
    elif key.keytype == Key.HAT and key.value == 3:     # DPAD UP-RIGHT
        print('DPAD UP-RIGHT')
    elif key.keytype == Key.HAT and key.value == 2:     # DPAD RIGHT
        print('DPAD RIGHT')
    elif key.keytype == Key.HAT and key.value == 6:     # DPAD DOWN-RIGHT
        print('DPAD DOWN-RIGHT')
    elif key.keytype == Key.HAT and key.value == 4:     # DPAD DOWN
        print('DPAD DOWN')
    elif key.keytype == Key.HAT and key.value == 12:     # DPAD DOWN-LEFT
        print('DPAD DOWN-LEFT')
    elif key.keytype == Key.HAT and key.value == 8:     # DPAD LEFT
        print('DPAD LEFT')
    elif key.keytype == Key.HAT and key.value == 9:     # DPAD UP-LEFT
        print('DPAD UP-LEFT')
    elif key.keytype == Key.AXIS and key.number == 2:   # LT
        print('LT value:', key.value)
    elif key.keytype == Key.AXIS and key.number == 5:   # RT
        print('RT value:', key.value)
    elif key.keytype == Key.AXIS and key.number == 0:   # LSX
        print('LSX value:', key.value)
    elif key.keytype == Key.AXIS and key.number == 1:   # LSY
        print('LSY value:', key.value)
    elif key.keytype == Key.AXIS and key.number == 3:   # RSX
        print('RSX value:', key.value)
    elif key.keytype == Key.AXIS and key.number == 4:   # RSY
        print('RSY value:', key.value)
    else:
        print('Unknown key:', key)

run_event_loop(print_add, print_remove, key_received)