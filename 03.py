from string import ascii_letters
import fileinput

lines = [line.rstrip() for line in fileinput.input()]

total = 0
for line in lines:
    i = len(line) // 2
    a, b = line[:i], line[i:]
    c = list(set(a) & set(b))[0]
    p = ascii_letters.index(c) + 1
    total += p
print(total)

groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
total = 0
for a, b, c in groups:
    c = list(set(a) & set(b) & set(c))[0]
    p = ascii_letters.index(c) + 1
    total += p
print(total)
