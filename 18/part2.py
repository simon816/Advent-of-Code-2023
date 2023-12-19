import sys

pos = (0, 0) # x, y
points = []
perim = 0
for line in sys.stdin.readlines():
    hexval = int(line.split('#')[1][:-2], base=16)
    dir = hexval & 0xF
    dist = hexval >> 4
    if dir == 3:
        end = (pos[0], pos[1] + dist)
    elif dir == 1:
        end = (pos[0], pos[1] - dist)
    elif dir == 2:
        end = (pos[0] - dist, pos[1])
    elif dir == 0:
        end = (pos[0] + dist, pos[1])
    else:
        assert False
    points.append(pos)
    pos = end
    perim += dist

assert pos == (0, 0)

s = 0
for (x1, y1), (x2, y2) in zip(points, points[1:] + [points[0]]):
    s += (y1 + y2) * (x1 - x2)
area = abs(s // 2)
# remove half the perimiter (area includes 1 width)
# XXX: Why are we off by one?
print((area - (perim//2)) + perim + 1)
