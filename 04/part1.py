import sys
import re

t = 0
for line in sys.stdin.readlines():
    winning, my = line.split(':')[1].split('|')
    winning = set(map(int, re.split('\s+', winning.strip())))
    my = set(map(int, re.split('\s+', my.strip())))
    l = len(winning & my)
    if l > 0:
        t += 2 ** (l - 1)

print(t)
