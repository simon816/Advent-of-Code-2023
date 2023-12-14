import sys

grid = []
for line in sys.stdin.readlines():
    line = list(line.strip())
    grid.append(line)
    width = len(line)

def cycle():
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
    for c in range(width):
        for r, row in enumerate(grid):
            if row[c] == '.':
                for find in range(c + 1, width):
                    if row[find] == 'O':
                        row[c] = 'O'
                        row[find] = '.'
                        break
                    if row[find] == '#':
                        break
    for r in range(len(grid) - 1, -1, -1):
        row = grid[r]
        for c, cell in enumerate(row):
            if cell == '.':
                for find in range(r - 1, -1, -1):
                    if grid[find][c] == 'O':
                        grid[r][c] = 'O'
                        grid[find][c] = '.'
                        break
                    if grid[find][c] == '#':
                        break
    for c in range(width - 1, -1, -1):
        for r, row in enumerate(grid):
            if row[c] == '.':
                for find in range(c - 1, -1, -1):
                    if row[find] == 'O':
                        row[c] = 'O'
                        row[find] = '.'
                        break
                    if row[find] == '#':
                        break

seen = set()
states = []
offset = 0
while True:
    cycle()
    state = tuple(tuple(r) for r in grid)
    if state in seen:
        offset = states.index(state)
        states = states[offset:]
        break
    seen.add(state)
    states.append(state)

rem = (1000000000 - 1 - offset) % len(states)
grid = states[rem]

load = 0
for r, row in enumerate(grid):
    load += row.count('O') * (len(grid) - r)
print(load)
