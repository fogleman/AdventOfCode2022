import fileinput
import numpy as np
import re

def parse(data):
    header, commands = data.split('\n\n')
    header = header.split('\n')[:-1]
    commands = commands.split('\n')[:-1]
    commands = [tuple(map(int, re.findall(r'\d+', command)))
        for command in commands]
    stacks = [['']]
    rows = np.array([list(line[1::4]) for line in header]).T
    for row in rows:
        stacks.append(list(''.join(reversed(row)).strip()))
    return stacks, commands

def part1(stacks, commands):
    stacks = [x[:] for x in stacks]
    for count, src, dst in commands:
        for i in range(count):
            stacks[dst].append(stacks[src].pop())
    return ''.join(x[-1] for x in stacks)

def part2(stacks, commands):
    stacks = [x[:] for x in stacks]
    for count, src, dst in commands:
        values = [stacks[src].pop() for i in range(count)]
        stacks[dst].extend(reversed(values))
    return ''.join(x[-1] for x in stacks)

stacks, commands = parse(''.join(fileinput.input()))
print(part1(stacks, commands))
print(part2(stacks, commands))
