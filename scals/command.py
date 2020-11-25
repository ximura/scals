from typing import List, Set, Dict


class Command():

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def execute(self, n: int, argv: List[Set[int]]) -> Set[int]:
        count_dict = Command.__fill_count_dict(argv)
        return set((k for k, v in count_dict.items() if self.check(n, v)))

    def check(self, n: int, count: int) -> bool:
        return False

    @staticmethod
    def __fill_count_dict(argv: List[Set[int]]) -> Dict[int, int]:
        count_dict = dict()
        for arg in argv:
            for a in arg:
                count_dict[a] = count_dict.get(a, 0) + 1
        return count_dict


class EqCommand(Command):

    def __init__(self):
        Command.__init__(self, "eq")

    def check(self, n: int, count: int) -> bool:
        return count == n


class LeCommand(Command):

    def __init__(self):
        Command.__init__(self, "le")

    def check(self, n: int, count: int) -> bool:
        return count < n


class GrCommand(Command):

    def __init__(self):
        Command.__init__(self, "gr")

    def check(self, n: int, count: int) -> bool:
        return count > n
