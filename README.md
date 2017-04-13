# Main idea / What is does?

Tool/Game providing a way to practise typing without looking at the keyboard or just speed and correctness.


# How to run?

**in development, so keep in mind that whole project can change dramaticly**

Clone or fork this repo. Both python 2.X and 3.X should work. (Tested under linux, dunno if windows can handle colors in cmd)
Use 'typingtraining' as an entry point. Pick one:

    $ python3 typingtraining
    $ python  typingtraining
    $ ./typingtraining


# How to use?

## Options:
1. without any : displays random text from textlist.json file
2. -d or --difficulty [{0,1,2}, ...] : specify difficulty
3. -r or --random-chars : displays bunch of random characters; without any difficulty set uses hardest mode; -d 0 uses just lowercase letters, -d 1 adds uppers and digits, -d 2 adds also specials

## You can add your own texts manually by editing textlist.json
If it does not exist then run typingtraining so it will create it for you. Delete that file if u messed with it too much.

## If you need help or want to learn more: run with --help


# Functionality

1. Display block of text, mark current character. Follow what user types. Mark 'red' or 'green' accordingly. Allow to use Backspace. Allow to skip some characters.
2. Gather info about speed and correctness. Show them after completion
3. Read those 'blocks of text' from json file with more info about them. Let filter or search. Mark with difficulty: polish language, more numbers, numbers mixed with weird characters, etc.


# ToDo

1. Long text
2. non-stop-mode

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
    + **gettextbyid**:
    + **getrandom**: *difficulty -> str* - returns random text filtered by difficulty. Difficulty should be int or iterable object of int's

4. **Archive**:
    - **dirpath**: *str* - absolute path to script directory
    - **path**: *str* - absolute path to file with texts
    + **load**: *() -> None* - loads file with texts (file initialized together with class)
    

5. **Default**:

