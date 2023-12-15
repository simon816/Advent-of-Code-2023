import sys

tot = 0
strings = sys.stdin.readline().strip().split(',')
for s in strings:
    cv = 0
    for v in s:
        cv += ord(v)
        cv *= 17
        cv = cv % 256
    tot += cv

print(tot)
