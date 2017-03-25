# Main idea / What is does?

Tool/Game providing a way to practise typing without looking at the keyboard (speed, correctness also).


# How to run?

TBD

# Functionality

1. Display block of text, mark current character. Follow what user types. Mark 'red' or 'green' accordingly. Allow to use Backspace. Allow to skip some characters.
2. Gather info about speed and correctness. Show them after completion
3. Read those 'blocks of text' from json file with more info about them. Let filter or search. Mark with difficulty: polish language, more numbers, numbers mixed with weird characters, etc.


# ToDo

1. Make full argparse thing
2. Design modes: (quick random, quick DIFF, choose by id, non-stop-mode, support for long text)
3. Print short representation of current library


# Components

1. **TextObject**:
    + **text**: *str* - block of text that will be written on screen
    - **colorsarray**: *list* - list of IDs of colors under corresponding indexes in *text*
    + **display**: *stdscr -> None* - handles displaying *text* on the screen
    - **changecolor**: *(index, color) -> None* - sets color under passed index if index is in [0, len(*text*))
    + **cleanchar**: *index -> None* - reset char under index to default state
    + **wrongchar**: *index -> None* - mark char under index as wrong
    + **okchar**: *index -> None* - mark char under index as ok
    + **currentchar**: *index -> None* - mark char under index as next character to be typed

2. **Tracker**:
    + **textobj**: *TextObject*
    + **stats**: *dict* - gathers informations about misses(number of misspelled characters), typedkeys(number of those), starttime and finishtime
    + **summarize**: *stdscr -> None* - prints informations after completion
    + **starttracking**: *stdscr -> None* - contains 'game loop'; changes elements in textobj accordingly to correctness of typed characters by the user; also gathers informations and stores them in *stats*

3. **Library**:
    - **dirpath**: *str* - absolute path to script directory
    - **path**: *str* - absolute path to file with texts
    + **load**: *() -> None* - loads file with texts (file initialized together with class)
    + **getrandom**: *difficulty -> str* - returns random text filtered by difficulty. Difficulty should be int or iterable object of int's
