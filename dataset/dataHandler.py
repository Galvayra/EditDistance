from .variables import *
import re
import json
from collections import OrderedDict


class MyDataHandler:
    def __init__(self):
        self.__data_dict = dict()

    @property
    def data_dict(self):
        return self.__data_dict

    @staticmethod
    def __read_corpus():
        try:
            with open(dir_path + corpus_path, 'r') as r_file:
                lines = r_file.readlines()
                return lines
        except FileNotFoundError:
            print("Can not find read file!\n\n")
            return False

    def __set_data_dict(self, plist):
        for word in plist:
            word = word.split('/')
            key = word[0].lower()
            value = word[1]

            if key not in self.__data_dict:
                self.data_dict[key] = [value]
            else:
                if value not in self.data_dict[key]:
                    self.data_dict[key].append(value)

    def pre_processing(self):
        lines = self.__read_corpus()
        p = re.compile("[A-Za-z]+/[A-Za-z]+")

        for line in lines:
            self.__set_data_dict(p.findall(line))

    def print_dict(self):
        keys = sorted(self.data_dict.keys())

        print("\n===============================\n")
        print("Vocab Size -", len(keys), "\n\n")
        for key in keys:
            print(key.ljust(15), self.data_dict[key])

    def dump(self):
        def __sorted(data_dict):
            dump_dict = OrderedDict()

            for key in sorted(data_dict.keys()):
                dump_dict[key] = data_dict[key]

            return dump_dict

        try:
            with open(dir_path + save_path, 'w') as w_file:
                json.dump(__sorted(self.data_dict), w_file, indent=4)
                print("\n\nSuccess Save File !! \n")
                print("File name is", "'" + save_path + "'", "in the", "'" + dir_path[:-1] + "'", "directory", "\n\n")
        except FileNotFoundError:
            print("Can not save dump file!\n\n")
