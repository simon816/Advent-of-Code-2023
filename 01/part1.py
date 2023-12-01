import sys

s = 0

for line in sys.stdin.readlines():
    first = None
    last = None
    for d in line:
        if d.isdigit():
            if first is None:
                first = int(d)
            last = int(d)
    num = (first * 10) + last
    s += num

print(s)
