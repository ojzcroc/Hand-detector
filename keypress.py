from subprocess import Popen, PIPE

control_f4_sequence = '''keydown Control_L
key F4
keyup Control_L
'''

shift_a_sequence = '''keydown Shift_L
key Up
keyup Shift_L
'''

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

keypress(shift_a_sequence)
keypress(control_f4_sequence)
