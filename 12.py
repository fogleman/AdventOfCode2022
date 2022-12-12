import fileinput
import heapq

grid = [list(line.strip()) for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

start = end = None
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'S':
            start = (x, y)
            grid[y][x] = 'a'
        if grid[y][x] == 'E':
            end = (x, y)
            grid[y][x] = 'z'

def shortest_path(grid, source, target):
    seen, queue = set(), [(0, source)]
    while queue:
        d, p = heapq.heappop(queue)
        if p == target:
            return d
        if p in seen:
            continue
        seen.add(p)
        x, y = p
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            q = nx, ny = (x + dx, y + dy)
            if q in seen:
                continue
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if ord(grid[ny][nx]) - ord(grid[y][x]) > 1:
                continue
            heapq.heappush(queue, (d + 1, q))

print(shortest_path(grid, start, end))

ds = []
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'a':
            d = shortest_path(grid, (x, y), end)
            if d is not None:
                ds.append(d)
print(min(ds))
