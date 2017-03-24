#!/usr/bin/env python3
import curses


def main(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    stdscr.addch(height - 1, width - 1, ord('o'))
    # for h in range(height - 1):
    #     for w in range(width):
    #         stdscr.addch(h, w, ord('x'))

    # for i in range(11):
    #     v = i - 11
    #     stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10 / v))

    stdscr.refresh()
    stdscr.getkey()


if __name__ == '__main__':
    curses.wrapper(main)
