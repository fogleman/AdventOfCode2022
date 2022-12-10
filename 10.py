import fileinput

X = 1
values = [X]
for line in fileinput.input():
    tokens = line.split()
    values.append(X)
    if tokens[0] == 'addx':
        values.append(X)
        X += int(tokens[1])

print(sum((i * 40 + 20) * x for i, x in enumerate(values[20::40])))

for y in range(6):
    for x in range(40):
        v = values[y * 40 + x + 1]
        print('#' if abs(v - x) < 2 else '.', end='')
    print()
