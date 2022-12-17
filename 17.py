import fileinput

jets = ''.join(fileinput.input()).strip()
# jets = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

pieces = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)},
    {(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)},
    {(0, 3), (0, 2), (0, 1), (0, 0)},
    {(0, 1), (1, 1), (0, 0), (1, 0)},
]

def translate(piece, dx, dy):
    return {(x + dx, y + dy) for x, y in piece}

def oob(piece):
    return any(x < 0 or x >= 7 or y < 0 for x, y in piece)

def collides(piece, grid):
    return len(piece & grid) > 0

def prune(grid):
    maxy = max(y for x, y in grid)
    return {(x, y) for x, y in grid if maxy - y < 100}

def part1(jets, pieces):
    grid = set()
    maxy = 0
    j = 0
    counts = {}
    previous = {}
    previous_index = {}
    for i in range(100000):
        piece = pieces[i % len(pieces)]
        piece = translate(piece, 2, maxy + 3)
        while True:
            jet = jets[j % len(jets)]
            j += 1
            dx = -1 if jet == '<' else 1
            piece = translate(piece, dx, 0)
            if oob(piece) or collides(piece, grid):
                piece = translate(piece, -dx, 0)
            piece = translate(piece, 0, -1)
            if oob(piece) or collides(piece, grid):
                piece = translate(piece, 0, 1)
                grid |= piece
                maxy = max(maxy, max(y for x, y in piece) + 1)
                break
        grid = prune(grid)
        key = (i % len(pieces), j % len(jets))
        counts[key] = counts.get(key, 0) + 1
        dy = maxy - previous.get(key, 0)
        di = max(1, i - previous_index.get(key, 0))
        e = maxy + ((1000000000000 - i) / di) * dy
        if int(e) == e:
            print(i, maxy, dy, di, int(e)-1)
        previous[key] = maxy
        previous_index[key] = i
    return maxy

print(part1(jets, pieces))
