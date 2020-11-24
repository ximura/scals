import os.path
from typing import List, Set, Dict, Tuple, Optional

class check_sets_count(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        # not enough data, return empty set
        if len(args[1]) < args[0] :
           return set()
        return self.f(*args)

def load(filename: str) -> Set[int]:
    if not os.path.isfile(filename):
        return set()
    return set(int(line.strip()) for line in open(filename))

def fill_count_dict(argv: List[Set[int]]) -> Dict[int, int]:
    count_dict = dict()
    for arg in argv:
        for a in arg:
            count_dict[a] = count_dict.get(a, 0) + 1
    return count_dict