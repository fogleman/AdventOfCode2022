import fileinput
import re

# order: ore, clay, obsidian, geode

blueprints = [tuple(map(int, re.findall(r'\d+', line))) for line in fileinput.input()]
blueprints = [((x[1], 0, 0, 0), (x[2], 0, 0, 0), (x[3], x[4], 0, 0), (x[5], 0, x[6], 0)) for x in blueprints]

def can_build(materials, costs):
    return all(a >= b for a, b in zip(materials, costs))

def consume(materials, costs):
    return tuple(a - b for a, b in zip(materials, costs))

def build(robots, index):
    return tuple(x + (i == index) for i, x in enumerate(robots))

def collect(materials, robots):
    return tuple(a + b for a, b in zip(materials, robots))

def search(blueprint, minute, materials, robots, memo):
    if minute == 0:
        yield materials[-1]
        return
        
    key = (minute, materials, robots)
    if key in memo:
        yield memo[key]
        return

    result = 0
    for i, costs in enumerate(blueprint):
        if can_build(materials, costs):
            g = search(blueprint, minute - 1, collect(consume(materials, costs), robots), build(robots, i), memo)
            result = max(result, max(g, default=0))

    g = search(blueprint, minute - 1, collect(materials, robots), robots, memo)
    result = max(result, max(g, default=0))
    memo[key] = result
    yield result

for i, blueprint in enumerate(blueprints):
    for x in search(blueprint, 19, (0, 0, 0, 0), (1, 0, 0, 0), {}):
        print(x)
