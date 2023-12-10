import sys


grid = []

row = 0
start = None
for line in sys.stdin.readlines():
    line = line.strip()
    idx = line.find('S')
    grid.append(line)
    if idx != -1:
        start = row, idx
    row += 1


start_r, start_c = start
con = []
if start_r > 0:
    if grid[start_r - 1][start_c] in '|7F':
        con.append((start_r - 1, start_c, 'N'))
if start_r < len(grid) - 1:
    if grid[start_r + 1][start_c] in '|LJ':
        con.append((start_r + 1, start_c, 'S'))
if start_c > 0:
    if grid[start_r][start_c - 1] in '-FL':
        con.append((start_r, start_c - 1, 'W'))
if start_c < len(grid[start_r]) - 1:
    if grid[start_r][start_c + 1] in '-7J':
        con.append((start_r, start_c + 1, 'E'))

assert len(con) == 2

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

cell = con[0]
dist = 1
while True:
    cell = step(*cell)
    dist += 1
    if cell[0] == con[1][0] and cell[1] == con[1][1]:
        break

# XXX: Why +1?
dist += 1
print(dist / 2)
