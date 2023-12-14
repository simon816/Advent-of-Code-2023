import sys

grid = []
for line in sys.stdin.readlines():
    line = list(line.strip())
    grid.append(line)

load = 0
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == '.':
            for find in range(r + 1, len(grid)):
                if grid[find][c] == 'O':
                    grid[r][c] = 'O'
                    grid[find][c] = '.'
                    break
                if grid[find][c] == '#':
                    break
    load += row.count('O') * (len(grid) - r)

print(load)
