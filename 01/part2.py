import sys

s = 0

nums = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

for line in sys.stdin.readlines():
    line = line.strip()
    minidx = 999
    maxidx = -1
    first = None
    last = None
    for n, v in nums.items():
        idx = line.find(n)
        if idx != -1 and idx < minidx:
            minidx = idx
            first = v
        idx = line.rfind(n)
        if idx != -1 and idx > maxidx:
            maxidx = idx
            last = v
    for i, n in enumerate(line):
        if n.isdigit():
            if i < minidx:
                minidx = i
                first = int(line[i])
            if i > maxidx:
                maxidx = i
                last = int(line[i])
    num = (first * 10) + last
    s += num

print(s)
