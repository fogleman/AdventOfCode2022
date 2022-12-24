import fileinput
import heapq

dirs = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}
grid = [line.strip()[1:-1] for line in fileinput.input()][1:-1]
w, h = len(grid[0]), len(grid)
S, E = (0, -1), (w - 1, h)

blizzards = [(x, y, d[0], d[1]) for y in range(h) for x in range(w)
    if (d := dirs.get(grid[y][x]))]

memo = {}
def blizzards_at_time(t):
    if t not in memo:
        memo[t] = {((bx + dx * t) % w, (by + dy * t) % h)
            for bx, by, dx, dy in blizzards}
    return memo[t]

def shortest_path(source, target, t):
    seen, queue = set(), [(t, source)]
    while queue:
        d, p = heapq.heappop(queue)
        if p == target:
            return d
        if (d, p) in seen:
            continue
        seen.add((d, p))
        x, y = p
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]:
            q = nx, ny = (x + dx, y + dy)
            if (d + 1, q) in seen:
                continue
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                if (nx, ny) not in (source, target):
                    continue
            if (nx, ny) in blizzards_at_time(d + 1):
                continue
            heapq.heappush(queue, (d + 1, q))

t = shortest_path(S, E, 0)
print(t)

t = shortest_path(E, S, t)
t = shortest_path(S, E, t)
print(t)
