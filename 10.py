import fileinput

X = 1
values = [X, X]
for line in fileinput.input():
    tokens = line.split()
    op, args = tokens[0], tokens[1:]
    if op == 'addx':
        values.append(X)
        X += int(args[0])
        values.append(X)
    else:
        values.append(X)

print(sum((i * 40 + 20) * x for i, x in enumerate(values[20::40])))

for y in range(6):
    for x in range(40):
        v = values[y * 40 + x + 1]
        print('#' if abs(v - x) <= 1 else '.', end='')
    print()
