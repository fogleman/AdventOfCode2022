import fileinput

monkeys = {}
for line in fileinput.input():
    tokens = line.split()
    monkeys[tokens[0][:-1]] = tuple(tokens[1:])

def value(name):
    tokens = monkeys[name]
    if len(tokens) == 1:
        return int(tokens[0])
    a, op, b = tokens
    a, b = value(a), value(b)
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b

print(value('root'))

def value(name):
    if name == 'humn':
        return 'X'
    tokens = monkeys[name]
    if len(tokens) == 1:
        return int(tokens[0])
    a, op, b = tokens
    a, b = value(a), value(b)
    if name == 'root':
        return (a, b)
    if isinstance(a, int) and isinstance(b, int):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a // b
    return (a, op, b)

def solve(lhs, rhs):
    if lhs == 'X':
        return rhs
    a, op, b = lhs
    if isinstance(a, int):
        if op == '+':
            return solve(b, rhs - a)
        if op == '-':
            return solve(b, a - rhs)
        if op == '*':
            return solve(b, rhs // a)
        if op == '/':
            return solve(b, rhs * a)
    else:
        if op == '+':
            return solve(a, rhs - b)
        if op == '-':
            return solve(a, rhs + b)
        if op == '*':
            return solve(a, rhs // b)
        if op == '/':
            return solve(a, rhs * b)

lhs, rhs = value('root')
print(solve(lhs, rhs))
