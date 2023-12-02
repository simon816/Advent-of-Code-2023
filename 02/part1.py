import sys

tot = 0
for line in sys.stdin.readlines():
    line = line.strip()
    game, play = line.split(': ')
    game = int(game.strip().split(' ')[1])
    sets = play.split(';')
    possible = True
    for s in sets:
        contents = s.split(',')
        for c in contents:
            c = c.strip()
            qty, color = c.split(' ')
            qty = int(qty)
            if color == 'red' and qty > 12:
                possible = False
            if color == 'green' and qty > 13:
                possible = False
            if color == 'blue' and qty > 14:
                possible = False
    if possible:
        tot += game

print(tot)
