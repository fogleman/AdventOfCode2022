import fileinput
import math

def snafu_to_decimal(s):
    return sum(('=-012'.index(c) - 2) * (5 ** i)
        for i, c in enumerate(reversed(s)))

def decimal_to_snafu(value):
    seq = '012=-'
    result = []
    x = value
    while x:
        result.append(seq[x % 5])
        x //= 5
    result.append('0')
    while True:
        e = value - snafu_to_decimal(''.join(reversed(result)))
        if e == 0:
            break
        i = int(math.log(e, 5))
        result[i] = seq[(seq.index(result[i]) + 1) % len(seq)]
    return ''.join(reversed(result)).lstrip('0')

value = sum(snafu_to_decimal(line.strip())
    for line in fileinput.input())
print(decimal_to_snafu(value))
