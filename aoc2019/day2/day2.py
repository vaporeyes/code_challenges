import operator
import sys

OPCODES = {1: operator.add, 2: operator.mul}


def chunk_file(input_file):
    with open(input_file) as f:
        data = [x.split() for x in f.readlines()]
        orig_lst = [int(x) for x in data[0][0].split(",")]
        c = [x for x in chunks(orig_lst, 4)]
        return c, orig_lst


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def process_opcode_set(lst, orig_lst):
    opcode = lst[0]
    if opcode == 99:
        sys.exit(0)
    op = OPCODES[opcode]
    a = lst[1]
    b = lst[2]
    loc = lst[3]
    x = orig_lst[a]
    y = orig_lst[b]
    output = op(x, y)
    orig_lst[loc] = output


if __name__ == "__main__":
    c, orig_lst = chunk_file("day2_input.txt")
    for i in c:
        process_opcode_set(c, orig_lst)
