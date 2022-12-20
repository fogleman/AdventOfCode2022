import fileinput

class Node:
    def __init__(self, value):
        self.value = value
    def move(self, offset):
        while offset:
            if offset > 0:
                a, b, c, d = self.prev, self, self.next, self.next.next
                offset -= 1
            else:
                a, b, c, d = self.prev.prev, self.prev, self, self.next
                offset += 1
            a.next = c
            c.prev, c.next = a, b
            b.prev, b.next = c, d
            d.prev = b

def run(values, multiplier, iterations):
    n = len(values)
    nodes = [Node(x * multiplier) for x in values]
    for i in range(n):
        nodes[i].prev = nodes[(i + n - 1) % n]
        nodes[i].next = nodes[(i + 1) % n]
    for i in range(iterations):
        for node in nodes:
            node.move(node.value % (n - 1))
    node = [x for x in nodes if x.value == 0][0]
    values = []
    for i in range(n):
        values.append(node.value)
        node = node.next
    return sum(values[x % n] for x in [1000, 2000, 3000])

values = list(map(int, fileinput.input()))
print(run(values, 1, 1))
print(run(values, 811589153, 10))
