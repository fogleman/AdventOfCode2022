import fileinput

def update(i, x):
    if i == 0: return x * 13
    if i == 1: return x + 3
    if i == 2: return x * x
    if i == 3: return x + 5
    if i == 4: return x + 7
    if i == 5: return x + 4
    if i == 6: return x * 19
    if i == 7: return x + 2

def throw(i, x):
    if i == 0: return 1 if x % 5 == 0 else 6
    if i == 1: return 5 if x % 7 == 0 else 3
    if i == 2: return 0 if x % 13 == 0 else 6
    if i == 3: return 5 if x % 11 == 0 else 7
    if i == 4: return 2 if x % 3 == 0 else 0
    if i == 5: return 4 if x % 2 == 0 else 7
    if i == 6: return 1 if x % 17 == 0 else 3
    if i == 7: return 2 if x % 19 == 0 else 4

monkeys = [
    [52, 78, 79, 63, 51, 94],
    [77, 94, 70, 83, 53],
    [98, 50, 76],
    [92, 91, 61, 75, 99, 63, 84, 69],
    [51, 53, 83, 52],
    [76, 76],
    [75, 59, 93, 69, 76, 96, 65],
    [89],
]

counts = [0] * len(monkeys)
for r in range(10000):
    for m, items in enumerate(monkeys):
        while items:
            counts[m] += 1
            x = items.pop(0)
            y = update(m, x) % (5 * 7 * 13 * 11 * 3 * 2 * 17 * 19)#// 3
            t = throw(m, y)
            monkeys[t].append(y)

counts.sort()
print(counts[-1] * counts[-2])
