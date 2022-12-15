import fileinput
import re

sensors = [tuple(map(int, re.findall(r'[-\d]+', line)))
    for line in fileinput.input()]

def row(y):
    spans = list(sorted((sx - d, sx + d + 1) for sx, sy, bx, by in sensors
        if (d := abs(bx - sx) + abs(by - sy) - abs(sy - y)) > 0))
    start, end = spans[0]
    for x0, x1 in spans:
        if x0 > end:
            yield (start, end)
            start = x0
        end = max(end, x1)
    yield (start, end)

def part1(y):
    return (sum(s[1] - s[0] for s in row(y)) -
        len(set(s[2] for s in sensors if s[3] == y)))

def part2(n):
    return next(x1 * n + y for y in range(n) for x0, x1 in row(y)
        if x1 >= 0 and x1 <= n)

print(part1(2000000))
print(part2(4000000))
