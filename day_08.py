import copy
input_file = __file__.split('\\')[-1].replace('.py', '') + "_input.txt"


def process_input_line(line):
    line = line.strip()
    operation = line[0:3]
    arg = int(line[4:])
    return operation, arg


input_lines = list()
with open(input_file) as f:
    while True:
        raw_line = f.readline()
        if raw_line:
            operation, arg = process_input_line(raw_line)
            input_lines.append([operation, arg])
        else:
            break
max_lines = len(input_lines)


class ConsoleGame():
    def __init__(self):
        self.OPERATIONS = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop}
        self.accumulator = 0
        self.instruction_n = 0
        self.executed_ins = list()

    def acc(self, arg):
        self.accumulator += arg
        self.instruction_n += 1

    def jmp(self, arg):
        self.instruction_n += arg

    def nop(self, arg):
        self.instruction_n += 1

    def run(self, program):
        self.accumulator = 0
        self.instruction_n = 0
        self.executed_ins = list()
        while True:
            if self.instruction_n in self.executed_ins:
                # print("Part 1 = ", self.accumulator)
                return False

            elif self.instruction_n == len(program):
                print("Part 2 = ", self.accumulator)
                return True
            else:
                self.executed_ins.append(self.instruction_n)
                ins = program[self.instruction_n]
                op = ins[0]
                arg = ins[1]
                self.OPERATIONS[op](arg)


if __name__ == "__main__":
    console = ConsoleGame()
    done = False
    while True:
        len_prog = len(input_lines)
        i = 0
        while i < len_prog:
            program = copy.deepcopy(input_lines)
            if program[i][0] == 'nop':
                program[i][0] = 'jmp'
                if console.run(program):
                    done = True
                    break
            i += 1
            if done:
                break
        i = 0
        while i < len_prog:
            program = copy.deepcopy(input_lines)
            if program[i][0] == 'jmp':
                program[i][0] = 'nop'
                if console.run(program):
                    done = True
                    break
            i += 1
            if done:
                break
        break
