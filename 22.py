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

def cube_example(x, y, d):
    n = 4
    B = (2, 0)
    Y = (0, 1)
    O = (1, 1)
    W = (2, 1)
    G = (2, 2)
    R = (3, 2)

    def result(pq, ij, d):
        p, q = pq
        i, j = ij
        return p * n + i, q * n + j, d

    pq = x // n, y // n
    i, j = x % n, y % n
    ni, nj = n - i - 1, n - j - 1

    # ..B.
    # YOW.
    # ..GR

    if d == 0 and i == n - 1: # right
        if pq == B: # right to left
            return result(R, (n - 1, nj), 2)
        if pq == W: # right to down
            return result(R, (nj, 0), 1)
        if pq == R: # right to left
            return result(B, (n - 1, nj), 2)
    if d == 1 and j == n - 1: # down
        if pq == Y: # down to up
            return result(G, (ni, n - 1), 3)
        if pq == O: # down to right
            return result(G, (0, ni), 0)
        if pq == G: # down to up
            return result(Y, (ni, n - 1), 3)
        if pq == R: # down to right
            return result(Y, (0, ni), 0)
    if d == 2 and i == 0: # left
        if pq == B: # left to down
            return result(O, (j, 0), 1)
        if pq == Y: # left to up
            return result(R, (nj, n - 1), 3)
        if pq == G: # left to up
            return result(O, (nj, n - 1), 3)
    if d == 3 and j == 0: # up
        if pq == B: # up to down
            return result(Y, (ni, 0), 1)
        if pq == Y: # up to down
            return result(B, (ni, 0), 1)
        if pq == O: # up to right
            return result(B, (0, i), 0)
        if pq == R: # up to left
            return result(W, (n - 1, ni), 2)

    dx, dy = dirs[d]
    return (x + dx, y + dy, d)

def cube(x, y, d):
    n = 50
    B = (1, 0)
    R = (2, 0)
    W = (1, 1)
    O = (0, 2)
    G = (1, 2)
    Y = (0, 3)

    def result(pq, ij, d):
        p, q = pq
        i, j = ij
        return p * n + i, q * n + j, d

    pq = x // n, y // n
    i, j = x % n, y % n
    ni, nj = n - i - 1, n - j - 1

    # .BR
    # .W.
    # OG.
    # Y..

    if d == 0 and i == n - 1: # right
        if pq == R: # right to left
            return result(G, (n - 1, nj), 2)
        if pq == W: # right to up
            return result(R, (j, n - 1), 3)
        if pq == G: # right to left
            return result(R, (n - 1, nj), 2)
        if pq == Y: # right to up
            return result(G, (j, n - 1), 3)
    if d == 1 and j == n - 1: # down
        if pq == R: # down to left
            return result(W, (n - 1, i), 2)
        if pq == G: # down to left
            return result(Y, (n - 1, i), 2)
        if pq == Y: # down to down
            return result(R, (i, 0), 1)
    if d == 2 and i == 0: # left
        if pq == B: # left to right
            return result(O, (0, nj), 0)
        if pq == W: # left to down
            return result(O, (j, 0), 1)
        if pq == O: # left to right
            return result(B, (0, nj), 0)
        if pq == Y: # left to down
            return result(B, (j, 0), 1)
    if d == 3 and j == 0: # up
        if pq == B: # up to right
            return result(Y, (0, i), 0)
        if pq == R: # up to up
            return result(Y, (i, n - 1), 3)
        if pq == O: # up to right
            return result(W, (0, i), 0)

    dx, dy = dirs[d]
    return (x + dx, y + dy, d)

def show(x, y, d):
    c = '>v<^'[d]
    for j in range(h):
        for i in range(w):
            if (i, j) == (x, y):
                print(c, end='')
            else:
                print(grid[j][i], end='')
        print()
    print()

def run(x, y, d, path, one):
    for op in path:
        if op == 'R':
            d = (d + 1) % 4
            continue
        if op == 'L':
            d = (d + 3) % 4
            continue
        if one:
            dx, dy = dirs[d]
            nx, ny, n = x, y, int(op)
        n = int(op)
        while n > 0:
            if one:
                nx, ny, nd = (nx + dx + w) % w, (ny + dy + h) % h, d
            else:
                nx, ny, nd = cube(x, y, d)
            if grid[ny][nx] == '.':
                x, y, n, d = nx, ny, n - 1, nd
            elif grid[ny][nx] == '#':
                break
    return (y + 1) * 1000 + (x + 1) * 4 + d

print(run(x, y, d, path, True))
print(run(x, y, d, path, False))
