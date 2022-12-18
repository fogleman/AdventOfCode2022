import fileinput

dirs = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (-1, 0, 0), (0, -1, 0), (0, 0, -1),
]

points = set([tuple(map(int, line.split(',')))
    for line in fileinput.input()])

def part1():
    return sum(len(dirs) - sum((x + dx, y + dy, z + dz) in points
        for dx, dy, dz in dirs) for x, y, z in points)

def part2():
    x0, y0, z0 = [min(p[i] - 1 for p in points) for i in range(3)]
    x1, y1, z1 = [max(p[i] + 1 for p in points) for i in range(3)]
    queue = [(x0, y0, z0)]
    seen = set(queue)
    while queue:
        x, y, z = queue.pop()
        for dx, dy, dz in dirs:
            nx, ny, nz = other = x + dx, y + dy, z + dz
            if nx < x0 or ny < y0 or nz < z0:
                continue
            if nx > x1 or ny > y1 or nz > z1:
                continue
            if other not in points and other not in seen:
                queue.append(other)
                seen.add(other)
    return sum(len(dirs) - sum((x + dx, y + dy, z + dz) not in seen
        for dx, dy, dz in dirs) for x, y, z in points)

print(part1())
print(part2())
