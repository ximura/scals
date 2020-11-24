from scals_utils import check_sets_count, load, fill_count_dict
from typing import List, Set, Dict, Tuple, Optional

@check_sets_count
def eq(n: int, argv) -> Set[int]:
    return eq_impl(n, (load(arg) for arg in argv))

def eq_impl(n:int, argv: List[Set[int]]) -> Set[int]:
    count_dict = fill_count_dict(argv)
    return set((k for k, v in count_dict.items() if v == n))

def le(n: int, argv) -> Set[int]:
    return le_impl(n, (load(arg) for arg in argv))

def le_impl(n:int, argv: List[Set[int]]) -> Set[int]:
    count_dict = fill_count_dict(argv)
    return set((k for k, v in count_dict.items() if v < n))

@check_sets_count
def gr(n: int, argv) -> Set[int]:
    return gr_impl(n, (load(arg) for arg in argv))

def gr_impl(n:int, argv: List[Set[int]]) -> Set[int]:
    count_dict = fill_count_dict(argv)
    return set((k for k, v in count_dict.items() if v > n))

if __name__ == "__main__":
    test_set = ['test_sets/a.txt', 'test_sets/b.txt', 'test_sets/c.txt']
    print(eq(3, test_set))
    pass