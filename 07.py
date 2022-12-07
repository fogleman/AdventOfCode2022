import fileinput

def parse(it):
    files = []
    cwd = ['']
    for line in it:
        tokens = line.rstrip().split()
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '/':
                    cwd = cwd[:1]
                elif tokens[2] == '..':
                    cwd.pop()
                else:
                    cwd.append(tokens[2])
        elif tokens[0] != 'dir':
            path = '%s/%s' % ('/'.join(cwd), tokens[1])
            files.append((path, int(tokens[0])))
    sizes = {}
    for path, size in files:
        names = path.split('/')[:-1]
        for i in range(len(names)):
            name = '/'.join(names[:i+1])
            sizes[name] = sizes.get(name, 0) + size
    return sizes

sizes = parse(fileinput.input())

# part 1
print(sum(x for x in sizes.values() if x <= 100000))

# part 2
need = 30000000 - (70000000 - sizes[''])
print(min(x for x in sizes.values() if x >= need))
