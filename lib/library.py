import random
import json
import os


class Library(object):
    def __init__(self):
        self.__default = Default()
        self._dirpath = os.path.dirname(os.path.realpath(__file__))
        self._path = os.path.join(self._dirpath, self.__default.filename)
        self.list = None

        # check if file exists
        if os.path.exists(self._path):
            return

        # create default file
        self.createdefault()

    def createdefault(self):
        # with open(self._path, mode='w', encoding='utf-8') as f:
        # without encoding cuz python2
        with open(self._path, mode='w') as f:
            json.dump(
                self.__default.getdefaultlist(),
                f,
                ensure_ascii=False,
                indent=4,
                sort_keys=True
            )

    def load(self):
        # with open(self._path, encoding='utf-8') as f:
        # without encoding cuz python2
        with open(self._path) as f:
            self.list = json.load(f)
            if type(self.list) is not list:
                raise TypeError('Loaded file is not a list: {}'.format(type(self.list)))

    def getrandom(self, difficulty=None):
        # Load the file if it is not loaded
        if self.list is None:
            self.load()

        # transform param to set
        if type(difficulty) is not set:
            # maybe its iterable
            try:
                difficulty = set(difficulty)
            # its not iterable
            except TypeError:
                difficulty = {difficulty}

        # get list of wanted texts
        textslist = [
            elem['text'] for elem in self.list
            if difficulty is None or
            elem['difficulty'] in difficulty
        ]

        return textslist[random.randrange(0, len(textslist))]


class Default(object):
    """Here we've got default info about file with texts"""

    def __init__(self):
        self.filename = '.typingtraininglib.json'
        self.__defaultlist = []

    def getdefaultlist(self):
        self.__quickAdd(
            text="You will all be running. In a world you cannot hide. And the end is coming. For the lemming standing in line.",
            difficulty=0)
        self.__quickAdd(
            text="Overcoming. Let the fury build inside. It could all be broken. If you only opened your eyes",
            difficulty=0)
        self.__quickAdd(
            text="def __init__(self, arg): super(ClassName, self).__init__()",
            difficulty=1)
        self.__quickAdd(
            text="for ind4x, v4L in enumerate(2 ** _285 for _285 in l492)",
            difficulty=1)
        self.__quickAdd(
            text="wariancja V(X) = E(X^2) - E(X)^2",
            difficulty=1)
        self.__quickAdd(
            text="As I survey the chaos, taking in the lack of raw humanity. It's as if the entire world's fallen in love with their insanity. Hear the innocent voices scream. As their tormentors laugh through all of it. No forgiveness from all I've seen. A degradation I cannot forget",
            difficulty=1)
        self.__quickAdd(
            text="Raw emotion, pure devotion. They will testify. And our memory will endure for all time. Never hiding, no dividing. Let them witness us move as one now. Show no mercy, let the world see. We're invincible. Show them nothing is beyond our control. Take it higher, our desire. Will determine what we've become now",
            difficulty=1)
        self.__quickAdd(
            text="qo29*328s@xcsa^0-[]-;-/+1421d()ED#b6X&x*^@",
            difficulty=2)
        self.__quickAdd(
            text="#En0rm0u$11",
            difficulty=2)

        return self.__defaultlist

    def __quickAdd(self, **kwargs):
        """This function allows adding new fields (like 'text') without need of changing older texts"""
        self.__defaultlist.append({})
        self.__defaultlist[-1]['difficulty'] = kwargs.get('difficulty', 0)
        self.__defaultlist[-1]['text'] = kwargs.get('text', 'EMPTY')
