import sys


grid = []

row = 0
start = None
for line in sys.stdin.readlines():
    line = line.strip()
    idx = line.find('S')
    grid.append(list(line))
    if idx != -1:
        start = row, idx
    row += 1


start_r, start_c = start
con = []
maybe_shape = set('|-7FLJ')
if start_r > 0:
    if grid[start_r - 1][start_c] in '|7F':
        con.append((start_r - 1, start_c, 'N'))
        maybe_shape = maybe_shape & set('|JL')
if start_r < len(grid) - 1:
    if grid[start_r + 1][start_c] in '|LJ':
        con.append((start_r + 1, start_c, 'S'))
        maybe_shape = maybe_shape & set('|7F')
if start_c > 0:
    if grid[start_r][start_c - 1] in '-FL':
        con.append((start_r, start_c - 1, 'W'))
        maybe_shape = maybe_shape & set('-7J')
if start_c < len(grid[start_r]) - 1:
    if grid[start_r][start_c + 1] in '-7J':
        con.append((start_r, start_c + 1, 'E'))
        maybe_shape = maybe_shape & set('-LF')

assert len(con) == 2
assert len(maybe_shape) == 1
start_shape = next(iter(maybe_shape))

def step(cell_r, cell_c, dir):
    cell = grid[cell_r][cell_c]
    if cell == '|' and dir == 'N':
        return cell_r - 1, cell_c, 'N'
    if cell == '|' and dir == 'S':
        return cell_r + 1, cell_c, 'S'
    if cell == '-' and dir == 'W':
        return cell_r, cell_c - 1, 'W'
    if cell == '-' and dir == 'E':
        return cell_r, cell_c + 1, 'E'
    if cell == 'L' and dir == 'S':
        return cell_r, cell_c + 1, 'E'
    if cell == 'L' and dir == 'W':
        return cell_r - 1, cell_c, 'N'
    if cell == 'J' and dir == 'S':
        return cell_r, cell_c - 1, 'W'
    if cell == 'J' and dir == 'E':
        return cell_r - 1, cell_c, 'N'
    if cell == '7' and dir == 'N':
        return cell_r, cell_c - 1, 'W'
    if cell == '7' and dir == 'E':
        return cell_r + 1, cell_c, 'S'
    if cell == 'F' and dir == 'N':
        return cell_r, cell_c + 1, 'E'
    if cell == 'F' and dir == 'W':
        return cell_r + 1, cell_c, 'S'
    assert False, cell

loop = set((start, (con[0][0], con[0][1])))
cell = con[0]
while True:
    cell = step(*cell)
    r, c, _ = cell
    loop.add((r, c))
    if cell[0] == con[1][0] and cell[1] == con[1][1]:
        break

def flood(r, c):
    if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[r]) - 1:
        return -1, -1, set()
    adj = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    visited = set(((r, c),))
    space = set()
    if grid[r][c] == '.':
        space.add((r, c))
    while adj:
        r, c = adj.pop()
        if r == -1 or r == len(grid) or c == -1 or c == len(grid[r]):
            return -1, -1, visited
        visited.add((r, c))
        if grid[r][c] == '.' or grid[r][c] == '*':
            if grid[r][c] == '.':
                space.add((r, c))
            adj.extend(filter(lambda p: p not in visited,
                              ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))))
    return sorted(visited)[0], len(space), visited

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if (r, c) not in loop:
            grid[r][c] = '.'
        if (r, c) == start:
            grid[r][c] = start_shape

# TODO: Start cell
new_grid = []
for row in grid:
    new_row = []
    for cell in row:
        new_row.append(cell)
        new_row.append('-' if cell in '-FL' else '*')
    new_grid.append(new_row)
    new_grid.append(['|' if cell in '|F7' else '*' for cell in new_row])
grid = new_grid

"""
for row in grid:
    print(''.join(row))
"""

inside = {}
all_visited = set()
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if (r, c) in all_visited:
            continue
        if cell == '.' or cell == '*':
            flood_id, size, visited = flood(r, c)
            all_visited |= visited
            if flood_id != -1:
                if flood_id in inside:
                    assert inside[flood_id] == size
                inside[flood_id] = size

assert len(inside) == 1
print(next(iter(inside.values())))
