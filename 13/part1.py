import sys

grids = []
grid = []
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        grids.append(grid)
        grid = []
        continue
    grid.append(line)
grids.append(grid)

tot = 0
for grid in grids:

    val = 0
    width = 0
    for r, row in enumerate(grid):
        width = max(width, len(row))
        if r > 0 and row == grid[r - 1]:
            no_match = False
            check_above = r - 2
            for check_below in range(r + 1, len(grid)):
                if check_above >= 0 and grid[check_above] != grid[check_below]:
                    no_match = True
                    break
                check_above -= 1
            if not no_match:
                val = r * 100
                break
    if val == 0:
        prev_col = None
        for c in range(width):
            col = [r[c] for r in grid]
            if col == prev_col:
                no_match = False
                check_right = c + 1
                for check_left in range(c - 2, -1, -1):
                    if check_right < width and \
                       [r[check_left] for r in grid] != \
                       [r[check_right] for r in grid]:
                        no_match = True
                        break
                    check_right += 1
                if not no_match:
                    val = c
                    break
            prev_col = col
    tot += val
print(tot)
