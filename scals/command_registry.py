import os.path
from typing import Set, List
from command import Command


class CommandRegistry():
    def __init__(self):
        self.registry = dict()
        self.cmd_result = dict()
        subclasses = Command.__subclasses__()
        for s in subclasses:
            cmd = s()
            self.registry[cmd.get_name()] = cmd

    def execute(self, cmd: str, n: int, argv: List[str]) -> Set[int]:
        command = self.registry.get(cmd, None)
        if not command:
            raise Exception("ERROR unknown command {}".format(cmd))

        result = command.execute(n, (self.__load(arg) for arg in argv))
        res_id = str(id(result))
        self.cmd_result[res_id] = result

        return result

    def __load(self, filename: str) -> Set[int]:
        if filename in self.cmd_result:
            return self.cmd_result[filename]

        if not os.path.isfile(filename):
            print("ERROR file not found {}".format(filename))
            return set()

        return set(int(line.strip()) for line in open(filename))
