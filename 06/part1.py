import sys
import re

times = list(map(int, re.split(' +', sys.stdin.readline().strip().split(':')[1].strip())))
distances = list(map(int, re.split(' +', sys.stdin.readline().strip().split(':')[1].strip())))

ret = 1
for time, dist in zip(times, distances):
    ways = 0
    for hold in range(1, time):
        remaining = time - hold
        if remaining * hold > dist:
            ways += 1
    ret *= ways
print(ret)
