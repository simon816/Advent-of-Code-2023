import sys
from collections import defaultdict

stack = []
for line in sys.stdin.readlines():
    start, end = line.strip().split('~')
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))
    zmin, zmax = min(start[2], end[2]), max(start[2], end[2])
    # mutate coords such that lowest z is the start
    start[2] = zmin
    end[2] = zmax
    stack.append((start, end))

def intersect(a, b):
    astart, aend = a
    bstart, bend = b
    lower_ax = min(astart[0], aend[0])
    lower_ay = min(astart[1], aend[1])
    lower_az = min(astart[2], aend[2])
    upper_ax = max(astart[0], aend[0])
    upper_ay = max(astart[1], aend[1])
    upper_az = max(astart[2], aend[2])
    lower_bx = min(bstart[0], bend[0])
    lower_by = min(bstart[1], bend[1])
    lower_bz = min(bstart[2], bend[2])
    upper_bx = max(bstart[0], bend[0])
    upper_by = max(bstart[1], bend[1])
    upper_bz = max(bstart[2], bend[2])
    if upper_az < lower_bz or lower_az > upper_bz:
        return False
    if upper_ay < lower_by or lower_ay > upper_by:
        return False
    if upper_ax < lower_bx or lower_ax > upper_bx:
        return False
    return True

zsorted = sorted(stack, key=lambda b:b[0][2])

height_map = defaultdict(list)
highest = 999

for i, brick in enumerate(zsorted):
    start, end = brick
    if start[2] == 1:
        height_map[start[2]].append((tuple(start), tuple(end)))
        # ground level
        continue
    z = min(highest + 1, start[2])
    while z > 1:
        z -= 1
        new_start = (start[0], start[1], z)
        new_end = (end[0], end[1], end[2] - 1)
        too_far = False
        for n in range(i - 1, -1, -1):
            check = zsorted[n]
            if intersect((new_start, new_end), check):
                too_far = True
                break
        if too_far:
            z += 1
            break
    old = tuple(start), tuple(end)
    shift = start[2] - z
    start[2] = z
    end[2] -= shift
    height_map[z].append((tuple(start), tuple(end)))
    highest = max(highest, end[2])

count = 0
for z, bricks in height_map.items():
    for brick in bricks:
        upper_z = brick[1][2]
        # convert to tuple so != works
        without = [b for b in stack if (tuple(b[0]), tuple(b[1])) != brick]
        can_remove = False
        # Nothing above - must not be holding anything
        if upper_z + 1 not in height_map:
            can_remove = True
        else:
            can_remove = True
            for other in height_map[upper_z + 1]:
                start, end = other
                # lower the brick by 1
                start = (start[0], start[1], start[2] - 1)
                end = (end[0], end[1], end[2] - 1)
                still_supported = False
                for b in without:
                    # ignore the same brick that we are testing
                    if (tuple(b[0]), tuple(b[1])) == other:
                        continue
                    if intersect((start, end), b):
                        still_supported = True
                        break
                if not still_supported:
                    can_remove = False
                    break
        if can_remove:
            count += 1

print(count)
