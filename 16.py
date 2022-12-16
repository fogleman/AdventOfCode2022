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
