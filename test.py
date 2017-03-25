import curses
from lib.library import Library
from lib.textobject import TextObject
from lib.tracker import Tracker


def blocking_exit(stdscr):
    stdscr.addstr('To proceed press "BACKSPACE" key...', curses.color_pair(3))
    stdscr.refresh()
    while 'KEY_BACKSPACE' != stdscr.getkey():
        pass


def main(stdscr):
    if curses.has_colors():
        # height, width = stdscr.getmaxyx()
        lib = Library()
        tracker = Tracker(TextObject(lib.getrandom(0)))
        tracker.start_tracking(stdscr)
        tracker.summarize(stdscr)
        blocking_exit(stdscr)
    else:
        stdscr.addstr('This terminal does not support colors')
        stdscr.refresh()
        stdscr.getkey()


if __name__ == '__main__':
    curses.wrapper(main)
