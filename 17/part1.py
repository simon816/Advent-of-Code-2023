import sys
import queue

nodes = {}
max_r = None
max_c = None
for r, line in enumerate(sys.stdin.readlines()):
    for c, cell in enumerate(line.strip()):
        nodes[(r, c)] = int(cell)

        if max_r is None or r > max_r:
            max_r = r
        if max_c is None or c > max_c:
            max_c = c

start = (0, 0)

def get_adj(pos, dir, in_count):
    r, c = pos
    if (r - 1, c) in nodes and dir != 'S':
        count = in_count + 1 if dir == 'N' else 0
        if count < 3:
            yield (r - 1, c), 'N', count
    if (r, c - 1) in nodes and dir != 'E':
        count = in_count + 1 if dir == 'W' else 0
        if count < 3:
            yield (r, c - 1), 'W', count
    if (r + 1, c) in nodes and dir != 'N':
        count = in_count + 1 if dir == 'S' else 0
        if count < 3:
            yield (r + 1, c), 'S', count
    if (r, c + 1) in nodes and dir != 'W':
        count = in_count + 1 if dir == 'E' else 0
        if count < 3:
            yield (r, c + 1), 'E', count

q = queue.PriorityQueue()
start_node1 = (start, 'E', 0)
start_node2 = (start, 'S', 0)
q.put((0, start_node1))
q.put((0, start_node2))
lowest = {start_node1: 0, start_node2: 0}
final_nodes = set()
while not q.empty():
    cost, node = q.get()
    pos, dir, count = node
    if pos == (max_r, max_c):
        final_nodes.add(node)
    for adj in get_adj(pos, dir, count):
        pos, dir, count = adj
        new_cost = lowest[node] + nodes[pos]
        if adj not in lowest or new_cost < lowest[adj]:
            lowest[adj] = new_cost
            heuristic = (max_r - pos[0]) + (max_c - pos[1])
            q.put((new_cost + heuristic, adj))

dist = min(lowest[node] for node in final_nodes)
print(dist)
