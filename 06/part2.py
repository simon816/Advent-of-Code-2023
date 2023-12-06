import sys
import re

time = int(re.sub('\s+', '', sys.stdin.readline().split(':')[1]))
distance = int(re.sub('\s+', '', sys.stdin.readline().split(':')[1]))

ways = 0
for hold in range(1, time):
    remaining = time - hold
    if remaining * hold > distance:
        ways += 1
print(ways)
