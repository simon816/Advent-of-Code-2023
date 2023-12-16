import sys

grid = []
width = 0
for line in sys.stdin.readlines():
    line = line.strip()
    width = max(width, len(line))
    grid.append(line)

def run(init):
    beams = set((init,))
    seen = set()
    energised = set()
    while len(beams):
        new_beams = set()
        for beam in beams:
            if beam in seen:
                continue
            seen.add(beam)
            r, c, dir = beam
            if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[r]) - 1:
                continue
            energised.add((r, c))
            tile = grid[r][c]
            if tile == '.':
                if dir == 'N':
                    r -= 1
                elif dir == 'E':
                    c += 1
                elif dir == 'S':
                    r += 1
                elif dir == 'W':
                    c -= 1
            elif tile == '|':
                if dir in 'EW':
                    new_beams.add((r - 1, c, 'N'))
                    r += 1
                    dir = 'S'
                elif dir == 'N':
                    r -= 1
                elif dir == 'S':
                    r += 1
            elif tile == '-':
                if dir in 'NS':
                    new_beams.add((r, c + 1, 'E'))
                    c -= 1
                    dir = 'W'
                elif dir == 'E':
                    c += 1
                elif dir == 'W':
                    c -= 1
            elif tile == '/':
                if dir == 'N':
                    dir = 'E'
                    c += 1
                elif dir == 'E':
                    dir = 'N'
                    r -= 1
                elif dir == 'S':
                    dir = 'W'
                    c -= 1
                elif dir == 'W':
                    dir = 'S'
                    r += 1
            elif tile == '\\':
                if dir == 'N':
                    dir = 'W'
                    c -= 1
                elif dir == 'E':
                    dir = 'S'
                    r += 1
                elif dir == 'S':
                    dir = 'E'
                    c += 1
                elif dir == 'W':
                    dir = 'N'
                    r -= 1
            else:
                assert False
            new_beams.add((r, c, dir))
        beams = new_beams
    return len(energised)

vals = []
for r in range(len(grid)):
    vals.append(run((r, 0, 'E')))
    vals.append(run((r, width - 1, 'W')))

for c in range(width):
    vals.append(run((0, c, 'S')))
    vals.append(run((len(grid) - 1, c, 'N')))

print(max(vals))
