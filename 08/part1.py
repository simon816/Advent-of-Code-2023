import sys
import itertools

seq = itertools.cycle(sys.stdin.readline().strip())
assert sys.stdin.readline() == '\n'

graph = {}

for line in sys.stdin.readlines():
    src, dest = line.strip().split(' = ')
    left, right = dest[1:-1].split(', ')
    graph[src] = (left, right)

steps = 0
node = 'AAA'
while node != 'ZZZ':
    side = next(seq)
    if side == 'L':
        idx = 0
    else:
        idx = 1
    node = graph[node][idx]
    steps += 1

print(steps)
