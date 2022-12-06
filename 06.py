import fileinput

data = ''.join(fileinput.input()).strip()

for n in [4, 14]:
    for i in range(len(data)):
        if len(set(data[i:i+n])) == n:
            print(i+n)
            break
