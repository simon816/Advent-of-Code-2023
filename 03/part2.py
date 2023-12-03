import sys
from collections import defaultdict

grid = []

for line in sys.stdin.readlines():
    line = line.strip()
    grid.append(list(line))

gears = defaultdict(list)
valid_nums = set()
for r, row in enumerate(grid):
    num = []
    valid = False
    for c, cell in enumerate(row):
        if cell.isdigit():
            num.append(cell)
            check = []
            if r > 0:
                check.append((r - 1,c))
                if c > 0:
                    check.append((r - 1,c - 1))
                if c < len(row) - 1:
                    check.append((r - 1,c + 1))
            if r < len(grid) - 1:
                check.append((r + 1,c))
                if c > 0:
                    check.append((r + 1,c - 1))
                if c < len(row) - 1:
                    check.append((r + 1,c + 1))
            if c > 0:
                check.append((r,c - 1))
            if c < len(row) - 1:
                check.append((r,c + 1))
            for cr, cc in check:
                ch = grid[cr][cc]
                if ch != '.' and not ch.isdigit():
                    valid = True
                    if ch == '*':
                        gears[(cr, cc)].append(num)
                    break
        else:
            if valid:
                valid_nums.add(id(num))
            valid = False
            num = []
    if valid:
        valid_nums.add(id(num))

s = 0
print(gears)
for gear in gears.values():
    ratio = None
    done = set()
    for l in gear:
        if id(l) in valid_nums and id(l) not in done:
            num = int(''.join(l))
            print(num)
            if ratio is None:
                ratio = 1
            ratio *= num
        done.add(id(l))
    if ratio is not None and len(done) >= 2:
        s += ratio
print(s)
