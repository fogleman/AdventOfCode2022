import fileinput
import re

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

lines = [line.rstrip('\n') for line in fileinput.input()]
grid, path = lines[:-2], lines[-1]
w, h = max(len(row) for row in grid), len(grid)
grid = [row + ' ' * (w - len(row)) for row in grid]
x, y, d = grid[0].index('.'), 0, 0

path = path.replace('R', ' R ')
path = path.replace('L', ' L ')
path = path.split()

def run(x, y, d, path):
    for op in path:
        if op == 'R':
            d = (d + 1) % 4
            continue
        if op == 'L':
            d = (d + 3) % 4
            continue
        dx, dy = dirs[d]
        nx, ny, n = x, y, int(op)
        while n > 0:
            nx, ny = (nx + dx + w) % w, (ny + dy + h) % h
            if grid[ny][nx] == '.':
                x, y, n = nx, ny, n - 1
            elif grid[ny][nx] == '#':
                break
    return (y + 1) * 1000 + (x + 1) * 4 + d

print(run(x, y, d, path))
