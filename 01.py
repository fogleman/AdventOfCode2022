import fileinput

counts = sorted([sum(map(int, x.split())) for x in
    ''.join(fileinput.input()).split('\n\n')], reverse=True)

print(counts[0])
print(sum(counts[:3]))
