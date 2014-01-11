#!/usr/bin/env python

from subprocess import Popen, PIPE
import nxt.locator
from nxt.sensor import *

b = nxt.locator.find_one_brick()
uparrow = '''keydown Up
keyup Up
'''
downarrow = '''keydown Down
keyup Down
'''
wkey = '''keydown w
keyup w
''' 
skey = '''keydown s
keyup s
''' 
def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)
while 1 == 1:
	if Ultrasonic(b, PORT_4).get_sample() <= 25:
		keypress(wkey)
	elif Ultrasonic(b, PORT_4).get_sample() <= 40:
		print ""
	elif Ultrasonic(b, PORT_4).get_sample() >= 40:
		keypress(skey)
