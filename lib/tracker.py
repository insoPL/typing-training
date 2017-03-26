import time
import curses
import math


class Tracker(object):
    """Contains 'game loop', where TextObject is being changed
accordingly to correctness of typed characters by the user.
Also prints summary of the game"""

    def __init__(self, Textobj):
        self.textobj = Textobj
        self.stats = {
            'misses': 0,
            'typedkeys': 0,
            'starttime': None,
            'finishtime': None
        }

    def summarize(self, stdscr):
        d = self.stats
        t = math.floor(d['finishtime'] - d['starttime'] + 0.5)
        keys = d['typedkeys']
        misses = d['misses']

        stdscr.addch(ord('#'), curses.color_pair(1))
        stdscr.addstr('Missed chars = {}\n'.format(misses))

        stdscr.addch(ord('#'), curses.color_pair(1))
        stdscr.addstr('Typed chars  = {}\n'.format(keys))

        stdscr.addch(ord('#'), curses.color_pair(1))
        stdscr.addstr('Accuracy     = {}%\n'.format((keys - misses) * 100 // keys))

        stdscr.addch(ord('#'), curses.color_pair(1))
        stdscr.addstr('Time elapsed = {}s\n'.format(t))

        stdscr.addch(ord('#'), curses.color_pair(1))
        stdscr.addstr('Keys_per_min = {}\n'.format((keys * 60) // t))

        stdscr.refresh()

    def start_tracking(self, stdscr):
        # Points to current character
        ptr = 0

        # Highlight current character
        self.textobj.currentchar(0)

        while ptr < len(self.textobj.text):
            self.textobj.display(stdscr)

            key = stdscr.getkey()
            self.stats['typedkeys'] += 1

            # Start time after first typed char
            if self.stats['starttime'] is None:
                self.stats['starttime'] = time.time()

            # correct
            if self.textobj.text[ptr] == key:
                self.textobj.okchar(ptr)
                ptr += 1

            # backspace
            elif key == 'KEY_BACKSPACE':
                if ptr > 0:
                    self.textobj.cleanchar(ptr - 1)
                    self.textobj.cleanchar(ptr)
                    # self.text.clean_char(ptr + 1)
                    ptr -= 1

            # miss
            else:
                self.textobj.wrongchar(ptr)
                ptr += 1
                self.stats['misses'] += 1

            # Highlight current character
            self.textobj.currentchar(ptr)

        self.stats['finishtime'] = time.time()

        self.textobj.display(stdscr)
