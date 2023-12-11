import sys
import itertools

grid = []
for line in sys.stdin.readlines():
    grid.append(list(line.strip()))

width = 0
grow_rows = []
for r, row in enumerate(grid):
    width = max(width, len(row))
    if row.count('.') == len(row):
        grow_rows.append(r)

grow_cols = []
for c in range(width):
    empty = True
    for row in grid:
        if row[c] != '.':
            empty = False
            break
    if empty:
        grow_cols.append(c)

galaxies = set()
expand = 1000000 - 1
for r, row in enumerate(grid):
    orig_r = r
    for grow in grow_rows:
        if grow > orig_r:
            break
        r += expand
    for c, cell in enumerate(row):
        orig_c = c
        for grow in grow_cols:
            if grow > orig_c:
                break
            c += expand
        if cell == '#':
            galaxies.add((r, c))

tot = 0
for (r1, c1), (r2, c2) in itertools.combinations(galaxies, 2):
    dist = abs(r1 - r2) + abs(c1 - c2)
    tot += dist

print(tot)
