import sys
import itertools
import re

pat = re.compile('\.+')

match = 0
for line in sys.stdin.readlines():
    springs, counts = line.strip().split(' ')
    counts = list(map(int, counts.split(',')))
    for perm in itertools.product('.#', repeat=springs.count('?')):
        new_s = ''
        p = 0
        for s in springs:
            if s == '?':
                new_s += perm[p]
                p += 1
            else:
                new_s += s
        new_counts = list(map(len, pat.split(new_s.strip('.'))))
        if new_counts == counts:
            match += 1

print(match)
