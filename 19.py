import fileinput
import re

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

best = 0
def search(blueprint, minute, materials, robots, skipped, memo):
    global best

    if minute == 0:
        best = max(best, materials[-1])
        yield materials[-1]
        return

    key = (minute, materials, robots)
    if key in memo:
        yield memo[key]
        return

    b = materials[-1] + robots[-1] * minute + (minute * (minute - 1)) // 2
    if b <= best:
        return

    result = 0
    for i, costs in enumerate(blueprint):
        if can_build(materials, costs) and not skipped[i]:
            g = search(blueprint, minute - 1, collect(consume(materials, costs), robots), build(robots, i), (0, 0, 0, 0), memo)
            result = max(result, max(g, default=0))

    skipped = tuple(can_build(materials, costs) for costs in blueprint)
    g = search(blueprint, minute - 1, collect(materials, robots), robots, skipped, memo)
    result = max(result, max(g, default=0))

    memo[key] = result
    yield result

materials = (0, 0, 0, 0)
robots = (1, 0, 0, 0)
skipped = (0, 0, 0, 0)

result = 0
for i, blueprint in enumerate(blueprints):
    best = 0
    value = next(search(blueprint, 24, materials, robots, skipped, {}))
    result += value * (i + 1)
print(result)

result = 1
for i, blueprint in enumerate(blueprints[:3]):
    best = 0
    value = next(search(blueprint, 32, materials, robots, skipped, {}))
    result *= value
print(result)
