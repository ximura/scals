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
    return set(int(line.strip()) for line in open(filename))

def fill_count_dict(argv: List[Set[int]]) -> Dict[int, int]:
    count_dict = dict()
    for arg in argv:
        for a in arg:
            count_dict[a] = count_dict.get(a, 0) + 1
    return count_dict

@check_sets_count
def eq(n: int, argv) -> Set[int]:
    return eq_impl(n, (load(arg) for arg in argv))

def eq_impl(n:int, argv: List[Set[int]]) -> Set[int]:
    count_dict = fill_count_dict(argv)
    return set((k for k, v in count_dict.items() if v == n))

if __name__ == "__main__":
    test_set = ['test_sets/a.txt', 'test_sets/b.txt', 'test_sets/c.txt']
    print(eq(3, test_set))
    pass