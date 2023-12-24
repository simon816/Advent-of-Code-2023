import sys

grid = []
start = None
for r, line in enumerate(sys.stdin.readlines()):
    grid.append(line.strip())
    if 'S' in line:
        start = (r, line.index('S'))

reach = set((start,))
for _ in range(64):
    new_reach = set()
    for r, c in reach:
        if r > 0 and grid[r - 1][c] != '#':
            new_reach.add((r - 1, c))
        if r < len(grid) - 1 and grid[r + 1][c] != '#':
            new_reach.add((r + 1, c))
        if c > 0 and grid[r][c - 1] != '#':
            new_reach.add((r, c - 1))
        if c < len(grid[r]) - 1 and grid[r][c + 1] != '#':
            new_reach.add((r, c + 1))
    reach = new_reach

print(len(reach))
