import random
import json
import os
from lib.dict import Dict


class Library(object):
    def __init__(self):
        self.list = Archive().data

    def get_all(self, shorter=False):
        return "\n".join(
            ": ".join([str(i), val['text']])
            for i, val in enumerate(self.list)
        )

    def get_text_by_id(self, id):
        """Returns text from Library list[id]"""
        if -len(self.list) <= id and id < len(self.list):
            return self.list[id]['text']
        else:
            return "Wrong index XD"

    def getrandom(self, difficulties=set()):
        """Returns random text from Library list"""
        # transform param to set
        difficulties = self.__transform(difficulties)
        # get list of wanted texts
        textlist = [
            elem.text for elem in self.list
            if len(difficulties) == 0 or None in difficulties or elem.difficulty in difficulties
        ]
        if len(textlist) > 0:
            return textlist[random.randrange(0, len(textlist))]
        else:
            return "*No records*"

    def get_random_chars(self, difficulties=set()):
        """Returns random sequence of characters based on difficulties"""
        # transform param to set
        difficulties = self.__transform(difficulties)

        def chars_range(a, z):  # [a, z]
            return [chr(ord(a) + i) for i in range(ord(z) - ord(a) + 1)]
        lchars = chars_range('a', 'z')
        uchars = chars_range('A', 'Z')
        digits = chars_range('0', '9')

        chars = lchars  # base case
        size = 40
        if sum(difficulties) > 0:
            chars += uchars
            chars += digits
        if sum(difficulties) > 1:
            chars += Default.special_chars

        res = []
        import random
        for i in range(size):
            if random.randrange(5) == 0:  # randomly split with space
                res.append(' ')
            res.append(chars[random.randrange(len(chars))])
        return "".join(res)

    def __transform(self, difficulties):
        """Transform difficulties param to set if needed"""
        if type(difficulties) is not set:
            # maybe its iterable
            try:
                difficulties = set(difficulties)
            # its not iterable
            except TypeError:
                difficulties = {difficulties}
        return difficulties


class Archive(object):
    def __init__(self):
        self.data = None
        self._path = os.path.join(Default.dirpath, Default.filename)

        # check if file exists
        if not os.path.exists(self._path):
            self.data = Default.get_default_list()
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
        for dic in Default.get_default_list():
            # found new in default list
            if dic['text'] not in texts:
                # add new text
                self.data.append(
                    # add default values if keys are missing
                    Default.correctdict(dic)
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
            # self.data = json.load(f)
            self.data = Default.correctdata(json.load(f))


class Default(object):
    """Here we've got default info about file with texts"""
    filename = os.path.join('..', 'textlist.json')
    dirpath = os.path.dirname(os.path.realpath(__file__))
    texts_filename = os.path.join(dirpath, '.typingtraining_archive.json')

    special_chars = """!@#$%^&*()_-=+{}[]|\:;"',<>./?"""

    def __new__(s):
        return None

    @staticmethod
    def correctdata(data):
        if type(data) is not list:
            raise TypeError('Loaded file is not a list: {}'.format(type(data)))
        # make sure its in right format
        res = []
        for i, dic in enumerate(data):
            res.append(Default.correctdict(dic))
        return res

    @staticmethod
    def correctdict(dic):
        dic = Dict(dic)
        dic.difficulty = dic.get('difficulty', 0)
        dic.text = dic.get('text', 'EMPTY')
        return dic

    @staticmethod
    def get_default_list():
        with open(Default.texts_filename) as f:
            return Default.correctdata(json.load(f))
