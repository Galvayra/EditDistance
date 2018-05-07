import sys
from os import path

try:
    import EditDistance
except ImportError:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from EditDistance.dataset.dataHandler import MyDataHandler

if __name__ == '__main__':
    data_handler = MyDataHandler()
    data_handler.pre_processing()
