import sys
import math
from functools import reduce

seq = sys.stdin.readline().strip()
assert sys.stdin.readline() == '\n'

graph = {}

for line in sys.stdin.readlines():
    src, dest = line.strip().split(' = ')
    left, right = dest[1:-1].split(', ')
    graph[src] = (left, right)

steps = 0
tracks = [[set(), node, 999999999] for node in graph.keys() if node.endswith('A')]

all_looped = False
seq_pos = 0
while not all_looped:
    side = seq[seq_pos]
    if side == 'L':
        idx = 0
    else:
        idx = 1
    all_looped = True
    for t in tracks:
        visited, curr, z_dist = t
        new = graph[curr][idx]
        if (new, seq_pos) in visited:
            continue
        all_looped = False
        visited.add((new, seq_pos))
        if new.endswith('Z'):
            t[2] = min(z_dist, len(visited))
        t[1] = new
    seq_pos += 1
    if seq_pos == len(seq):
        seq_pos = 0

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print(reduce(lcm, (t[2] for t in tracks), 1))

