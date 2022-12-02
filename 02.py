import fileinput

lookup = dict(zip('ABCXYZ', 'RPSRPS'))
results = dict(RP=1, PR=-1, SR=1, RS=-1, PS=1, SP=-1)
item_scores = dict(R=1, P=2, S=3)
result_scores = {-1: 0, 0: 3, 1: 6}
result_needed = dict(R=-1, P=0, S=1)

rows = [tuple(lookup[x] for x in line.split()) for line in fileinput.input()]

total1 = total2 = 0
for a, b in rows:
    r = results.get(a + b, 0)
    total1 += item_scores[b] + result_scores[r]
    n = result_needed[b]
    for b in 'RPS':
        r = results.get(a + b, 0)
        if r == n:
            break
    total2 += item_scores[b] + result_scores[r]
print(total1)
print(total2)
