from typing import List, Set, Dict, Tuple, Optional

def load(filename: str) -> Set[int]: 
    return set(int(line.strip()) for line in open(filename))

def eq(n: int, argv) -> Set[int]:
    # not enough data, return empty set
    if len(argv) < n :
        return set()

    return eq_impl(n, [load(arg) for arg in argv])

def eq_impl(n:int, argv: List[Set[int]]) -> Set[int]:
    count_dict = dict()
    for arg in argv:
        for a in arg:
            count_dict[a] = count_dict.get(a, 0) + 1

    return set(filter(lambda a: a[1] == n, count_dict))


if __name__ == "__main__":
    test_set = ['test_sets/a.txt', 'test_sets/b.txt', 'test_sets/c.txt']
    print(eq(3, test_set))
    pass