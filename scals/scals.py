import os.path
import sys
import re
from typing import List, Set, Dict


def check_sets_count(method):
    def inner(ref, *args):
        if len(args[1]) < args[0]:
            return set()

        return method(ref, *args)
    return inner


class Scals():
    def __init__(self):
        self.pattern = re.compile(r'\s*([a-zA-Z]+)\s*(\d)(.*)')
        self.cmd_result = dict()

    def parse_cmd(self, cmd: str):
        cmd_start = 1
        cmd_end = 0
        while True:
            cmd_end = cmd.find(']')
            cmd_start = cmd.rfind('[', 0, cmd_end)

            if cmd_start == -1 or cmd_end == -1:
                break

            try:
                result = self.__execute_cmd(cmd[cmd_start+1:cmd_end])
            except Exception as exception:
                result = None
                print(exception)

            res_id = str(id(result)) if result else ""
            if result:
                self.cmd_result[res_id] = result

            cmd = cmd.replace(cmd[cmd_start:cmd_end+1], res_id)

        return result

    @check_sets_count
    def eq(self, n: int, argv) -> Set[int]:
        return Scals.eq_impl(n, (self.__load(arg) for arg in argv))

    @staticmethod
    def eq_impl(n: int, argv: List[Set[int]]) -> Set[int]:
        count_dict = Scals.__fill_count_dict(argv)
        return set((k for k, v in count_dict.items() if v == n))

    def le(self, n: int, argv) -> Set[int]:
        return Scals.le_impl(n, [self.__load(arg) for arg in argv])

    @staticmethod
    def le_impl(n: int, argv: List[Set[int]]) -> Set[int]:
        count_dict = Scals.__fill_count_dict(argv)
        return set((k for k, v in count_dict.items() if v < n))

    @check_sets_count
    def gr(self, n: int, argv) -> Set[int]:
        return Scals.gr_impl(n, (self.__load(arg) for arg in argv))

    @staticmethod
    def gr_impl(n: int, argv: List[Set[int]]) -> Set[int]:
        count_dict = Scals.__fill_count_dict(argv)
        return set((k for k, v in count_dict.items() if v > n))

    def __execute_cmd(self, cmd: str):
        m = self.pattern.match(cmd)
        if not m:
            raise Exception(f"ERROR cant parse command {cmd}")

        command = m.group(1).lower()

        if not hasattr(self, command):
            raise Exception(f"ERROR unknown command {command}")

        n = int(m.group(2))
        sets = [name for name in m.group(3).split(" ") if len(name) > 0]
        result = self.__getattribute__(command)(n, sets)
        return result

    def __load(self, filename: str) -> Set[int]:
        if filename in self.cmd_result:
            return self.cmd_result[filename]

        if not os.path.isfile(filename):
            print(f"ERROR file not found {filename}")
            return set()

        return set(int(line.strip()) for line in open(filename))

    @staticmethod
    def __fill_count_dict(argv: List[Set[int]]) -> Dict[int, int]:
        count_dict = dict()
        for arg in argv:
            for a in arg:
                count_dict[a] = count_dict.get(a, 0) + 1
        return count_dict


if __name__ == "__main__":
    argv = ' '.join(sys.argv[1:])
    print(f"Command line {argv}")
    scals = Scals()
    print(scals.parse_cmd(argv))
