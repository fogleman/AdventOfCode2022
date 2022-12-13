import ast
import fileinput
import functools

pairs = [tuple(map(ast.literal_eval, p.split('\n')[:2]))
    for p in ''.join(fileinput.input()).split('\n\n')]

def compare(a, b):
    la, lb = isinstance(a, list), isinstance(b, list)
    if la and lb:
        for x, y in zip(a, b):
            if x != y:
                return compare(x, y)
        return compare(len(a), len(b))
    elif la:
        return compare(a, [b])
    elif lb:
        return compare([a], b)
    return (a > b) - (a < b)

def part1():
    return sum(i + 1 for i, (a, b) in enumerate(pairs)
        if compare(a, b) < 0)

def part2():
    packets = [[[2]], [[6]]]
    for (a, b) in pairs:
        packets.extend([a, b])
    packets.sort(key=functools.cmp_to_key(compare))
    a = packets.index([[2]]) + 1
    b = packets.index([[6]]) + 1
    return a * b

print(part1())
print(part2())
