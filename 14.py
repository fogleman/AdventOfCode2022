import fileinput

def parse(it):
    cells = set()
    for line in it:
        points = [tuple(map(int, p.split(','))) for p in line.split()[::2]]
        for (x0, y0), (x1, y1) in zip(points, points[1:]):
            x0, y0, x1, y1 = min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)
            cells |= set((x0, y) for y in range(y0, y1 + 1))
            cells |= set((x, y0) for x in range(x0, x1 + 1))
    return cells

def drop(cells, threshold, floor):
    x, y = (500, 0)
    while y < threshold:
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in cells and ny != floor:
                x, y = nx, ny
                break
        else:
            return (x, y)

rock = parse(fileinput.input())
floor = max(y for x, y in rock) + 2

# part 1
cells = set(rock)
while True:
    p = drop(cells, floor, None)
    if p is None:
        break
    cells.add(p)
print(len(cells) - len(rock))

# part 2
cells = set(rock)
while True:
    p = drop(cells, floor, floor)
    cells.add(p)
    if p == (500, 0):
        break
print(len(cells) - len(rock))
