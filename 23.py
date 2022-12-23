from collections import Counter
from itertools import count
import fileinput

grid = [line.strip() for line in fileinput.input()]
cells = set((x, y) for y in range(len(grid[0])) for x in range(len(grid))
    if grid[y][x] == '#')

N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
NE, SE, NW, SW = (1, -1), (1, 1), (-1, -1), (-1, 1)
DIRS = [N, S, E, W, NE, SE, NW, SW]

options = [
    ((N, NE, NW), N),
    ((S, SE, SW), S),
    ((W, NW, SW), W),
    ((E, NE, SE), E),
]

def step(cells, iteration):
    todo = {}
    for cell in cells:
        x, y = cell
        todo[cell] = cell
        if any((x + dx, y + dy) in cells for dx, dy in DIRS):
            for i in range(4):
                neighbors, direction = options[(i + iteration) % 4]
                if all((x + dx, y + dy) not in cells for dx, dy in neighbors):
                    dx, dy = direction
                    todo[cell] = (x + dx, y + dy)
                    break
    c = Counter(todo.values())
    return {v if c[v] == 1 else k for k, v in todo.items()}

def part1(cells):
    for i in range(10):
        cells = step(cells, i)
    x0, x1 = min(x for x, y in cells), max(x for x, y in cells)
    y0, y1 = min(y for x, y in cells), max(y for x, y in cells)
    return (x1 - x0 + 1) * (y1 - y0 + 1) - len(cells)

def part2(cells):
    for i in count():
        new_cells = step(cells, i)
        if new_cells == cells:
            return i + 1
        cells = new_cells

print(part1(cells))
print(part2(cells))
