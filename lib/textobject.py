import curses


class TextObject(object):
    """Handles text with its coloring and displaying"""

    def __init__(self, text):
        self.text = text
        self.colorsarray = [0 for _ in self.text]

        # Initialize colors
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)

    def display(self, stdscr):
        stdscr.clear()
        for i, char in enumerate(self.text):
            if char not in '\n\r\t':
                color = self.colorsarray[i]
                stdscr.addch(char, curses.color_pair(color))
        stdscr.addch('\n')
        stdscr.refresh()

    def cleanchar(self, index):
        self.__changecolor(index, 0)

    def wrongchar(self, index):
        self.__changecolor(index, 1)

    def okchar(self, index):
        self.__changecolor(index, 2)

    def currentchar(self, index):
        self.__changecolor(index, 3)

    def __changecolor(self, index, color):
        if 0 <= index and index < len(self.text):
            self.colorsarray[index] = color
