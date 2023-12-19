import sys

dug = set()
pos = (0, 0) # x, y
dug.add(pos)

min_x, min_y, max_x, max_y = 0, 0, 0, 0

line_dirs = {}

for line in sys.stdin.readlines():
    dir, dist, _ = line.split(' ')
    dist = int(dist)
    if dir == 'U':
        shift = (0, 1)
    elif dir == 'D':
        shift = (0, -1)
    elif dir == 'L':
        shift = (-1, 0)
    elif dir == 'R':
        shift = (1, 0)
    else:
        assert False
    if dir in 'UD':
        line_dirs[pos] = dir
    for _ in range(dist):
        pos = pos[0] + shift[0], pos[1] + shift[1]
        dug.add(pos)
        if dir in 'RL':
            line_dirs[pos] = None
        else:
            line_dirs[pos] = dir
        min_x = min(min_x, pos[0])
        max_x = max(max_x, pos[0])
        min_y = min(min_y, pos[1])
        max_y = max(max_y, pos[1])

area = 0
for y in range(min_y, max_y + 1):
    inside = False
    winding = 0
    enter_line = None
    for x in range(min_x, max_x + 1):
        if (x, y) in dug:
            dir = line_dirs[(x, y)]
            if dir is not None:
                if enter_line is None:
                    enter_line = dir
                    inside = not inside
                else:
                    if dir == enter_line:
                        pass
                    else:
                        inside = not inside
                    enter_line = None
            area += 1
        elif inside:
            area += 1
            enter_line = None
        else:
            enter_line = None
print(area)
