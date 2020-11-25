import sys
import re
from command_registry import CommandRegistry


class Scals():
    def __init__(self):
        self.pattern = re.compile(r'\s*([a-zA-Z]+)\s*(\d)(.*)')
        self.registry = CommandRegistry()

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
            cmd = cmd.replace(cmd[cmd_start:cmd_end+1], res_id)

        return result

    def __execute_cmd(self, cmd: str):
        m = self.pattern.match(cmd)
        if not m:
            raise Exception("ERROR cant parse command {}".format(cmd))

        command = m.group(1).lower()
        n = int(m.group(2))
        sets = [name for name in m.group(3).split(" ") if len(name) > 0]
        return self.registry.execute(command, n, sets)


if __name__ == "__main__":
    argv = ' '.join(sys.argv[1:])
    scals = Scals()
    print(scals.parse_cmd(argv))
