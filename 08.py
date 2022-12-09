import fileinput

grid = [line.rstrip() for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

def scan(x, y):
    score, visible = 1, False
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny, d = x, y, 0
        while True:
            nx, ny = nx + dx, ny + dy
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                visible = True
                break
            d += 1
            if grid[ny][nx] >= grid[y][x]:
                break
        score *= d
    return visible, score

print(sum(scan(x, y)[0] for y in range(h) for x in range(w)))
print(max(scan(x, y)[1] for y in range(h) for x in range(w)))
