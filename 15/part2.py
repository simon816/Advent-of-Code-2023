import sys
from collections import OrderedDict

boxes = [OrderedDict() for _ in range(256)]

strings = sys.stdin.readline().strip().split(',')
for s in strings:
    action = None
    fl = None
    if s[-1] == '-':
        label = s[:-1]
        action = 'del'
    else:
        label, fl = s.split('=')
        fl = int(fl)
        action = 'add'
    cv = 0
    for v in label:
        cv += ord(v)
        cv *= 17
        cv = cv % 256
    box = boxes[cv]
    if action == 'del':
        if label in box:
            del box[label]
    else:
        box[label] = fl

tot = 0
for i in range(256):
    box = boxes[i]
    for pos, fl in enumerate(box.values()):
        power = (i + 1) * (pos + 1) * fl
        tot += power

print(tot)
