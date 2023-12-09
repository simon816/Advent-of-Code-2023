import sys

s = 0
for line in sys.stdin.readlines():
    vals = list(map(int, line.strip().split(' ')))
    chain = [vals]
    while not all(v == 0 for v in vals):
        new_vals = []
        for a, b in zip(vals[:-1], vals[1:]):
            new_vals.append(b - a)
        vals = new_vals
        chain.append(vals)

    dec = 0
    for vals in chain[::-1]:
        dec = vals[0] - dec
    s += dec

print(s)
