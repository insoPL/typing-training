import curses
import time
import math


class Tracker(object):
    """
    Handles main loop: track correctness, adjust colors
    Also gathers statistics
    """

    def __init__(self, stdscr, Text_obj):
        self.stdscr = stdscr
        self.text = Text_obj
        self.stats = {
            'misses': 0,
            'typed_keys': 0,
            'start_time': None,
            'finish_time': None
        }

    def summarize(self, stdscr):
        d = self.stats
        t = math.floor(d['finish_time'] - d['start_time'] + 0.5)
        keys = d['typed_keys']

        stdscr.addch('#', curses.color_pair(1))
        stdscr.addstr('Missed chars = {}\n'.format(d['misses']))

        stdscr.addch('#', curses.color_pair(1))
        stdscr.addstr('Typed chars  = {}\n'.format(keys))

        stdscr.addch('#', curses.color_pair(1))
        stdscr.addstr('Time elapsed = {}s\n'.format(t))

        stdscr.addch('#', curses.color_pair(1))
        stdscr.addstr('Keys_per_min = {}\n'.format((keys * 60) // t))

        stdscr.refresh()

    def start_tracking(self):
        # Points to current character
        ptr = 0

        # Highlight current character
        self.text.current_char(0)

        while ptr < len(self.text.string):
            self.text.display(self.stdscr)

            key = self.stdscr.getkey()
            self.stats['typed_keys'] += 1

            # Start time after first typed char
            if self.stats['start_time'] is None:
                self.stats['start_time'] = time.time()

            # correct
            if self.text.string[ptr] == key:
                self.text.ok_char(ptr)
                ptr += 1

            # backspace
            elif key == 'KEY_BACKSPACE':
                if ptr > 0:
                    self.text.clean_char(ptr - 1)
                    self.text.clean_char(ptr)
                    # self.text.clean_char(ptr + 1)
                    ptr -= 1

            # miss
            else:
                self.text.wrong_char(ptr)
                ptr += 1
                self.stats['misses'] += 1

            # Highlight current character
            self.text.current_char(ptr)

        self.stats['finish_time'] = time.time()

        self.text.display(self.stdscr)


class Text(object):
    """
    Contains structure for block of text.
    Handles colors and changes to certain characters
    """

    def __init__(self, text):
        self.string = text
        self.colors_array = [0 for _ in self.string]

        # Initialize colors
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)

    def display(self, stdscr):
        stdscr.clear()
        for i, char in enumerate(self.string):
            if is_printable(char):
                color = self.colors_array[i]
                stdscr.addch(char, curses.color_pair(color))
        stdscr.addch('\n')
        stdscr.refresh()

    def clean_char(self, index):
        self.__change_color(index, 0)

    def wrong_char(self, index):
        self.__change_color(index, 1)

    def ok_char(self, index):
        self.__change_color(index, 2)

    def current_char(self, index):
        self.__change_color(index, 3)

    def __change_color(self, index, color):
        if 0 <= index and index < len(self.string):
            self.colors_array[index] = color


tmp_s = 'Initialize curses and call'  # another callable object, func, which should be the rest of your curses-using application. If the application raises an exception, this function will restore the terminal to a sane state before re-raising the exception and generating a traceback.'


def is_printable(c):
    return c not in '\n\t\r'


def blocking_exit(stdscr):
    stdscr.addstr('To proceed press "BACKSPACE" key...', curses.color_pair(3))
    stdscr.refresh()
    while 'KEY_BACKSPACE' != stdscr.getkey():
        pass


def main(stdscr):
    if curses.has_colors():
        # height, width = stdscr.getmaxyx()
        tracker = Tracker(stdscr, Text(tmp_s))
        tracker.start_tracking()
        tracker.summarize(stdscr)
        blocking_exit(stdscr)
    else:
        stdscr.addstr('This terminal does not support colors')
        stdscr.refresh()
        stdscr.getkey()


if __name__ == '__main__':
    curses.wrapper(main)
