import sys
import pprint

seeds = list(map(int, sys.stdin.readline().split(': ')[1].split(' ')))

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

def search(m, key):
    for k, (dst, l) in m.items():
        if key >= k and k + l > key:
            return dst + (key - k)
    return key

curlist = seeds
for map_name in chain:
    nextlist = []
    for val in curlist:
        nextlist.append(search(maps[map_name], val))
    curlist = nextlist

print(min(curlist))
