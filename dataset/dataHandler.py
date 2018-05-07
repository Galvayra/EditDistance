from .variables import *
import re


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
            print("File not found Error!\n\n")
            return False

    def pre_processing(self):
        lines = self.__read_corpus()
        
