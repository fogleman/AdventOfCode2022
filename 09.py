import fileinput

dirs = dict(U=(0, -1), D=(0, 1), L=(-1, 0), R=(1, 0))

def step(hx, hy, tx, ty):
    dx, dy = hx - tx, hy - ty
    if abs(dx) < 2 and abs(dy) < 2:
        return (tx, ty)
    dx //= abs(dx) or 1
    dy //= abs(dy) or 1
    return (tx + dx, ty + dy)

def run(commands, length):
    rope = [(0, 0)] * length
    positions = set(rope)
    for d, n in commands:
        for i in range(int(n)):
            rope[0] = (rope[0][0] + dirs[d][0], rope[0][1] + dirs[d][1])
            for j in range(1, len(rope)):
                rope[j] = step(*rope[j-1], *rope[j])
            positions.add(rope[-1])
    return len(positions)

commands = [line.split() for line in fileinput.input()]

print(run(commands, 2))
print(run(commands, 10))
