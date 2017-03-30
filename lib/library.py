import random
import json
import os
from lib.dict import Dict


class Library(object):
    def __init__(self):
        self.list = Archive().data

    def get_text_by_id(self, id):
        """Returns text from Library list[id]"""
        if -len(self.list) <= id and id < len(self.list):
            return self.list[id]['text']
        else:
            return "Wrong index XD"

    def getrandom(self, difficulty=None):
        """Returns random text from Library list"""
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


class Archive(object):
    def __init__(self):
        self.data = None
        self.__default = Default()
        self._dirpath = os.path.dirname(os.path.realpath(__file__))
        self._path = os.path.join(self._dirpath, self.__default.filename)

        # check if file exists
        if not os.path.exists(self._path):
            self.data = self.__default.get_default_list()
            # create default file
            self.dump()
        else:
            # Load the file
            self.load()
            # Merge with existing file
            self.merge_with_default()
            # Save changes
            self.dump()

    def merge_with_default(self):
        # texts already in file
        texts = [dic['text'] for dic in self.data]
        for dic in self.__default.get_default_list():
            # found new in default list
            if dic['text'] not in texts:
                # add new text
                self.data.append(
                    # add default values if keys are missing
                    self.__default.correctdict(dic)
                )

    def dump(self):
        if self.data is None:
            raise Exception('Nothing to dump: list in library is empty')
        with open(self._path, mode='w') as f:
            json.dump(
                self.data,
                f,
                ensure_ascii=False,
                indent=4,
                sort_keys=True
            )

    def load(self):
        """Read file(list of dicts) and
        process every dict by saving only usefull keys and
        setting default keys if missing"""
        with open(self._path) as f:
            self.data = json.load(f)
            if type(self.data) is not list:
                raise TypeError('Loaded file is not a list: {}'.format(type(self.data)))
            # make sure its in right format
            for i, dic in enumerate(self.data):
                self.data[i] = self.__default.correctdict(dic)


class Default(object):
    """Here we've got default info about file with texts"""

    def __init__(self):
        self.filename = '.typingtraininglib.json'
        self.__defaultlist = []

    def correctdict(self, dic):
        dic = Dict(dic)
        dic.difficulty = dic.get('difficulty', 0)
        dic.text = dic.get('text', 'EMPTY')
        return dic

    def get_default_list(self):
        self.__quick_add(
            text="You will all be running. In a world you cannot hide. And the end is coming. For the lemming standing in line.",
            difficulty=0)
        self.__quick_add(
            text="Overcoming. Let the fury build inside. It could all be broken. If you only opened your eyes",
            difficulty=0)
        self.__quick_add(
            text="def __init__(self, arg): super(ClassName, self).__init__()",
            difficulty=1)
        self.__quick_add(
            text="for ind4x, v4L in enumerate(2 ** _285 for _285 in l492)",
            difficulty=1)
        self.__quick_add(
            text="wariancja V(X) = E(X^2) - E(X)^2",
            difficulty=1)
        self.__quick_add(
            text="As I survey the chaos, taking in the lack of raw humanity. It's as if the entire world's fallen in love with their insanity. Hear the innocent voices scream. As their tormentors laugh through all of it. No forgiveness from all I've seen. A degradation I cannot forget",
            difficulty=1)
        self.__quick_add(
            text="Raw emotion, pure devotion. They will testify. And our memory will endure for all time. Never hiding, no dividing. Let them witness us move as one now. Show no mercy, let the world see. We're invincible. Show them nothing is beyond our control. Take it higher, our desire. Will determine what we've become now",
            difficulty=1)
        self.__quick_add(
            text="qo29*328s@xcsa^0-[]-;-/+1421d()ED#b6X&x*^@",
            difficulty=2)
        self.__quick_add(
            text="#En0rm0u$11",
            difficulty=2)
        return self.__defaultlist

    def __quick_add(self, **kwargs):
        """This function allows adding new fields (like 'text') without need of changing older texts"""
        dic = self.correctdict(kwargs)
        self.__defaultlist.append(dic)
