import fileinput
import heapq
import re

rooms = {}
for line in fileinput.input():
    valves = re.findall(r'[A-Z]{2}', line)
    room, neighbors = valves[0], valves[1:]
    rate = int(re.findall(r'\d+', line)[0])
    rooms[room] = (rate, tuple(neighbors))

def shortest_path(source, target):
    seen, queue = set(), [(0, source)]
    while queue:
        d, p = heapq.heappop(queue)
        if p == target:
            return d
        seen.add(p)
        for q in rooms[p][1]:
            if q not in seen:
                heapq.heappush(queue, (d + 1, q))

distances = {(a, b): shortest_path(a, b) for a in rooms for b in rooms}

def search(room, minute, pressure, remaining):
    yield pressure
    for other in remaining:
        m = minute + distances[(room, other)] + 1
        p = pressure + (30 - m) * rooms[other][0]
        if m < 30:
            yield from search(other, m, p, remaining - set([other]))

remaining = set(k for k, v in rooms.items() if v[0])
print(max(search('AA', 0, 0, remaining)))

best = 0
def search(positions, times, pressure, remaining, path):
    global best
    if pressure > best:
        best = pressure
        # print(best, remaining, positions, times)
        # print(' '.join(b for a, b in path if a == 0))
        # print(' '.join(b for a, b in path if a == 1))

    yield pressure

    rates = [rooms[other][0] for other in remaining]
    rates.sort(reverse=True)
    p = pressure
    m = min(times) + 2
    for rate in rates:
        p += (30 - m) * rate
    if p <= best:
        return

    v = [0, 1] if len(path) % 2 == 0 else [1, 0]
    # for i, (room, t) in enumerate(list(zip(positions, times))):
    for i in v:
        room, t = positions[i], times[i]
        if t >= 30:
            continue
        order = list(remaining)
        order.sort(key=lambda other: rooms[other][0] * (30 - (t + distances[(room, other)] + 1)), reverse=True)
        for other in order:
            m = t + distances[(room, other)] + 1
            if m > 30:
                continue
            p = pressure + (30 - m) * rooms[other][0]
            positions[i] = other
            times[i] = m
            remaining.remove(other)
            path.append((i, other))
            yield from search(positions, times, p, remaining, path)
            positions[i] = room
            times[i] = t
            remaining.add(other)
            path.pop()

print(max(search(['AA', 'AA'], [4, 4], 0, remaining, [])))
