#!/usr/bin/env python

'''Test that font colour is applied correctly.   Default font should
appear blue.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: COLOR.py 932 2007-06-25 05:41:34Z Alex.Holkner $'

import unittest
import base_text

from pyglet import font

class TEST_COLOR(base_text.TextTestBase):
    def render(self):
        fnt = font.load(self.font_name, self.font_size)
        self.label = font.Text(fnt, self.text, 10, 10, color=(0, 0, 1, 1))

if __name__ == '__main__':
    unittest.main()
