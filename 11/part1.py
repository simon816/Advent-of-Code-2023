import sys
import itertools

grid = []
for line in sys.stdin.readlines():
    grid.append(list(line.strip()))

width = 0
new_grid = []
for row in grid:
    width = max(width, len(row))
    new_grid.append(row)
    if row.count('.') == len(row):
        new_grid.append(list(row))

grid = new_grid

c = 0
while c < width:
    empty = True
    for row in grid:
        if row[c] != '.':
            empty = False
            break
    if empty:
        for row in grid:
            row.insert(c, '.')
        c += 1
        width += 1
    c += 1

galaxies = set()
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == '#':
            galaxies.add((r, c))

tot = 0
for (r1, c1), (r2, c2) in itertools.combinations(galaxies, 2):
    dist = abs(r1 - r2) + abs(c1 - c2)
    tot += dist

print(tot)
