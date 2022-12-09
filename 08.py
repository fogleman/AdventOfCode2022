import fileinput
import re

grid = []
for line in fileinput.input():
    grid.append(list(map(int, line.rstrip())))

h = len(grid)
w = len(grid[0])

def visible(x, y):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dirs:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx, ny + dy
            if nx < 0 or ny < 0 or nx > w - 1 or ny > h - 1:
                return True
            if grid[ny][nx] >= grid[y][x]:
                break
    return False

def visible(x, y):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    scores = []
    for dx, dy in dirs:
        nx, ny = x, y
        result = 0
        while True:
            nx, ny = nx + dx, ny + dy
            if nx < 0 or ny < 0 or nx > w - 1 or ny > h - 1:
                break
            result += 1
            if grid[ny][nx] >= grid[y][x]:
                break
        scores.append(result)
    return scores[0]*scores[1]*scores[2]*scores[3]

counts = []
for y in range(h):
    for x in range(w):
        counts.append(visible(x, y))
print(max(counts))
