import fileinput
import re

count1 = count2 = 0
for line in fileinput.input():
    a, b, c, d = map(int, re.findall(r'\d+', line))
    A = set(range(a, b + 1))
    B = set(range(c, d + 1))
    count1 += A <= B or B <= A
    count2 += bool(A & B)

print(count1)
print(count2)
