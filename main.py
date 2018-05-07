import sys
from os import path

try:
    import EditDistance
except ImportError:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from EditDistance.str2edit import MyEditDistance

if __name__ == '__main__':
    ed = MyEditDistance()
    ed.get_distance()
