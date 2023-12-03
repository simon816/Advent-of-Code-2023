import sys

grid = []

for line in sys.stdin.readlines():
    line = line.strip()
    grid.append(list(line))

s = 0
for r, row in enumerate(grid):
    num = ''
    valid = False
    for c, cell in enumerate(row):
        if cell.isdigit():
            num += cell
            check = []
            if r > 0:
                check.append(grid[r - 1][c])
                if c > 0:
                    check.append(grid[r - 1][c - 1])
                if c < len(row) - 1:
                    check.append(grid[r - 1][c + 1])
            if r < len(grid) - 1:
                check.append(grid[r + 1][c])
                if c > 0:
                    check.append(grid[r + 1][c - 1])
                if c < len(row) - 1:
                    check.append(grid[r + 1][c + 1])
            if c > 0:
                check.append(grid[r][c - 1])
            if c < len(row) - 1:
                check.append(grid[r][c + 1])
            for ch in check:
                if ch != '.' and not ch.isdigit():
                    valid = True
                    break
        else:
            if valid:
                print((r, c), num)
                s += int(num)
            valid = False
            num = ''
    if valid:
        print((r,), num)
        s += int(num)

print(s)
