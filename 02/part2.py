import sys

tot = 0
for line in sys.stdin.readlines():
    line = line.strip()
    game, play = line.split(': ')
    game = int(game.strip().split(' ')[1])
    sets = play.split(';')
    mins = { 'red': 0, 'green': 0, 'blue': 0 }
    for s in sets:
        contents = s.split(',')
        for c in contents:
            c = c.strip()
            qty, color = c.split(' ')
            qty = int(qty)
            mins[color] = max(mins[color], qty)
    power = mins['red'] * mins['green'] * mins['blue']
    tot += power

print(tot)
