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

old_solutions = {}

for g, grid in enumerate(grids):

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
    old_solutions[g] = val


def grid_range(grid):
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            yield r, c

tot = 0
for g, orig_grid in enumerate(grids):
    new_sol = None
    sns = 0
    for s_r, s_c in grid_range(orig_grid):
        #print("Try", s_r, s_c)
        grid = list(orig_grid)
        row = list(grid[s_r])
        row[s_c] = '.' if row[s_c] == '#' else '#'
        grid[s_r] = ''.join(row)
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
                    # If we found the old solution, keep looking
                    if val != old_solutions[g]:
                        break
        if val == 0 or val == old_solutions[g]:
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
                        if val != old_solutions[g]:
                            break
                prev_col = col
        if val > 0 and val != old_solutions[g] and val != new_sol:
            sns += 1
            assert sns == 1
            tot += val
            new_sol = val
    assert new_sol is not None, (g, new_sol, old_solutions[g])
print(tot)
