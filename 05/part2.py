import sys
import pprint

seeds = list(map(int, sys.stdin.readline().split(': ')[1].split(' ')))
ranges = []
for start, r in zip(seeds[:-1:2], seeds[1::2]):
    ranges.append((start, start + r))

maps = {}
cur_map = {}

chain = []

for line in sys.stdin.readlines():
    line = line.strip()
    if line.endswith('map:'):
        t = line.split(' ')[0]
        #src, dst = line.split(' ')[0].split('-to-')
        cur_map = {}
        maps[t] = cur_map
        chain.append(t)
        continue
    if not line:
        continue
    dst_start, src_start, r_len = tuple(map(int, line.split(' ')))
    cur_map[src_start] = (dst_start, r_len)

def search(m, r):
    start, stop = r
    newranges = []
    for k, (dst, l) in m.items():
        if start >= k and k + l > start:
            new_l = min(stop - start, l)
            newranges.append((dst, dst + new_l))
    return newranges

def search_brute(m, key):
    for k, (dst, l) in m.items():
        if key >= k and k + l > key:
            return dst + (key - k)
    return key

# TODO: none brute approach
m = None
for (start, stop) in ranges:
    for val in range(start, stop):
        for map_name in chain:
            val = search_brute(maps[map_name], val)
        if m is None or val < m:
            m = val

print(m)
#print(ranges)
#print(search(maps['seed-to-soil'], ranges[0]))
